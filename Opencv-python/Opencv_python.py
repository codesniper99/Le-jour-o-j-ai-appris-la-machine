import cv2
img = cv2.imread("C:/Users/Akhil/Desktop/opencv/OpenCV/lena.jpg",1)
print(img.shape)


cv2.imshow("Lenna",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

resized =cv2.resize(img,(300,300))

#resized =cv2.resize(img,(int(img.shape[0]/2),int(img.shape[1]/2)))

cv2.imshow("Lenna2",resized)
cv2.waitKey(0)
cv2.destroyAllWindows()

#face classifier
face_cascade = cv2.CascadeClassifier('C:/Users/Akhil/Documents/opencv/sources/data/haarcascades/haarcascade_frontalface_default.xml')
print(str(face_cascade))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('GREYSCALE',gray)
cv2.waitKey(0) 


cv2.destroyAllWindows()
faces = face_cascade.detectMultiScale(gray, 1.01, 5)

for (x,y,w,h) in faces:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
    
print(x,y,w,h)
cv2.imshow('FACE DETECTION',img)
cv2.waitKey(0)
cv2.destroyAllWindows()