from PIL import Image, ImageFilter, ImageEnhance
import os

# Get the path of the image to be compressed
path = './img'
pathOut = './imgOut'

for file in os.listdir(path):
    if file.endswith(".jpeg"):
        # Open the image
        img = Image.open(path + '/' + file)
        # Resize the image
        img = img.resize((300, 500), Image.ANTIALIAS)
        # Save the image
        img.save(pathOut + '/' + file, optimize=True, quality=85)