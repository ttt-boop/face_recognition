import cv2
cap = cv2.VideoCapture('1.mp4')
num=1
while (cap.isOpened()):
    ret_flag,Vshow=cap.read()
    if ret_flag == False:
        break
    cv2.imshow('pic',Vshow)
    k=cv2.waitKey(20)
    if k==ord('s'):
        cv2.imwrite('image/'+str(num)+'.ch'+'.tif',Vshow)
        num+=1
        print('success!')
    elif k==ord('q'):
        break
cv2.destroyAllWindows()
cap.release()