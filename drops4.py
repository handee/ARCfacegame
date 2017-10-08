
import cv2
import video
import sys
import numpy as np
from random import randint



# These are variables, which decide how big the picture is going to be
# and how many milliseconds to wait before updating the picture
width=400
height=400
frame_length=10

drop_size=10
x_position=200
y_position=5
blue=255
green=100
red=100

# Open a window
cv2.namedWindow('drops')

# Create an image 
myimage=np.zeros((height,width,3), np.uint8)


while True:
   myimage=np.zeros((height,width,3), np.uint8)

   # Change the y_position of the drop
   y_position=y_position+1
   
   # If it goes off the bottom of the screen, put it back at the top
   if (y_position>height):
      y_position=5

   # Draw a circle on the image    
   cv2.circle(myimage,(x_position,y_position), drop_size, (blue,green,red), -1)


   # Show the image in the window
   cv2.imshow('drops',myimage)
   
   # Wait a bit for a key to be pressed. This line also redraws the 
   # pictures so it's important
   ch=cv2.waitKey(frame_length) & 0xFF

   # If that key is 27 ("ESC") then quit
   if ch==27:
      break
