import cv2.cv as cv

im = cv.LoadImage("img/lena2.jpg",3)

cv.SetImageROI(im, (400,200,250,150)) #Give the rectangle coordinate of the selected area

cv.Zero(im)
#cv.Set(im, cv.RGB(100, 100, 100)) put the image to a given value

cv.ResetImageROI(im) # Reset the ROI

cv.ShowImage("Image",im)

cv.WaitKey(0)

