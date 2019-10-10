import cv2
import tkinter as tk
from tkinter import filedialog#文件控件
import time
from PIL import Image, ImageTk#图像控件
import threading#多线程

#---------------创建窗口
window = tk.Tk()
window.title('shexiangtou')
sw = window.winfo_screenwidth()#获取屏幕宽
sh = window.winfo_screenheight()#获取屏幕高
wx = 600
wh = 800
window.geometry("%dx%d+%d+%d" %(wx,wh,(sw-wx)/2,(sh-wh)/2-100))#窗口至指定位置
canvas = tk.Canvas(window,bg='#c4c2c2',height=wh,width=wx)#绘制画布
canvas.pack()

#create a list of thread
ts = []
rgbImage = 0
num = 0


def video_demo():
    def cc():
        global rgbImage
        imageName = 'DontCare.jpg' #Just a random string
        cap = cv2.VideoCapture(0)
        while(True):
            ret, frame = cap.read()
            frame = cv2.flip(frame, 1)
            rgbImage = frame

            cv2.imshow('inshow',rgbImage)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                imageName = str(time.strftime("%Y_%m_%d_%H_%M")) + '.jpg'
                cv2.imwrite(imageName, rgbImage)
                break
        cap.release()
        cv2.destroyAllWindows()
        return imageName

    t=threading.Thread(target=cc)
    t.do_run = True
    t.start()
    t.join()

def get_image():
    global num
    window.title(str(num))
    num = num + 1


bt_start = tk.Button(window, text='打开摄像头', height=2, width=15, command=video_demo)
bt_start.place(x=130, y=600)

bt_stop = tk.Button(window, text='分析', height=2, width=15, command=get_image)
bt_stop.place(x=330, y=600)

window.mainloop()
