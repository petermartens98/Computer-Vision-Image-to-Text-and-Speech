# Image to Text
# Version 1

# Import necessary libraries
import cv2
import pytesseract
import matplotlib.pyplot as plt

# File reference to pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

## Define Functions

# Function to grayscale Image
def grayscale(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Thresholding Function
def threshold(img):
    return cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

# Function to remove noise
def remove_noise(img):
    return cv2.medianBlur(img, 5)

# Function using tesseract to return text from image
def ocr_core(img):
    img_text = pytesseract.image_to_string(img)
    return img_text

# Read in image
img = cv2.imread('BookPage1.jpg')

#plt.imshow(img)

# Transform image and prepare for OCR model
img = grayscale(img)
img = threshold(img)
img = remove_noise(img)

# print text from image
print(ocr_core(img))

print("code completed")
