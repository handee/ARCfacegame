# This demo has all the shape types and also images.

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
# starting location of first shape
x=200
y=5
blue=255
green=100
red=100

# starting location and colour of second shape
x2=100
y2=5
b2=25
g2=250
r2=50

# starting location and colour of third shape
x3=50
y3=5
b3=0
g3=250
r3=250

# starting location and colour of fourth shape
x4=100
y4=5
b4=0
g4=250
r4=250

# Open a window
cv2.namedWindow('drops')

# Create an image 
myimage=np.zeros((height,width,3), np.uint8)


while True:
   myimage=np.zeros((height,width,3), np.uint8)

   # Change the y of the drop
   y=y+1
   
   # Change the x of the second drop
   x2=x2+2

   # Change the y of the second drop
   y3=y3+2

   # Change the y AND THE X! of the fourth drop
   y4=y4+1
   # Change the y AND THE X! of the fourth drop
   x4=x4+2

   # If shape 1 goes off the bottom of the screen, put it back at the top
   if (y>height):
      y=5
      # move the x to a random place from 0 (left-hand-side) 
      # to width (right-hand-side)
      x=randint(0,width)

  # If shape 2 goes off the side of the screen, put it back at the left 
   if (x2>width):
      x2=5
      # move the y to a random place from 0 (top-side) 
      # to height (bottom-side)
      y2=randint(0,height)


  # If shape 3 goes off the bottom of the screen, put it back at the top
   if (y3>height):
      y3=5
      # move the x to a random place from 0 (left-hand-side) 
      # to width (right-hand-side)
      x3=randint(0,width)

  # if shape 4 goes off the bottom of the screen or the side of the screen,
  # put it back at top
   if (y4>height) or (x4>width):
      y4=5
      # move the x to a random place from 0 (left-hand-side) 
      # to width (right-hand-side)
      x4=randint(0,width)

   # Draw a circle on the image 
   cv2.circle(myimage,(x,y), drop_size, (blue,green,red), -1)
   # Draw a square on the image (a square is a rectangle!)
   cv2.rectangle(myimage,(x2,y2), (x2+drop_size, y2+drop_size), (b2,g2,r2), -1)
   # Draw a rectangle on the image (make one of the sides bigger) 
   cv2.rectangle(myimage,(x3,y3), (x3+drop_size, y3+drop_size+5), (b3,g3,r3), -1)
   # Draw a line on the image
   cv2.line(myimage,(x4,y4), (x4+drop_size,y4), (b4,g4,r4), 2)

   # Show the image in the window
   cv2.imshow('drops',myimage)
   
   # Wait a bit for a key to be pressed. This line also redraws the 
   # pictures so it's important
   ch=cv2.waitKey(frame_length) & 0xFF

   # If that key is 27 ("ESC") then quit
   if ch==27:
      break
