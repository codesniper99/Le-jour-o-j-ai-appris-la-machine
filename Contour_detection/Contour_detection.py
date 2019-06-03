
import cv2

img = cv2.imread("lena.jpg",1)


gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Lenna",gray)


cv2.waitKey(0)
ret, thresh = cv2.threshold(gray, 127, 255, 0)
contours,hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(gray, contours,-1,(0,255,255),2)
cv2.imshow("Lenna",gray)
cv2.waitKey(0)

