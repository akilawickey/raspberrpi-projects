import cv2.cv as cv

im = cv.LoadImage("img/lena2.jpg", cv.CV_LOAD_IMAGE_GRAYSCALE)
thresholded = cv.CreateImage(cv.GetSize(im), 8, 1)

def onChange(val):
    cv.Threshold(im, thresholded, val, 255, cv.CV_THRESH_BINARY)
    cv.ShowImage("Image", thresholded)

onChange(100) #Call here otherwise at startup. Show nothing until we move the trackbar
cv.CreateTrackbar("Thresh", "Image", 100, 255, onChange) #Threshold value arbitrarily set to 100

cv.WaitKey(0)

