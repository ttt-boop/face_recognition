import cv2
import numpy as np
import os

#加载训练数据集文件
recogizer=cv2.face.LBPHFaceRecognizer_create()
recogizer.read('trainer.yml')
names=[]

#准备识别的图片
def face_detect_demo(img):
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#转换为灰度
    face_detector=cv2.CascadeClassifier('opencv-4.5.5/data/haarcascades/haarcascade_frontalface_alt.xml')
    face=face_detector.detectMultiScale(gray,1.1,5,cv2.CASCADE_SCALE_IMAGE,(100,100),(500,500))
    #face=face_detector.detectMultiScale(gray)
    for x,y,w,h in face:
        cv2.rectangle(img,(x,y),(x+w,y+h),color=(0,0,255),thickness=2)
        cv2.circle(img,center=(x+w//2,y+h//2),radius=w//2,color=(0,255,0),thickness=1)
        # 人脸识别
        ids, confidence = recogizer.predict(gray[y:y + h, x:x + w])
        #print('标签id:',ids,'置信评分：', confidence)
        if confidence > 80:
            cv2.putText(img, 'unkonw', (x + 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 1)
            confidence = "  {0}%".format(round(100 - confidence))
            cv2.putText(img, str(confidence), (x - 10, y + 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 1)
        else:
            confidence = "  {0}%".format(round(100 - confidence))
            cv2.putText(img, str(confidence), (x - 10, y + 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 1)
            cv2.putText(img,str(names[ids-1]), (x + 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 1)
    cv2.imshow('result',img)


def name():
    path = 'image'
    filenames = os.listdir(path)
    filenames.sort(key=lambda x:int(x[:-7])) #倒着数第7位'.'为分界线，按照‘.'左边的数字从小到大排序
    for f in filenames:
        print(f)
    imagePaths=[os.path.join(path,f) for f in filenames]
    names_ = ["lena","black","laowang"]
    for imagePath in imagePaths:
       id = str(os.path.split(imagePath)[1].split('.',2)[0])
       names.append(names_[int(id)-1])

cap=cv2.VideoCapture('1.mp4')
name()
while True:
    flag, frame = cap.read()
    if not flag:
        break
    face_detect_demo(frame)
    if ord(' ') == cv2.waitKey(20):
        break
cv2.destroyAllWindows()
cap.release()
