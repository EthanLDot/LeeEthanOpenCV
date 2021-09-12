import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('saltpepper.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

kernel = np.ones((5, 5), np.float32)/25 #matrix of 25 ones, we do 5 * 5

#homogenous filter
dst = cv2.filter2D(img, -1, kernel)
blur = cv2.blur(img, (5, 5)) #looks almost same as dst

gblur = cv2.GaussianBlur(img, (5, 5), 0) #slightly better quality, less noise

medianblur = cv2.medianBlur(img, 5) #5 is kernel size, good for salt/pepper noise
#median blur: good for salt/pepper noise

bifilter = cv2.bilateralFilter(img, 9, 75, 75)

titles = ['image', '2D Convolution', 'blur', 'Gaussian Blur', 'Median', 'bi']
images = [img, dst, blur, gblur, medianblur, bifilter]

for i in range(6):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()