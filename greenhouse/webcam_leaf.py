from cv2 import *
from cv import *
import numpy as np
from matplotlib import pyplot as plt

# initialize the camera
cam = VideoCapture(0)   # 0 -> index of camera
s, img = cam.read()

if s:    # frame captured without any errors
    namedWindow("cam-test",CV_WINDOW_AUTOSIZE)
    imshow("cam-test",img)
    #waitKey(0)
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
    waitKey(0)