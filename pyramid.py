import cv2

img = cv2.imread("lena.jpg")

lr = cv2.pyrDown(img)
llr = cv2.pyrDown(lr)
hr = cv2.pyrUp(llr)

cv2.imshow("Original image ", img)
cv2.imshow("low res", lr)
cv2.imshow("lower res", llr)
cv2.imshow("pyrUp", hr)
cv2.waitKey(0)
cv2.destroyAllWindows()