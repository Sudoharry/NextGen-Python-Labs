from pdf2docx import Converter
import os

pdf_file = r'C:\Users\Nilesh\Downloads\HarendraBarot_CV_04_2025r.pdf'
docx_file = r'C:\Users\Nilesh\Downloads\HarendraBarot_CV_04_2025r.docx'

if os.path.exists(pdf_file):
    cv = Converter(pdf_file)
    cv.convert(docx_file)
    cv.close()
    print("✅ Conversion complete.")
else:
    print("❌ PDF file not found.")

cv = Converter(pdf_file)
cv.convert(docx_file, start=0, end=None)
cv.close()
