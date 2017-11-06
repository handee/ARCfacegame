
import cv2
import video
import common
import sys
import numpy as np
from random import randint

cv2.namedWindow('facedetect')

score=0
level=0
player_lives=3

b=150
g=150
r=150
colour=(b,g,r)

balldiameter=10
bx=100
by=balldiameter/2
ballcolour=(255,100,100)
bx_direction=2
by_direction=3


#The face detector can have minimum and maximum sizes. 
mn=30 # minimum face width
mx=500 # maximum face width

#these two lines set up the face detector and the video input
cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
cam = video.create_capture(0)

fimg=cv2.imread("smily.png")

while True:
   ret, img = cam.read()

   height, width= img.shape[:2]
   #print(height,width)
#n make a blank background instead of the input image   
#   output_image=np.zeros((height,width,3),np.uint8)
#   output_image[:]=(0,0,255)
   output_image=img
   bx=bx+bx_direction
   by=by+by_direction
   if (bx>width or bx<0):
      bx_direction=-bx_direction
   if (by<0):
      by_direction=-by_direction
   if (by>height):
      by=balldiameter/2
   #n this is going off the bottom of the screen. do you want to do something
# when it's dropped? if so this is where you'll want to put the code.
      player_lives=player_lives-1
      print("you have {} lives left".format(player_lives))

   # read an image from the video camera
   # convert the image to greyscale (black and white) storing it in the 
   # variable "grey"
   grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
   
   cv2.circle(output_image, (bx,by), balldiameter, ballcolour, -1)

   # run the face detector on the grey image and store the output in 
   # the variable "rects"
   rects = cascade.detectMultiScale(grey, scaleFactor=1.3, minNeighbors=3, minSize=(mn, mn), maxSize=(mx,mx))

   # loop through and draw the detected faces on the image
   for x, y, w, h in rects:
      if ((bx > x) and (bx < x+w) and (by < y) and (by > y-balldiameter )):
         by_direction=-by_direction
         colour=(0,0,255) # make the face flash red

#n Increase the score by one
         score=score+1
	 print("your score is {}".format(score))
	 print("your level is {}".format(level))
         if (score>15):
            level=4
            by_direction=12
         elif (score>10):
            level=3
            by_direction=9
         elif (score>5):
            level=2
            by_direction=6
         else:
            level=1

      #else: 
         #n do something if you miss..?
#n draw a face instead of a rectangle?
      f2=cv2.resize(fimg,(w,h),interpolation=cv2.INTER_CUBIC)
      output_image[y:y+h,x:x+w]=f2
     # cv2.rectangle(img, (x, y), (x+w, y+h), colour, -1)
      colour=(b,g,r)

#n flip the image - make sure to do this before writing but after drawing
   output=cv2.flip(output_image,1)
 

#n Put the score on the screen
   font=cv2.FONT_HERSHEY_SIMPLEX
   score_print ="Score: {}".format(score)
   cv2.putText(output,score_print,(10,40), font, 1,(255,255,255),4,cv2.LINE_AA)
   lives_print ="Lives: {}".format(player_lives)
   cv2.putText(output,lives_print,(10,80), font, 1,(255,255,255),2,cv2.LINE_AA)



   cv2.imshow('facedetect', output)


   if 0xFF & cv2.waitKey(5) == 27:
      break
   if (player_lives<0):
      print("You lose!")
      break





