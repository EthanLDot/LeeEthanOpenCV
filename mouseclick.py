import cv2

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        strXY = str(x) + ", " + str(y)
        #print(strXY)
        cv2.putText(img, strXY, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)
        cv2.imshow('image', img)
    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        strBGR = str(blue) + ", " + str(green)  + ", " + str(red)
        cv2.putText(img, strBGR, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow('image', img)


#img = np.zeros((512, 512, 3), np.uint8)
img = cv2.imread("lena.jpg")
cv2.imshow('image', img)

cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()