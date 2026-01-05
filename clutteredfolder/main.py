from PyPDF2 import PdfMerger
import os

merger = PdfMerger()

pdf_files = [file for file in os.listdir() if file.endswith(".pdf") and file != "merged-pdf.pdf"]

# Sort files (optional – so file1, file2, file3 order is correct)
pdf_files.sort()

for pdf in pdf_files:
    print(f"Adding: {pdf}")
    merger.append(open(pdf, 'rb'))

output_name = "merged-pdf.pdf"
merger.write(output_name)
merger.close()

print(f"✅ Merged PDF saved as {output_name}")