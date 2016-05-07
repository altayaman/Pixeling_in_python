import numpy as np
import pandas as pn
import matplotlib.pyplot as plt
from math import sqrt
from PIL import Image 
from PIL import PngImagePlugin
from dotmap import DotMap


small_eightImagePath = 'C:/Users/Altay/Desktop/small_eight.png'
eightImagePath = 'C:/Users/Altay/Desktop/eight55.png'
nineImagePath = 'C:/Users/Altay/Desktop/nine.png'
squareImagePath1 = 'C:/Users/Altay/Desktop/square1.png'
squareImagePath2 = 'C:/Users/Altay/Desktop/square2.png'
circleImagePath1 = 'C:/Users/Altay/Desktop/circle1.png'
circleImagePath2 = 'C:/Users/Altay/Desktop/circle2.png'


small_eightImage = Image.open(small_eightImagePath)
# eightImage = Image.open(eightImagePath)
nineImage = Image.open(nineImagePath)
squareImage1 = Image.open(squareImagePath1)
squareImage2 = Image.open(squareImagePath2)
circleImage1 = Image.open(circleImagePath1)
circleImage2 = Image.open(circleImagePath2)


#  Set image to be processed
img = nineImage

#____________________________________________________________________
#
#  Create array with image dimensions and fill it with img
#  by putting 0's for white pixels and 1's for non-white pixels
#____________________________________________________________________

#  empty array
arr = np.zeros(shape=(img.size[1], img.size[0]))
print('Array size: ', arr.shape)

start_pixel = DotMap()
stop_pixel = DotMap()
start_pixel_found = False
RGB = ()

#  fill array with image
for x in range(img.size[0]):
    for y in range(img.size[1]):
        RGB = img.getpixel((x, y))
        if(RGB[0] != 255 or RGB[1] != 255 or RGB[2] != 255):   #  Mark as 1, if pixel is not white color point
            arr[y, x] = '1'
            if(start_pixel_found == False):   #   Set first encountered pixel with 8 as start-pixel
                arr[y, x] = '8'
                start_pixel.x = y
                start_pixel.y = x
                start_pixel_found = True
        

#  Convert array into data frame 
df = pn.DataFrame(arr)

#________________________________________________
#
#  Find edge pixels
#________________________________________________


#  Pass coordinates of start-pixel
x,  y  =  start_pixel.x,  start_pixel.y
print('Starting edge pixel: x = ', x, '  y = ', y)


#  Calculate stop-pixel (e.g. last edge pixel)
#  according to right-hand search
if(arr[x + 1][y - 1] == 1):
    stop_pixel.x = x + 1
    stop_pixel.y = y - 1
elif(arr[x + 1][y] == 1):
    stop_pixel.x = x + 1
    stop_pixel.y = y
elif(arr[x + 1][y + 1] == 1):
    stop_pixel.x = x + 1
    stop_pixel.y = y + 1
elif(arr[x][y + 1] == 1):
    stop_pixel.x = x
    stop_pixel.y = y + 1
elif(arr[x - 1][y + 1] == 1):
    stop_pixel.x = x - 1
    stop_pixel.y = y + 1

print('Stopping edge pixel: x = ', stop_pixel.x, '  y = ', stop_pixel.y)


#  Create DotMap to store edge-pixels coordinates
#  and their length from the xy-origin (0,0)
edge_pixels = DotMap()
edge_pixels.x_coordinates = []
edge_pixels.y_coordinates = []
edge_pixels.orig_distance = []
edge_pixels.adjust_distance = []

orig_len = 0.0
adjust_len = 0.0
x_ = 0.0
y_ = 0.0
face_direction = 'left'   #  initial face direction (because search of initial start-pixel starts from left side of image)

#  Find all edge pixels by using right-hand search starting from start-pixel
#  and mark them with 8s
while(True):
    
    #  Transform x,y coordinates of 2D-array 
    #  into normal XY-coordinate plane axes
    x_ = y                      #  in case of 2D-arrays, y-axis is a x-axis of real XY-coordinate plane 
    y_ = abs(img.size[1] - x)   #  in case of 2D-arrays, x-axis is a y-axis of real XY-coordinate plane
                                #   which starts from upper-side instead of lower-side
    
    #  Calculate original distance and adjusted distance 
    #  between edge-pixel point and xy-origin (0,0)
    orig_distance = sqrt(x_ ** 2 + y_ ** 2)
    adjust_distance = (int(orig_distance) + 1) if((orig_distance%1) >= 0.8) else int(orig_distance)   #  take decimal part by rounding if >= 0.8 
    
    #  Store the x, y and the distances
    edge_pixels.x_coordinates.append(x_)
    edge_pixels.y_coordinates.append(y_)
    edge_pixels.orig_distance.append(orig_distance)
    edge_pixels.adjust_distance.append(adjust_distance)
    

# Stop IF last edge pixel
    if(x == stop_pixel.x and y == stop_pixel.y):
        x_ = start_pixel.y
        y_ = abs(img.size[1] - start_pixel.x)
        orig_distance = sqrt(x_ ** 2 + y_ ** 2)
        adjust_distance = (int(orig_distance) + 1) if((orig_distance%1) >= 0.8) else int(orig_distance)
        edge_pixels.x_coordinates.append(x_)
        edge_pixels.y_coordinates.append(y_)
        edge_pixels.orig_distance.append(orig_distance)
        edge_pixels.adjust_distance.append(adjust_distance)
        break
# IF facing LEFT side
    elif(face_direction == 'left'):
        if(arr[x - 1][y - 1] == 1):
            x = x - 1
            y = y - 1
            arr[x][y] = 8
            face_direction = 'down'
            print('LEFT -> DOWN')
        elif(arr[x - 1][y] == 1):
            x = x - 1
            arr[x][y] = 8
        elif(arr[x - 1][y + 1] == 1):
            x = x - 1
            y = y + 1
            arr[x][y] = 8
        elif(arr[x][y + 1] == 1):
            y = y + 1
            arr[x][y] = 8
            face_direction = 'up'
            print('LEFT -> UP')
        elif(arr[x + 1][y + 1] == 1):
            x = x + 1
            y = y + 1
            arr[x][y] = 8
            face_direction = 'up'
            print('LEFT -> UP')
        elif(arr[x + 1][y] == 1):
            x = x + 1
            arr[x][y] = 8
            face_direction = 'right'
            print('LEFT -> RIGHT')
        print('LEFT:  x - ', x, ' y - ', y)
# IF facing UP side 
    elif(face_direction == 'up'):
        if(arr[x - 1][y + 1] == 1):
            x = x - 1
            y = y + 1
            arr[x][y] = 8
            face_direction = 'left'
            print('UP -> LEFT')
        elif(arr[x][y + 1] == 1):
            y = y + 1
            arr[x][y] = 8
        elif(arr[x + 1][y + 1] == 1):
            x = x + 1
            y = y + 1
            arr[x][y] = 8
        elif(arr[x + 1][y] == 1):
            x = x + 1
            arr[x][y] = 8
            face_direction = 'right'
            print('UP -> RIGHT')
        elif(arr[x + 1][y - 1] == 1):
            x = x + 1
            y = y - 1
            arr[x][y] = 8
            face_direction = 'right'
            print('UP -> RIGHT')
        elif(arr[x][y - 1] == 1):
            y = y - 1
            arr[x][y] = 8
            face_direction = 'down'
            print('UP -> DOWN')
        print('UP:  x - ', x, ' y - ', y) 
# IF facing RIGHT side
    elif(face_direction == 'right'):
        if(arr[x + 1][y + 1] == 1):
            x = x + 1
            y = y + 1
            arr[x][y] = 8
            face_direction = 'up'
            print('RIGHT -> UP')
        elif(arr[x + 1][y] == 1):
            x = x + 1
            arr[x][y] = 8
        elif(arr[x + 1][y - 1] == 1):
            x = x + 1
            y = y - 1
            arr[x][y] = 8
        elif(arr[x][y - 1] == 1):
            y = y - 1
            arr[x][y] = 8
            face_direction = 'down'
            print('RIGHT -> DOWN')
        elif(arr[x - 1][y - 1] == 1):
            x = x - 1
            y = y - 1
            arr[x][y] = 8
            face_direction = 'down'
            print('RIGHT -> DOWN')
        elif(arr[x - 1][y] == 1):
            x = x - 1
            arr[x][y] = 8
            face_direction = 'left'
            print('RIGHT -> LEFT')
        print('RIGHT:  x - ', x, ' y - ', y)  
# IF facing DOWN side
    elif(face_direction == 'down'):
        if(arr[x + 1][y - 1] == 1):
            x = x + 1
            y = y - 1
            arr[x][y] = 8
            face_direction = 'right'
            print('DOWN -> RIGHT')
        elif(arr[x][y - 1] == 1):
            y = y - 1
            arr[x][y] = 8
        elif(arr[x - 1][y - 1] == 1):
            x = x - 1
            y = y - 1
            arr[x][y] = 8
        elif(arr[x - 1][y] == 1):
            x = x - 1
            arr[x][y] = 8
            face_direction = 'left'
            print('DOWN -> LEFT')
        elif(arr[x - 1][y + 1] == 1):
            x = x - 1
            y = y + 1
            arr[x][y] = 8
            face_direction = 'left'
            print('DOWN -> LEFT')
        elif(arr[x][y + 1] == 1):
            y = y + 1
            arr[x][y] = 8
            face_direction = 'up'
            print('DOWN -> UP')
        print('DOWN:  x - ', x, ' y - ', y)
                   

        
#  Calculate dimensions for data frame
#  that will store linear form of image
edge_pixels_count = len(edge_pixels.x_coordinates)
max_distance = max(edge_pixels.adjust_distance) # distance of the most distant edge pixel from origin (0,0)

#  Create empty data frame and fill it with 0s
df2 = pn.DataFrame(index=range(max_distance + 5), columns = range(edge_pixels_count))
df2 = df2.fillna(0)

for i in range(edge_pixels_count):
    for j in range(edge_pixels.adjust_distance[i]):
        df2[i][j] = 8



# Write data frames to Excel file 
writer = pn.ExcelWriter('E:/1 - ShapeToLineConversion.xlsx')
df.to_excel(writer,'Sheet1')  # export image shape into Sheet1
df2.to_excel(writer,'Sheet2') # export linear shape into Sheet2
writer.save()

print('Excel file saved ...')

#  Plot the image shape
plt.plot(edge_pixels.x_coordinates, edge_pixels.y_coordinates, label="image shape")
plt.scatter(edge_pixels.x_coordinates, edge_pixels.y_coordinates)
plt.xlim([0, img.size[0]])  # set x-axis range from 0 to img.size[0] (e.g. image width)
plt.ylim([0, img.size[1]])  # set y-axis range from 0 to img.size[1] (e.g. image heigth)
plt.grid()
plt.gca().set_aspect('equal', adjustable='box')  # set x-axis and y-axis equally-scaled 
# plt.legend(loc='upper left')
plt.show()


#  Plot the linear shape
plt.plot(list(range(edge_pixels_count)), edge_pixels.adjust_distance, label="linear shape")
plt.scatter(list(range(edge_pixels_count)), edge_pixels.adjust_distance)
plt.xlim([-2, edge_pixels_count + 2])
plt.ylim([0, max_distance + 5])
plt.grid()
plt.gca().set_aspect('equal', adjustable='box')
# plt.legend(loc='upper left')
plt.show()