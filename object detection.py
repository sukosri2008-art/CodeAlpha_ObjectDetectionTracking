
import cv2
import imutils #resize 
cam=cv2.VideoCapture(0)
f=None
while True:
    _, img = cam.read()
    img=imutils.resize(img,width=1000)
    g=cv2.GaussianBlur(cv2.cvtColor(img,cv2.COLOR_BGR2GRAY),(23,23),0)
    if f is None:
        f=g
        continue
    d=cv2.absdiff(f,g)
    t=cv2.threshold(d,25,255,cv2.THRESH_BINARY)[1]
    di=cv2.dilate(t,None,iterations=2)
    c=imutils.grab_contours(
        cv2.findContours(
            di.copy(),
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE))
    for i in c:
     if cv2.contourArea(i) > 500:
        x,y,w,h=cv2.boundingRect(i)
        cv2.rectangle(img,
                      (x,y),
                      (x+w,y+h),
                      (255,24,56),
                      2)
        cv2.imshow("MOTION DETECTION",img)
    if cv2.waitKey(20) == ord('a'):
      break
cam.release()
cv2.destroyAllWindows()
        
