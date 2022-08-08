import PyPDF2 as pdf
from random import shuffle
from io import BytesIO

def processPDF(file):
    reader = pdf.PdfFileReader(file,)
    pages = [page for page in reader.pages]
    shuffle(pages)
    writer = pdf.PdfFileWriter()
    while pages:
        writer.add_page(pages.pop())
    dest = BytesIO()
    writer.write(dest)
    return dest