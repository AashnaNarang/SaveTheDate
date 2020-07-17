from PIL import Image
import pytesseract
import argparse
import cv2
import re
import sys
import PyPDF2
import requests

def image_to_text(image):
    image = 'dates.jpg'
    img = cv2.imread(image)
    text = pytesseract.image_to_string(img)
    parser(text)

def pdf_to_text(pdf):
    pdf = "GNG1105-Course-Schedule.pdf"
    pdfFileObject = open(pdf, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObject)
    count = pdfReader.numPages
    for i in range(count):
        page = pdfReader.getPage(i)
        parser(page.extractText())

def parser(text):
    for match in re.finditer(
        r"""(?ix)             # case-insensitive, verbose regex
        (?:([1-9]?[0-9])[a-zA-Z ]{0,20}(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec))
        |
        (?:(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-zA-Z ]{0,20}([1-9]?[0-9]))       
        """,  # and end at a word boundary.
        text):
        match.start()
        match.end()
        print(match.group())

# x = datetime.datetime.now()
#
# print(x.year)
