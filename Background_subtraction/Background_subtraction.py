
import cv2
import numpy as np

video = cv2.VideoCapture(0)

ok,frame1 = video.read()

frame1 = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
if ok == False:
    print("Couldn't read")
a=1
while(1):
    a=a+1
    ok,frame=video.read()
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    img = cv2.subtract(frame1,frame)
    height = img.shape[0]
    width = img.shape[1]

    #for y in range(0, height):
   #     for x in range(0, width):
   #         # threshold the pixel
   #         img[y, x] = 255 if img[y, x] > 0 else 0

    kernel = np.ones((5,5),np.float32)/25
    dst = cv2.filter2D(img,-1,kernel)
    
    
    
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(dst,'Frame =  ' + str(a),(10,500), font,2,(255,255,255),2,cv2.LINE_AA)
    cv2.imshow("Difference",dst)
    key = cv2.waitKey(1)
   # cv2.destroyAllWindows()
    if key==ord('q'):
        cv2.destroyAllWindows()
        break;

    
print(a)
video.release()
