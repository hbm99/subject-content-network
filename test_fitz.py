import fitz

doc = fitz.open("Conferencia-00-MN-CC-2021-(con-imagenes).pdf")

accum_text = ''
for i in range(doc.page_count):
    page = doc.load_page(i)
    text = page.get_text('text')
    accum_text += text

print(accum_text)