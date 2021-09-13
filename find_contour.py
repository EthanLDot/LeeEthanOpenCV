import numpy as np
import cv2

img = cv2.imread('opencv-logo.png')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 20, 255, 0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
#contours is a python list of all contours, each contour is a numpy array of coordinates
#hierarchy is the optional output vector

print("Number of contours = " + str(len(contours)))
print(contours[0])
cv2.drawContours(img, contours, -1, (0, 255, 0), 3) #change to -1 for all contours

cv2.imshow('Image', img)
cv2.imshow('Image GRAY', imgray)
#cv2.imshow('t', thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()