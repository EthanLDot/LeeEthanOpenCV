import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('messi5.jpg', cv2.IMREAD_GRAYSCALE)
#img = cv2.imread('sudoku.png', cv2.IMREAD_GRAYSCALE)
lap = cv2.Laplacian(img, cv2.CV_64F, ksize=3)
lap = np.uint8(np.absolute(lap)) #convert back to unsigned 8 bit, using absolute value of existing lap
sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0) #1 and 0 are dx and dy vals
sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1)
sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))
canny = cv2.Canny(img, 100, 200)

sobelXY = cv2.bitwise_or(sobelX, sobelY)

titles = ['image', 'Laplacian', 'sobel X', 'sobel Y', 'sobel combined', 'canny']
images = [img, lap, sobelX, sobelY, sobelXY, canny]
for i in range(len(images)):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()