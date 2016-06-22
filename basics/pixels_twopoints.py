import cv2.cv as cv

import random

im = cv.LoadImage("img/lena2.jpg") #or LoadImage and access pixel with Get2D/Set2D

for k in range(10000): #Create 5000 noisy pixels
    i = random.randint(0,im.height-1)
    j = random.randint(0,im.width-1)
    color = (random.randrange(256),random.randrange(256),random.randrange(256))
    im[i,j] = color

cv.ShowImage("Noize", im)
cv.WaitKey(0)

