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
camera.framerate = 4
rawCapture = PiRGBArray(camera, size=(640, 480))
 
# allow the camera to warmup
time.sleep(0.1)
 
# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	# grab the raw NumPy array representing the image, then initialize the timestamp
	# and occupied/unoccupied text
	image = frame.array
 
 
	# show the frame
	#cv2.imshow("Frame", image)
	key = cv2.waitKey(1) & 0xFF
 	cv2.imwrite('hello.jpg', image)
 	
 	
 	
 	img = cv2.imread('hello.jpg')
 	face_cascade = cv2.CascadeClassifier('/home/pi/image_processing/leaning/haarcascade_frontalface_default.xml')

	faces = face_cascade.detectMultiScale(img, 1.1, 5)

	print "Found "+str(len(faces))+" face(s)"

	if len(faces) > 0:
	    print 'Face detected'
	
	
	#Draw a rectangle around every found face
	for (x,y,w,h) in faces:
	    cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)

 	cv2.rectangle(img,(384,200),(510,128),(0,255,0),3)
   
 	
	# clear the stream in preparation for the next frame
	rawCapture.truncate(0)
	

	
		# create trackbars for color change
	cv2.createTrackbar('th1','image',0,255,nothing)
	cv2.createTrackbar('th2','image',0,255,nothing)
	#cv2.namedWindow('image')
	
   	# get current positions of four trackbars
  	th1 = cv2.getTrackbarPos('th1','image')
  	th2 = cv2.getTrackbarPos('th2','image')
   	 #apply canny 
   	edges = cv2.Canny(img,th1,th2)
    	 #show the image
       	cv2.imshow(' Edge Ditection ',edges)
  


	
	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break
