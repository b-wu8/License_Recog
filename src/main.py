import cv2
from tkinter import *
#import tkinter as tk
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
import threading
import time
from database import Database

LARGE_FONT= ("Verdana", 12)

class SeaofBTCapp(Tk):

    def __init__(self, *args, **kwargs):

        Tk.__init__(self, *args, **kwargs)
        self.winfo_toplevel().title("Search page")
        container = Frame(self,width=400,height=100)
        container.pack(side="top", fill="both", expand = True)# geometry = "400x400"

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (Searchpage,OwnerSearch,PlateSearch):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Searchpage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


class Searchpage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self,parent)
        button = Button(self, text="owner name",
                            command=lambda: controller.show_frame(OwnerSearch))
        button.pack()

        button2 = Button(self, text="plate number",
                            command=lambda: controller.show_frame(PlateSearch))
        button2.pack()



class OwnerSearch(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self,parent)
       # window.title("owner search page")
        #Label(window, text = "owner").grid(row = 0) # this is placed in 0 0
        # 'Entry' is used to display the input-field
        label = Label(self, text="Owner Search", font=LARGE_FONT)#, font=LARGE_FONT
        label.pack(pady=10,padx=10)
        input = Entry(self)
        input.pack()
        button = Button(self, text="back",
                            command=lambda: controller.show_frame(Searchpage))
        button.grid_rowconfigure(0, weight=1)
        button.grid_columnconfigure(0, weight=1)
        button.pack(side=LEFT)
        button = Button(self, text="search")#.grid(row=3,column=0,sticky=W,pady=4)
        button.grid_rowconfigure(0, weight=1)
        button.grid_columnconfigure(1, weight=1)
        button.pack()
        self.owner = input


class PlateSearch(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self,parent)
       # window.title("owner search page")
        #Label(window, text = "owner").grid(row = 0) # this is placed in 0 0
        # 'Entry' is used to display the input-field
        label = Label(self, text="Plate Search", font=LARGE_FONT)#
        label.pack(pady=10,padx=10)
        input = Entry(self)
        input.pack()
        button = Button(self, text="back",
                            command=lambda: controller.show_frame(Searchpage))
        button.grid_rowconfigure(0, weight=1)
        button.grid_columnconfigure(0, weight=1)
        button.pack(side=LEFT)
        button = Button(self, text="search")#.grid(row=3,column=0,sticky=W,pady=4)
        button.grid_rowconfigure(0, weight=1)
        button.grid_columnconfigure(1, weight=1)
        button.pack()
        self.plate = input

# Here, we are creating our class, Window, and inheriting from the Frame
# class. Frame is a class from the tkinter module. (see Lib/tkinter/__init__)
class Window(Frame):
    ts = []
    rgbImage = 0
    num = 0
    loginwindow = None
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
        database.add_command(label="Search", command = self.search_page)
        menu.add_cascade(label="Database", menu=database)

    def search_page(self):
        app = SeaofBTCapp()
        app.mainloop()


    def database(self):
        window = Tk()
        window.title("Admin Login Page")
        window.resizable(0,0)
        window.geometry("400x400")
        user = Label(window, text="User ID")
        input1 = Entry(window)
        password = Label(window, text="Password")
        input2 = Entry(window, show="*")
        Label(window, text="Welcome!").grid(row=0, column=0)
        user.grid(row=1, column=0)
        input1.grid(row=1, column=1)
        password.grid(row=2, column=0)
        input2.grid(row=2, column=1)
        self.input1 = input1
        self.input2 = input2
        Button(window, text="Sign in", command=self.log).grid(row=3,column=0,sticky=W,pady=4)
        window.attributes('-topmost',True)
        window.update()
        self.loginwindow = window
        window.mainloop()

    def log(self):
        print("username",self.input1.get(),"and password",len(self.input2.get())*'*',"requests to login")
        db = Database('127.0.0.1', self.input1.get(), self.input2.get(), 'Plates')
        login = db.connect()
        if not login:
            messagebox.showinfo('Message','Wrong Credentials!')
        else:
            self.loginwindow.destroy()
            self.db = db
            messagebox.showinfo('Message','You are in!')
            self.operation()




    def operation(self):
        self.op = Tk()
        self.op.title("Admin Operations")
        self.op.geometry('600x600')
        input = Entry(self.op)
        input.grid(row=0,column=0)
        self.get = input
        Button(self.op, text="Search", command=self.help_search).grid(row=0, column=1)
        Button(self.op, text="Add", command=self.db.add).grid(row=1, column=0, sticky=W, pady=4)
        Button(self.op, text="Delete", command=self.db.delete).grid(row=1, column=1, sticky=W, pady=4)
        Button(self.op, text="Verify", command=self.help_verify).grid(row=2, column=0, sticky=W, pady=4)
        self.op.mainloop()

    def help_search(self):
        str = self.get.get()
        result = self.db.search(str)
        Label(self.op, text=result).grid(row=4, column=0)

    def help_verify(self):
        str = self.get.get()
        result = self.db.verify(str)
        Label(self.op, text="Match? %s" % result).grid(row=4, column=0)

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
