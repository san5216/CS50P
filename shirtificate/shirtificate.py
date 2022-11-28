from fpdf import FPDF

pdf = FPDF()
pdf.set_margin(30)
pdf.set_auto_page_break(auto=False)
pdf.add_page()
pdf.set_font(family="helvetica", size=50)
pdf.oversized_images = "DOWNSCALE"

# Place title on page, centered
pdf.cell(w=0, txt='CS50 Shirtificate', align='C')

# Place shirt image centered on page
pdf.image("shirtificate.png", x=0.5, y=60)



# Place User's name on top of shirt, in white, centered
name = input("Name: ")
pdf.set_font(family="helvetica", style='B', size=35)
pdf.set_xy(25, 150)
pdf.set_text_color(r=255, g=255, b=255)
pdf.cell(w=0, txt=f'{name} took CS50', align='C')


# Output page to PDF
pdf.output("shirtificate.pdf")
