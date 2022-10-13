from PIL import Image
from pytesseract import pytesseract

# You'll need to specify the path to the tesseract
path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
image_path = r"Sam.jpg"

img = Image.open(image_path)
pytesseract.tesseract_cmd = path_to_tesseract

# Extract the text from the image
text = pytesseract.image_to_string(img)

# Print the text
print(text[:])
