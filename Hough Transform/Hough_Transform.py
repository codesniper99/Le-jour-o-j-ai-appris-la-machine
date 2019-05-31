import cv2
import numpy as np

img = cv2.imread('C:/Users/Akhil/Desktop/Le-jour-o-j-ai-appris-la-machine/Hough Transform/lena.jpg') # road.png is the filename
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


edges = cv2.Canny(gray,50,150,apertureSize = 3)
minLineLength = 100
maxLineGap = 1
lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength,maxLineGap)
for r in lines:
    for x1,y1,x2,y2 in r:
        cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)

cv2.imwrite('lenaedge.jpg',img)

img = cv2.imread('C:/Users/Akhil/Desktop/Le-jour-o-j-ai-appris-la-machine/Hough Transform/lenaedge.jpg') # road.png is the filename
cv2.imshow("ok",img)
cv2.waitKey(0)
