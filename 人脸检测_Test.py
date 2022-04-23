import cv2
def cv_show(name,img):
    cv2.imshow(name,img)
    cv2.waitKey(10)
    cv2.destroyAllWindows()
    #cv2.waitKey(0)
def face_detect_demo(img):
    gary = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face_detect = cv2.CascadeClassifier('opencv-4.5.5/data/haarcascades/haarcascade_frontalface_alt2.xml')
    face = face_detect.detectMultiScale(gary,1.1)
    for x,y,w,h in face:
        cv2.rectangle(img,(x,y),(x+w,y+h),color=(0,0,255),thickness=2)
    #cv2.imshow('pic',img)
    cv_show('123',img)
#人脸识别
img=cv2.imread('')
cap = cv2.VideoCapture(0)
while True:
    flag,frame = cap.read()
    if flag==False:
        break
    face_detect_demo(frame)
cv2.destroyAllWindows()
cap.release()
#face_detect_demo(img)
