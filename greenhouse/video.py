# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import sys
sys.path.append('/home/pi/opencv/data/haarcascades')


sys.path.append('/usr/local/lib/python2.7/site-packages')
import cv2

import numpy as np
from matplotlib import pyplot as plt	
def nothing(x):
    pass


         
# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))
 
# allow the camera to warmup
time.sleep(0.1)
 
# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	# grab the raw NumPy array representing the image, then initialize the timestamp
	# and occupied/unoccupied text
	image = frame.array
 
	# show the frame
	cv2.imshow("Frame", image)
	key = cv2.waitKey(1) & 0xFF
 	cv2.imwrite('hello.jpg', image)
 	
 	
 	img = cv2.imread('hello.jpg')
 	


 	cv2.rectangle(img,(384,200),(510,128),(0,255,0),3)
   
 	
	# clear the stream in preparation for the next frame
	rawCapture.truncate(0)
	

	
		# create trackbars for color change
	cv2.createTrackbar('th1','image',0,255,nothing)
	cv2.createTrackbar('th2','image',0,255,nothing)
	cv2.namedWindow('image')
	
   	# get current positions of four trackbars
  	th1 = cv2.getTrackbarPos('th1','image')
  	th2 = cv2.getTrackbarPos('th2','image')
   	 #apply canny 
   	edges = cv2.Canny(from cv2 import *
from cv import *
import numpy as np
from matplotlib import pyplot as plt

# initialize the camera
cam = VideoCapture(1)   # 0 -> index of camera
s, img = cam.read()
if s:    # frame captured without any errors
    namedWindow("cam-test",CV_WINDOW_AUTOSIZE)
    imshow("cam-test",img)
    waitKey(0)
    destroyWindow("cam-test")
    imwrite("filename.jpg",img) #save image

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
    waitKey(0),th1,th2)
    	 #show the image
       	cv2.imshow('image',edges)
    
	cv2.imshow('img',img)
	
 
	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break

