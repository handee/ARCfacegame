
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

px=5
py=5
ballcolour=(255,100,100)
px_direction=4
py_direction=4


#The face detector can have minimum and maximum sizes. 
mn=30 # minimum face width
mx=500 # maximum face width

#these two lines set up the face detector and the video input
cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
cam = video.create_capture(0)


while True:
   ret, img = cam.read()

   height, width= img.shape[:2]

   px=px+px_direction
   py=py+py_direction
   if (px>width or px<0):
      px_direction=-px_direction
   if (py>height or py<0):
      py_direction=-py_direction
   # read an image from the video camera
   # convert the image to greyscale (black and white) storing it in the 
   # variable "grey"
   grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
   
   # run the face detector on the grey image and store the output in 
   # the variable "rects"
   rects = cascade.detectMultiScale(grey, scaleFactor=1.3, minNeighbors=3, minSize=(mn, mn), maxSize=(mx,mx))

   # loop through and draw the detected faces on the image
   for x, y, w, h in rects:
      if ((px > x) and (px < x+w) and (py > y) and (py < y+h)):
         colour=(0,0,255) # make the face flash red
         print("Ouch!")
      else:
         print("Safe")
      cv2.rectangle(img, (x, y), (x+w, y+h), colour, -1)
      colour=(b,g,r)
   if (len(rects)==0):
      print("You're hiding, naughty") 

   cv2.circle(img, (px,py), 10, ballcolour, -1)
   cv2.imshow('facedetect', img)


   if 0xFF & cv2.waitKey(5) == 27:
      break





