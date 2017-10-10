
import cv2
import video
import common
import sys
import numpy as np
from random import randint

cv2.namedWindow('cameraview')

cam = video.create_capture(0)

while True:
   # read an image from the video camera
   ret, img = cam.read()
  
   # put that image in the window 
   cv2.imshow('cameraview', img)

   if 0xFF & cv2.waitKey(5) == 27:
      break





