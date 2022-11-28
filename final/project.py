"""
* Must have a 'main' function and 3 or more additional functions.
* Any pip-installable libraries must be listed, one per line, in a file called 'requirements.txt'


* Get quote from https://www.affirmations.dev/

"""

import requests
import smtplib
import email
import imaplib
import datetime
from email.message import EmailMessage

MY_EMAIL = "shawn.norris.test@gmail.com"
MY_PASSWORD = "gyxwnudtgpfzkybt"

SMTP_SERVER = "smtp.gmail.com"
IMAP_SERVER = "imap.gmail.com"


def main():
    t_date = datetime.date.today()
    y_date = t_date - datetime.timedelta(days=1)

    affirm = load_previous_affirmation()
    fetch_reply_email(y_date, affirm)

    affirm = get_affirmation_text()

    save_affirmation(affirmation=affirm)

    send_affirmation_email(aff_text=affirm, today_date=t_date)


def load_previous_affirmation():
    with open("affirmations.csv", "r") as quote_file:
        data = quote_file.readlines()[-1]
        affirm = data[12:-4]
    return affirm


def save_affirmation(affirmation):
    with open("affirmations.csv", "a") as wf:
        wf.write(affirmation)


def get_affirmation_text():
    """
    Get an affirmation message from affirmations.dev/
    :return: string of affirmation
    """

    response = requests.get(url="https://www.affirmations.dev/")
    text = response.json()["affirmation"]
    return text


def send_affirmation_email(aff_text, today_date):
    """
    Send text with day's date in subject and affirmation message as body
    :param aff_text: string of affirmation
    :param today_date: today's date
    :return: None
    """

    print("Sending affirmation email")

    msg = EmailMessage()
    msg.set_content(aff_text)

    msg['Subject'] = f'{today_date} journal entry'
    msg['From'] = MY_EMAIL
    msg['To'] = MY_EMAIL

    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.send_message(msg)

    print("Affirmation email sent")


def fetch_reply_email(yesterday, aff_text):
    """
    Get reply to affirmation email sent
    :return: email date and body
    """

    print('Fetching emails')

    mail = imaplib.IMAP4_SSL("imap.gmail.com", 993)
    mail.login(MY_EMAIL, MY_PASSWORD)
    mail.select('inbox')

    status, data = mail.search(None, "ALL")

    mail_ids = []
    for block in data:
        mail_ids += block.split()

    for i in mail_ids:
        status, msg = mail.fetch(i, '(RFC822)')

        for response_part in msg:
            if isinstance(response_part, tuple):
                message = email.message_from_bytes(response_part[1])

                mail_subject = message["Subject"]

                if message.is_multipart():
                    body = ""
                    for part in message.get_payload():
                        if part.get_content_type() == 'text/plain':
                            body += part.get_payload()
                else:
                    body = message.get_payload()

                if f"Re: {yesterday}" in mail_subject:
                    entry = format_journal_entry(mail_subject, body, aff_text, yesterday)
                    append_to_journal(entry)

    # delete_emails()


def format_journal_entry(subject, content, affirm, yesterday):
    # yesterday = datetime.date.today()
    entry_date = subject[4:15]
    search_date = yesterday.strftime("%a, %b %d, %Y")
    result = content.index(f"On {search_date} ")
    entry_body = content[:result]

    entry = f"{entry_date}\n\n{affirm}\n\n{entry_body}\n\n"

    return entry


def append_to_journal(entry):
    with open('journal.txt', "a") as wf:
        wf.write(entry)


def delete_emails():
    ...


if __name__ == "__main__":
    print(load_previous_affirmation())
