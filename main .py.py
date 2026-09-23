from PyPDF2 import PdfWriter
merger = PdfWriter()

pdfs = []
n = int (input(" How many pdf files do you want to merge? "))
for i in range(n):
    name = input (f" Enter PDF file {i+1}: ")
    pdfs.append(name)

for pdf in pdfs:
    merger.append(pdf)

output = input("Enter the name of the merged PDF:")
merger.write(output +".pdf")
merger.close()


 