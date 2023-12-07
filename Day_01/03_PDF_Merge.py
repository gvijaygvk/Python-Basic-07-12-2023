import os
import PyPDF2
from PyPDF2 import PdfReader , PdfWriter, PdfMerger
pdfFiles = []

for root, dirs, filenames in os.walk(os.getcwd()):
    for filename in filenames:
        if filename.lower().endswith('.pdf'):
            pdfFiles.append(os.path.join(root, filename))

pdfFiles.sort(key=str.lower)
pdfWriter = PyPDF2.PdfWriter()

for filename in pdfFiles:
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfReader(pdfFileObj)
    for pageNum in range(0, len(pdfReader.pages)):
        pageObj = pdfReader.pages[pageNum]
        pdfWriter.add_page(pageObj)

pdfOutput = open('Mergered_pdf.pdf', 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()