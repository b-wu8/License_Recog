import cv2
from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
import threading
import time

# Here, we are creating our class, Window, and inheriting from the Frame
# class. Frame is a class from the tkinter module. (see Lib/tkinter/__init__)
class Window(Frame):
    ts = []
    rgbImage = 0
    num = 0
    # Define settings upon initialization. Here you can specify
    def __init__(self, master=None):

        # parameters that you want to send through the Frame class.
        Frame.__init__(self, master)

        #reference to the master widget, which is the tk window
        self.master = master

        #with that, we want to then run init_window, which doesn't yet exist
        self.init_window()
    def init_window(self):

        # changing the title of our master widget
        self.master.title("Licence_Recog")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        # creating a menu instance
        menu = Menu(self.master)
        self.master.config(menu=menu)
        image = Menu(menu)
        image.add_command(label = "Image", command = self.showImg)
        menu.add_cascade(label = "Input", menu = image)
        # video = Menu(menu)
        image.add_command(label = "Screenshot",  command = self.video_demo)
        # menu.add_cascade(label = "video", menu = image)
        database = Menu(menu)
        database.add_command(label="Interface", command = self.database)
        menu.add_cascade(label="Database", menu=database)



        '''
        # create the file object)
        file = Menu(menu)

        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit
        file.add_command(label="Exit", command=self.client_exit)

        #added "file" to our menu
        menu.add_cascade(label="File", menu=file)


        # create the file object)
        edit = Menu(menu)

        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit
        edit.add_command(label="Show Img", command=self.showImg)
        edit.add_command(label="Show Text", command=self.showText)

        #added "file" to our menu
        menu.add_cascade(label="Edit", menu=edit)
        '''
    def database(self):
        window = Tk()
        window.title("Admin Login Page")
        window.resizable(0,0)
        window.geometry("400x400")
        user = Label(window, text="User ID")
        input1 = Entry(window)
        password = Label(window, text="Password")
        input2 = Entry(window)
        Label(window, text="Welcome!").grid(row=0, column=0)
        user.grid(row=1, column=0)
        input1.grid(row=1, column=1)
        password.grid(row=2, column=0)
        input2.grid(row=2, column=1)
        print(111)
        Button(window, text="Sign in", command=self.log(input1,input2)).grid(row=3,column=0,sticky=W,pady=4)

        window.mainloop()

    def log(self, input1, input2):
        a = input1.get()
        b = input2.get()
        print(a,b)


    def showImg(self):
        name = askopenfilename(
                           filetypes =(("Graph File", "*.jpg"),("All Files","*.*")),
                           title = "Choose a file."
                           )
        load = Image.open(name)
        render = ImageTk.PhotoImage(load)

        # labels can be text or images
        img = Label(self, image=render)
        img.image = render
        img.config(width=root.winfo_screenwidth()-840,height=root.winfo_screenheight())
        img.place(x=0, y=0)

        label0 = Label(self, text="Plate Number:")
        label0.place(x=1080,y=100)
        label1 = Label(self, text="Confidence:")
        label1.place(x=1080,y=200)
        label2 = Label(self, text="State:")
        label2.place(x=1080,y=300)

        # temporary recognition result
        # will use actual prediction to display
        prediction = Label(self, text=str(name.split("/")[-1].split(".")[0]))
        prediction.place(x=1080, y=150)
        confidence = Label(self, text="100")
        confidence.place(x=1080, y=250)
        state = Label(self, text="New York (Yellow)")
        state.place(x=1080, y=350)

    def video_demo(self):
        def cc():
            global rgbImage
            cap = cv2.VideoCapture(0)
            imageName = ""
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

    def get_image(self):
        global num
        self.title(str(num))
        num = num + 1

    def showText(self):
        text = Label(self, text="Hey there good lookin!")
        text.pack()


    def client_exit(self):
        exit()




# root window created. Here, that would be the only window, but
# you can later have windows within windows.
root = Tk()
root.title("Licence_Recog")
root.geometry("800x600")

#creation of an instance
app = Window(root)


#mainloop
root.geometry(str(root.winfo_screenwidth())+"x"+str(root.winfo_screenheight()))
root.mainloop()
