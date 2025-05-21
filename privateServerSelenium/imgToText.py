from PIL import Image
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

def imgtotext():
  img = Image.open('screenshots/antibot.png')
  text = tess.image_to_string(img)
  return text