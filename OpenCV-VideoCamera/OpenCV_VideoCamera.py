
import cv2,time

#1. BASIC VIDEO FRAME
video = cv2.VideoCapture(0)
print(video)

check, frame = video.read()
print(check)
#print(frame)
#time.sleep(3)
#first frame 
cv2.imshow("FIRST FRAME",frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
video.release()

#video total frame

#2. STREAMING VIDEO FRAME GREY AND COLOR

a=1;

video = cv2.VideoCapture(0)
while True:
    a=a+1;
    check,frame=video.read()
    print(frame)
    #color
    face_cascade = cv2.CascadeClassifier('C:/Users/Akhil/Documents/opencv/sources/data/haarcascades/haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.01, 5)

    for (x,y,w,h) in faces:
      frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
    
    print(x,y,w,h)
    cv2.imshow("COLOR FRAME",frame)
    #grey
    color = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("GRAY FRAME",color)
    #blur
    color = cv2.GaussianBlur(color,(21,21),0)
    cv2.imshow("GAUSSIAN BLUR FRAME",color)

    key = cv2.waitKey(1)
   # cv2.destroyAllWindows()
    if key==ord('q'):
        cv2.destroyAllWindows()
        break;

print(a)
video.release()

#3.



