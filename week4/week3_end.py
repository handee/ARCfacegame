
import cv2
import video
import common
import sys
import numpy as np
from random import randint

cv2.namedWindow('My Game')

# Colour for the face box
b=50
g=50
r=200
faceboxcolour=(b,g,r)

# Start location and colour of falling circle 
xdrop=100 
ydrop=5
dropsize=10
bdrop=250
gdrop=25
rdrop=250
dropcolour=(bdrop,gdrop,rdrop)
dropspeed=3



#The face detector can have minimum and maximum sizes. 
mn=30 # minimum face width
mx=500 # maximum face width

#these two lines set up the face detector and the video input
cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
cam = video.create_capture(0)

while True:
   # read an image from the video camera
   ret, img = cam.read()
   width,height=img.shape[:2] # find out how big the image is
   
   # convert the image to greyscale (black and white) storing it in the 
   # variable "grey"
   grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
   
   # run the face detector on the grey image and store the output in 
   # the variable "rects"
   rects = cascade.detectMultiScale(grey, scaleFactor=1.3, minNeighbors=3, minSize=(mn, mn), maxSize=(mx,mx))

  
   # Change the y of the drop
   ydrop=ydrop+dropspeed
   # If the drop goes off the bottom of the screen, put it back at the top
   if (ydrop>height):
      ydrop=5
      # move the x to a random place from 0 (left-hand-side) 
      # to width (right-hand-side)
      xdrop=randint(0,width)

 
   # draw the drop on the picture 
   cv2.circle(img,(xdrop,ydrop), dropsize, dropcolour, -1)

   # loop through the detected faces, draw on the image and do game stuff
   for x, y, w, h in rects:
      cv2.rectangle(img, (x, y), (x+w, y+h), faceboxcolour, 2)
      if (ydrop>y) and (xdrop>x) and (xdrop<x+w) and (ydrop<y+h):
         print("it's in the face box!")
         ydrop=y #move the ball to the top of the box
         dropspeed=dropspeed*-1 #reverse the direction of the motion
         

   cv2.imshow('My Game', img)

   if 0xFF & cv2.waitKey(5) == 27:
      break





