import cv2 as cv
import numpy as np
capture=cv.VideoCapture(0)


while True:
    isTrue,frame=capture.read()
   
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    lower_white = np.array([0, 0, 200], dtype=np.uint8)#white
    upper_white = np.array([180, 50, 255], dtype=np.uint8)
    m=cv.inRange(hsv,lower_white,upper_white)
    
   
    lower_blue = np.array([100, 150, 50], dtype=np.uint8)  #blude
    upper_blue = np.array([140, 255, 255], dtype=np.uint8) 

    mask = cv.inRange(hsv, lower_blue, upper_blue) 
    result = cv.bitwise_and(frame,frame, mask=mask) 

    lower_red1 = np.array([0, 120, 70], dtype=np.uint8)
    upper_red1 = np.array([10, 255, 255], dtype=np.uint8)


    lower_red2 = np.array([170, 120, 70], dtype=np.uint8)
    upper_red2 = np.array([180, 255, 255], dtype=np.uint8)
    m2=cv.inRange(hsv,lower_red1,upper_red1)
    m3=cv.inRange(hsv,lower_red2,upper_red2)
    r2 = cv.bitwise_and(frame,frame, mask=m2+m3) 
    

    r=cv.bitwise_and(frame,frame,mask=m)
    count,_=cv.findContours(m,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
    cv.drawContours(frame,count,-1,(0,255,0),2)
    cv.imshow('video',frame)
    cv.imshow('white',r)
    
    cv.imshow("b",result)
    cv.imshow("r",r2)
 
    
    if cv.waitKey(1)& 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()