
from PyPDF2 import PdfMerger

pdfs=["CamScanner 10-29-2021 14.58.pdf","Result Of All Semesters Combined.pdf"]

#first double qoute should contain the name of the pdfs you wanna merge and the 2nd double qoute aka the last one should contain the name of the pdf that will be created as one merged pf

merger=PdfMerger()

for i in pdfs:
    merger.append(i)

merger.write("Test.pdf")
merger.close()
