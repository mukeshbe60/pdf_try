
//////to read pdf file



pip install PyPDF2
import PyPDF2
# creating a pdf reader object
reader = PyPDF2.PdfReader('D:/newfolder/sample.pdf')

# print the number of pages in pdf file
print(len(reader.pages))

# print the text of the first page
print(reader.pages[0].extract_text())









======================================
import pytesseract
from pdf2image import convert_from_path
import glob
pdfs = glob.glob(r"D:/dataset_try/sample.pdf")
for pdf_path in pdfs:
    pages = convert_from_path(pdf_path, 500)
    
    for pageNum,imgBlob in enumerate(pages):
        text = pytesseract.image_to_string(imgBlob, lang='eng')
        
        with open(f'{pdf_path[:-4]}_page_{pageNum}.txt', 'w') as the_file:
            the_file.write(text)

