import cv2

cap = cv2.VideoCapture(0)

while True:

    ret,frame = cap.read()
    cv2.imshow("video",frame)
    
    if keys.keys =="q":
       cv2.waitkey()

