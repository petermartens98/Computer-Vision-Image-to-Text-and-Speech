# Image to Speech
# Version 1

# Import necessary libraries
import cv2
import pytesseract
import matplotlib.pyplot as plt
import pyttsx3

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

# Transform image and prepare for OCR model
img = grayscale(img)
img = threshold(img)
img = remove_noise(img)

# define text from image
text = ocr_core(img)

# Remove blank spaces from text
cleaned_text = text.replace('\n', ' ').replace('\r', '')

# Initialize voice engine
engine = pyttsx3.init()

# Set voice speaking rate , default = 200
engine.setProperty('rate', 150)

# Set male or female voice id
female_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
male_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"
engine.setProperty('voice', male_voice_id)

# Have voice engine recite cleaned text
engine.say(cleaned_text)
engine.runAndWait()

# Print to indicate code is finished
print("code completed")
