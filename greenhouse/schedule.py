#!/usr/bin/python

import thread
import time
from cv2 import *
from cv import *
import numpy as np
from matplotlib import pyplot as plt

# Define a function for the thread


def print_time( threadName, delay):
   count = 0
   while count < 5:
      time.sleep(delay)
      count += 1
      print "%s: %s" % ( threadName, time.ctime(time.time()) )

   # initialize the camera
   cam = VideoCapture(0)  # 0 -> index of camera
   s, img = cam.read()

   if s:  # frame captured without any errors
       namedWindow("cam-test", CV_WINDOW_AUTOSIZE)
       imshow("cam-test", img)
       # waitKey(0)
       destroyWindow("cam-test")
       imwrite("filename.jpg", img)  # save image

       # read image into matrix.
       m = imread("filename.jpg")
       image = cv.LoadImage('filename.jpg', cv.CV_LOAD_IMAGE_GRAYSCALE)

       # Get edges
       morphed = cv.CloneImage(image)
       cv.MorphologyEx(image, morphed, None, None, cv.CV_MOP_GRADIENT)  # Apply a dilate - Erode

       cv.Threshold(morphed, morphed, 30, 255, cv.CV_THRESH_BINARY_INV)

       cv.ShowImage("Image", image)
       cv.ShowImage("Morphed", morphed)

       # get image properties.
       h, w, bpp = np.shape(m)

       # iterate over the entire image.
       # for py in range(0, h):
       #     for px in range(0, w):
       #         print m[py][px]

       # display image
       imshow('matrix', m)
       imwrite('filename.png', m)
       waitKey(0)

# Create two threads as follows
try:
   thread.start_new_thread( print_time, ("Thread-1", 2, ) )
   thread.start_new_thread( print_time, ("Thread-2", 4, ) )
except:
   print "Error: unable to start thread"

while 1:
   pass