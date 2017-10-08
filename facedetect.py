
import cv2
import video
import common
import sys
import numpy as np
from random import randint

b=50
g=50
r=200
colour=(b,g,r)

#The face detector can have minimum and maximum sizes. 
mn=30 # minimum face width
mx=500 # maximum face width

#these two lines set up the face detector and the video input
cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
cam = video.create_capture(0)

while True:
   # read an image from the video camera
   ret, img = cam.read()
   
   # convert the image to greyscale (black and white) storing it in the 
   # variable "grey"
   grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
   
   # run the face detector on the grey image and store the output in 
   # the variable "rects"
   rects = cascade.detectMultiScale(grey, scaleFactor=1.3, minNeighbors=3, minSize=(mn, mn), maxSize=(mx,mx))

   # loop through and draw the detected faces on the image
   for x, y, w, h in rects:
      cv2.rectangle(img, (x, y), (x+w, y+h), colour, 2)

   cv2.imshow('facedetect', img)

   if 0xFF & cv2.waitKey(5) == 27:
      break


cv2.destroyAllWindows()


