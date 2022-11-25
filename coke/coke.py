

total_paid = 0

while total_paid < 50:
    get_coin = input("Insert a coin: ")
    coin = int(get_coin)




    if coin == 5 or coin == 10 or coin == 25:
        total_paid = total_paid + coin
    else:
        total_paid = 0


    amount_due = 50 - total_paid

    if amount_due > 0:
        print(f"Amount due: {amount_due}")
    else:
        continue

else:
    amount_owed = abs((total_paid - 50))
    print(f"Change owed: {amount_owed}")





