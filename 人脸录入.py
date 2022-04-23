import cv2
cap = cv2.VideoCapture('1.mp4')
num=1
while (cap.isOpened()):
    ret_flag,Vshow=cap.read()
    if ret_flag == False:
        break
    cv2.imshow('pic',Vshow)
    k=cv2.waitKey(20)
    #按下s键截屏 tif文件写入当前目录下的image文件夹中（在当前目录下新建一个image文件夹）
    if k==ord('s'):
        cv2.imwrite('image/'+str(num)+'.ch'+'.tif',Vshow)
        num+=1
        print('success!')
    elif k==ord('q'):
        break
cv2.destroyAllWindows()
cap.release()
