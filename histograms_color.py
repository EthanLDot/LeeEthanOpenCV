import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('lena.jpg', 1)
b, g, r = cv.split(img)

cv.imshow("img", img)
cv.imshow("b", b)
cv.imshow("g", g)
cv.imshow("r", r)

plt.hist(b.ravel(), 256, [0,256])
plt.hist(g.ravel(), 256, [0,256])
plt.hist(r.ravel(), 256, [0,256])
plt.xlabel("intensity")
plt.ylabel("# pixels")
plt.show()
cv.waitKey(0)
cv.destroyAllWindows()