import os
import pikepdf

pdfs = [pdf for pdf in os.listdir('.') if os.path.isfile(f)]

for pdf in pdfs:
	print(pdf)
	if f.endswith(".pdf"):
		pdf = pikepdf.Pdf.open(f, allow_overwriting_input = True)
		pdf.save(f)
