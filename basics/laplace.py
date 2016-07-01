import cv2
import cv
import numpy as np
from matplotlib import pyplot as plt

# Camera 0 is the integrated web cam on my netbook
camera_port = 0

# Number of frames to throw away while the camera adjusts to light levels
ramp_frames = 30

# Now we can initialize the camera capture object with the cv2.VideoCapture class.
# All it needs is the index to a camera port.
camera = cv2.VideoCapture(camera_port)


# Captures a single image from the camera and returns it in PIL format
def get_image():
    # read is the easiest way to get a full image out of a VideoCapture object.
    retval, im = camera.read()
    return im


# Ramp the camera - these frames will be discarded and are only used to allow v4l2
# to adjust light levels, if necessary
for i in xrange(ramp_frames):
    temp = get_image()
print("Taking image...")
# Take the actual image we want to keep
camera_capture = get_image()
file = "img/test_image.png"
# A nice feature of the imwrite method is that it will automatically choose the
# correct format based on the file extension you provide. Convenient!
cv2.imwrite(file, camera_capture)
cv2.rectangle(camera_capture, (384, 0), (510, 128), (0, 255, 0), 3)
img = cv2.imread('img/test_image.png', 0)
edges = cv2.Canny(img, 100, 200)

# plt.subplot(121),plt.imshow(img,cmap = 'gray')
# plt.title('Original Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(edges,cmap = 'gray')
# plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()
# cv2.imshow('home/akila/Desktop/test_image.png',camera_capture)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
plt.imshow(camera_capture, cmap='gray', interpolation='bicubic')

plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()
print camera_capture
# You'll want to release the camera, otherwise you won't be able to create a new
# capture object until your script exits
del (camera)

# im=cv.LoadImage('img/test_image.jpg', cv.CV_LOAD_IMAGE_COLOR)
#
# # Laplace on a gray scale picture
# gray = cv.CreateImage(cv.GetSize(im), 8, 1)
# cv.CvtColor(im, gray, cv.CV_BGR2GRAY)
#
# aperture=3
#
# dst = cv.CreateImage(cv.GetSize(gray), cv.IPL_DEPTH_32F, 1)
# cv.Laplace(gray, dst,aperture)
#
# cv.Convert(dst,gray)
#
# thresholded = cv.CloneImage(im)
# cv.Threshold(im, thresholded, 50, 255, cv.CV_THRESH_BINARY_INV)
#
# cv.ShowImage('Laplaced grayscale',gray)
# #------------------------------------
#
# # Laplace on color
# planes = [cv.CreateImage(cv.GetSize(im), 8, 1) for i in range(3)]
# laplace = cv.CreateImage(cv.GetSize(im), cv.IPL_DEPTH_16S, 1)
# colorlaplace = cv.CreateImage(cv.GetSize(im), 8, 3)
#
# cv.Split(im, planes[0], planes[1], planes[2], None) #Split channels to apply laplace on each
# for plane in planes:
#     cv.Laplace(plane, laplace, 3)
#     cv.ConvertScaleAbs(laplace, plane, 1, 0)
#
# cv.Merge(planes[0], planes[1], planes[2], None, colorlaplace)
#
# cv.ShowImage('Laplace Color', colorlaplace)
# #-------------------------------------
#
# cv.WaitKey(0)
