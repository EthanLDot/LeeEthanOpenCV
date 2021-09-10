import numpy as np
import cv2

img = cv2.imread("lena.jpg", 1)
#img = np.zeros([512, 512, 3], np.uint8)

img = cv2.line(img, (0,0), (255, 255), (255, 0, 0), 10)
img = cv2.arrowedLine(img, (0,255), (255, 255), (2, 30, 155), 10)
img = cv2.rectangle(img, (384, 0), (510, 128), (0, 0, 255), 1)
img = cv2.rectangle(img, (384, 0), (404, 328), (69, 59, 10), -1)
img = cv2.circle(img, (255, 255), 63, (0, 255, 255), -1)
img = cv2.putText(img, "OpenCV",
                  (10, 500), cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 255, 255), 10, cv2.LINE_AA)

cv2.imshow('hello', img)
k = cv2.waitKey(0)

if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('lena_copy.png', img)
    cv2.destroyAllWindows()