
import cv2
import video
import common
import sys
import numpy as np
from random import randint

cv2.namedWindow('facedetect')


b=150
g=150
r=150
colour=(b,g,r)

balldiameter=10
bx=100
by=balldiameter/2
ballcolour=(255,100,100)
bx_direction=2
by_direction=8


#The face detector can have minimum and maximum sizes. 
mn=30 # minimum face width
mx=500 # maximum face width

#these two lines set up the face detector and the video input
cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
cam = video.create_capture(0)


while True:
   ret, img = cam.read()

   height, width= img.shape[:2]

   bx=bx+bx_direction
   by=by+by_direction
   if (bx>width or bx<0):
      bx_direction=-bx_direction
   if (by<0):
      by_direction=-by_direction
   if (by>height):
      by=balldiameter/2
   # read an image from the video camera
   # convert the image to greyscale (black and white) storing it in the 
   # variable "grey"
   grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
   
   # run the face detector on the grey image and store the output in 
   # the variable "rects"
   rects = cascade.detectMultiScale(grey, scaleFactor=1.3, minNeighbors=3, minSize=(mn, mn), maxSize=(mx,mx))

   # loop through and draw the detected faces on the image
   for x, y, w, h in rects:
      if ((bx > x) and (bx < x+w) and (by < y) and (by > y-balldiameter )):
         by_direction=-by_direction
         colour=(0,0,255) # make the face flash red
         print("Ouch!")
      else:
         print("Safe")
      cv2.rectangle(img, (x, y), (x+w, y+h), colour, -1)
      colour=(b,g,r)
   if (len(rects)==0):
      print("You're hiding, naughty") 

   cv2.circle(img, (bx,by), balldiameter, ballcolour, -1)
   cv2.imshow('facedetect', img)


   if 0xFF & cv2.waitKey(5) == 27:
      break





