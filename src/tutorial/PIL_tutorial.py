from PIL import Image 
from PIL import PngImagePlugin
import numpy as np
import pandas as pn

whiteImagePath = 'C:/Users/Altay/Desktop/white.png'
blackImagePath = 'C:/Users/Altay/Desktop/black.png'

whiteImage = Image.open(whiteImagePath)
blackImage = Image.open(blackImagePath)
# a,b = size = whiteImage.size

# ***  TUTORIALS  ******************************************************************************************
coordinates = 12, 12
print('Format of white image: ', whiteImage.format)
print('Mode of white mode: ', whiteImage.mode)
print('Size of white image: ', whiteImage.size)
print('RGB of white pixel at: ', whiteImage.getpixel(coordinates), ' x,y - coordinates: ', coordinates, ' option - 1')
print('RGB of black pixel at: ', blackImage.getpixel(coordinates), ' x,y - coordinates: ', coordinates)
 
img = whiteImage.load()
print('RGB of white pixel at: ', img[coordinates], ' x,y - coordinates: ', coordinates, ' option - 2')
blackImage.show()

# **********************************************************************************************************