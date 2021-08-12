#Imort OpenCV
import cv2
import numpy as np
 
cap = cv2.VideoCapture(1)
 
while(1):
    #Ambil frame
    _,frame = cap.read()
    #Konversi RGB ke HSV
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    #nilai biru pada HSV
    lower_blue = np.array([20,0,0])
    upper_blue = np.array([40,255,255])
    #Threshold gambar hsv untuk hanya mendapatkan nilai biru saja
    mask = cv2.inRange(hsv,lower_blue,upper_blue)
    #dibitwise
    res = cv2.bitwise_and(frame,frame,mask=mask)
 
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
 
    if cv2.waitKey(1)==27:
        break
 
cv2.destroyAllWindows()
