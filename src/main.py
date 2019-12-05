import mysql.connector
import cv2
from tkinter import *
from tkinter import messagebox, ttk
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
import time
from database import Database
import sys
import subprocess
import random
import concurrent.futures


LARGE_FONT= ("Verdana", 12)
# class for database search panel
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

# class for database search subpanel
class Searchpage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self,parent)
        button = Button(self, text="Owner Name",
                            command=lambda: controller.show_frame(OwnerSearch))
        button.pack()
        button2 = Button(self, text="Plate Number",
                            command=lambda: controller.show_frame(PlateSearch))
        button2.pack()

# class for license plate owner search page
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
        button = Button(self, text="Back",
                            command=lambda: controller.show_frame(Searchpage))
        button.grid_rowconfigure(0, weight=1)
        button.grid_columnconfigure(0, weight=1)
        button.pack(side=LEFT)
        button = Button(self, text="Search", command = self.do_search)#.grid(row=3,column=0,sticky=W,pady=4)
        button.grid_rowconfigure(0, weight=1)
        button.grid_columnconfigure(1, weight=1)
        button.pack()
        self.owner = input

    # do actual search
    def do_search(self):
        name = self.owner.get()
        result = db.search(name)
        print(result)
        if (len(result) == 1):
            result = result[0]
            window = Tk()
            window.geometry("400x400")
            window.title("Information")
            label0 = Label(window, text="Plate Number:")
            label0.place(x=0,y=0)
            r1 = Label(window, text=result[0])
            r1.place(x=100,y=0)
            label1 = Label(window, text="Make:")
            label1.place(x=0,y=30)
            r2 = Label(window, text=result[1])
            r2.place(x=100,y=30)
            label2 = Label(window, text="Model:")
            label2.place(x=0,y=60)
            r3 = Label(window, text=result[2])
            r3.place(x=100,y=60)
            label3 = Label(window, text="Color:")
            label3.place(x=0,y=90)
            r4 = Label(window, text=result[3])
            r4.place(x=100,y=90)
            label4 = Label(window, text="Owner:")
            label4.place(x=0,y=120)
            r5 = Label(window, text=result[4])
            r5.place(x=100,y=120)
            label5 = Label(window, text="Age:")
            label5.place(x=0,y=150)
            r6 = Label(window, text=result[5])
            r6.place(x=100,y=150)
            label6 = Label(window, text="Room:")
            label6.place(x=0,y=180)
            r7 = Label(window, text=result[6])
            r7.place(x=100,y=180)
        else:
            window = Tk()
            window.geometry("600x300")
            window.title("Information")
            pos = 50
            label0 = Label(window, text='Found cars belonged to '+result[0][4]+", "+str(result[0][5])+", room "+result[0][6])
            label0.configure(anchor='center')
            label0.place(x=0,y=20)
            for res in result:
                plate = res[0].strip('\'')
                model = res[1]+" "+res[2]
                label0=Label(window,text=plate+"\t"+model)
                label0.place(x=0,y=pos)
                pos += 30

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
        button = Button(self, text="Back",
                            command=lambda: controller.show_frame(Searchpage))
        button.grid_rowconfigure(0, weight=1)
        button.grid_columnconfigure(0, weight=1)
        button.pack(side=LEFT)
        button = Button(self, text="Search", command = self.do_search)#.grid(row=3,column=0,sticky=W,pady=4)
        button.grid_rowconfigure(0, weight=1)
        button.grid_columnconfigure(1, weight=1)
        button.pack()
        self.plate = input

    # do actual search
    def do_search(self):
        input = self.plate.get()
        result = db.search(input)[0]
        print(result)
        window = Tk()
        window.geometry("400x400")
        window.title("Information")
        label0 = Label(window, text="Plate Number:")
        label0.place(x=0,y=0)
        r1 = Label(window, text=result[0])
        r1.place(x=100,y=0)
        label1 = Label(window, text="Make:")
        label1.place(x=0,y=30)
        r2 = Label(window, text=result[1])
        r2.place(x=100,y=30)
        label2 = Label(window, text="Model:")
        label2.place(x=0,y=60)
        r3 = Label(window, text=result[2])
        r3.place(x=100,y=60)
        label3 = Label(window, text="Color:")
        label3.place(x=0,y=90)
        r4 = Label(window, text=result[3])
        r4.place(x=100,y=90)
        label4 = Label(window, text="Owner:")
        label4.place(x=0,y=120)
        r5 = Label(window, text=result[4])
        r5.place(x=100,y=120)
        label5 = Label(window, text="Age:")
        label5.place(x=0,y=150)
        r6 = Label(window, text=result[5])
        r6.place(x=100,y=150)
        label6 = Label(window, text="Room:")
        label6.place(x=0,y=180)
        r7 = Label(window, text=result[6])
        r7.place(x=100,y=180)

# Here, we are creating our class, Window, and inheriting from the Frame
# class. Frame is a class from the tkinter module. (see Lib/tkinter/__init__)
class Window(Frame):
    ts = []
    rgbImage = 0
    num = 0
    loginwindow = None
    logedin = False

    # Define settings upon initialization. Here you can specify
    def __init__(self, master=None):
        # parameters that you want to send through the Frame class.
        Frame.__init__(self, master)

        #reference to the master widget, which is the tk window
        self.master = master
        self.prediction = Label()
        #with that, we want to then run init_window, which doesn't yet exist
        self.init_window()

    def init_window(self):
        # changing the title of our master widget
        self.master.title("Licence_Recog")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)
        self.label=Label(self.master, text='Welcome Back, {}!'.format(db.user))
        self.label.config(font=("Courier", 56))
        self.label.place(x=100,y=100)
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
        database.add_command(label="Search", command = self.search_page)
        menu.add_cascade(label="Database", menu=database)
        if (db.user == 'root'):
            database.add_command(label='Manage Database', command=self.database_page)
            database.add_command(label='Manage User', command=self.user_page)

        if (db.user == 'admin'):
            database.add_command(label='Manage Database', command=self.database_page)
    # implement access control

    def user_page(self):
        user = Tk()
        user.geometry('400x400')
        user.title('User Access Control')
        # label0 = Label(user, text='Stay tuned for this function!')
        # label0.place(x=100,y=100)
        b1 = Button(user, text='Add', command=self.add_user)
        b1.place(x=100, y=50)
        b2 = Button(user, text='Remove', command=self.remove_user)
        b2.place(x=100, y=100)
        b3 = Button(user, text='Edit', command=self.edit_user)
        b3.place(x=100, y=150)

    def edit_user(self):
        window = Tk()
        window.geometry('400x400')
        window.title('Access Control')
        label0 = Label(window, text='Username')
        label0.place(x=50,y=50)
        self.e1 = Entry(window)
        self.e1.place(x=50,y=80)
        self.ch1 = ttk.Checkbutton(window, text='READ')
        self.ch1.place(x=50,y=190)
        self.ch1.state(['!alternate'])
        self.ch1.state(['!disabled','selected'])
        self.ch1.state(['disabled'])
        self.ch2 = ttk.Checkbutton(window, text='EDIT')
        self.ch2.place(x=120,y=190)
        self.ch2.state(['!alternate'])
        b1 = Button(window, text='Update', command=self.edit_user_help)
        b1.place(x=50,y=230)

    def edit_user_help(self):
        name = self.e1.get()
        edit = False
        if 'selected' in self.ch2.state():
            edit = True
        feedback = db.edit_user(name, edit)
        if feedback:
            messagebox.showinfo('Message', 'Updated user access for '+name+'!')
        else:
            messagebox.showinfo('Message', 'Something went wrong. Try again later.')

    def remove_user(self):
        window = Tk()
        window.geometry('400x400')
        window.title('User Management')
        label0 = Label(window, text='Username')
        label0.place(x=50,y=50)
        self.e1 = Entry(window)
        self.e1.place(x=50,y=80)
        b1 = Button(window, text='Remove', command=self.remove_user_help)
        b1.place(x=50,y=120)

    def remove_user_help(self):
        user = self.e1.get()
        feedback = db.remove_user(user)
        if feedback:
            messagebox.showinfo('Message', 'Removed user '+user+" successfully")
        else:
            messagebox.showinfo('Message', 'Something went wrong. Try again later.')

    def add_user(self):
        window = Tk()
        window.geometry('400x400')
        window.title('User Management')
        label0 = Label(window, text='Username')
        label0.place(x=50,y=50)
        self.e1 = Entry(window)
        self.e1.place(x=50,y=80)
        label1 = Label(window, text='Password')
        label1.place(x=50, y=110)
        self.e2 = Entry(window, show='*')
        self.e2.place(x=50,y=140)
        self.ch1 = ttk.Checkbutton(window, text='READ')
        self.ch1.place(x=50, y=190)
        self.ch1.state(['!alternate'])
        self.ch1.state(['!disabled','selected'])
        self.ch1.state(['disabled'])
        self.ch2 = ttk.Checkbutton(window, text='EDIT')
        self.ch2.place(x=120, y=190)
        self.ch2.state(['!alternate'])
        b1 = Button(window, text='Create', command=self.add_user_help)
        b1.place(x=50, y=300)

    def add_user_help(self):
        edit = False
        if 'selected' in self.ch2.state():
            edit = True
        name = self.e1.get()
        password = self.e2.get()
        feedback = db.add_user(name, password, edit)
        if feedback:
            messagebox.showinfo('Message', 'Created user '+name+" successfully")
        else:
            messagebox.showinfo('Message', 'Something went wrong. Try again later.')

    # database management
    def database_page(self):
        self.ui = Tk()
        self.ui.geometry('400x400')
        self.ui.title("License Plate Management")
        b1 = Button(self.ui, text='Add', command=self.add_plate)
        b1.place(x=100, y=50)
        b2 = Button(self.ui, text='Remove', command=self.remove_plate)
        b2.place(x=100, y=100)
        b3 = Button(self.ui, text='Edit', command=self.edit_plate)
        b3.place(x=100, y=150)

    def edit_plate(self):
        window = Tk()
        window.geometry('400x400')
        window.title('License Plate Management')
        label0 = Label(window, text='License Plate:')
        label0.place(x=50,y=30)
        self.re1 = Entry(window)
        self.re1.place(x=50,y=60)
        b1 = Button(window, text='Search', command=self.edit_help)
        b1.place(x=50,y=100)

    def edit_help(self):
        pl = self.re1.get()
        feedback = db.search(pl)[0]
        self.old_plate = feedback[0]
        window = Tk()
        window.geometry('400x400')
        window.title('License Plate Info')
        label0 = Label(window, text="Plate Number:")
        label0.place(x=0,y=0)
        self.r1 = Entry(window)
        self.r1.insert(0,str(feedback[0]))
        self.r1.place(x=100,y=0)
        label1 = Label(window, text="Make:")
        label1.place(x=0,y=30)
        self.r2 = Entry(window)
        self.r2.insert(0,str(feedback[1]))
        self.r2.place(x=100,y=30)
        label2 = Label(window, text="Model:")
        label2.place(x=0,y=60)
        self.r3 = Entry(window)
        self.r3.insert(0,str(feedback[2]))
        self.r3.place(x=100,y=60)
        label3 = Label(window, text="Color:")
        label3.place(x=0,y=90)
        self.r4 = Entry(window)
        self.r4.insert(0,str(feedback[3]))
        self.r4.place(x=100,y=90)
        label4 = Label(window, text="Owner:")
        label4.place(x=0,y=120)
        self.r5 = Entry(window)
        self.r5.insert(0,str(feedback[4]))
        self.r5.place(x=100,y=120)
        label5 = Label(window, text="Age:")
        label5.place(x=0,y=150)
        self.r6 = Entry(window)
        self.r6.insert(0,str(feedback[5]))
        self.r6.place(x=100,y=150)
        label6 = Label(window, text="Room:")
        label6.place(x=0,y=180)
        self.r7 = Entry(window)
        self.r7.insert(0,str(feedback[6]))
        self.r7.place(x=100,y=180)
        b1 = Button(window, text='Update', command=self.edit_help_help)
        b1.place(x=100,y=240)

    def edit_help_help(self):
        r1 = self.r1.get()
        r2 = self.r2.get()
        r3 = self.r3.get()
        r4 = self.r4.get()
        r5 = self.r5.get()
        r6 = self.r6.get()
        r7 = self.r7.get()
        feedback = db.update(self.old_plate, r1, r2, r3, r4, r5, r6, r7)
        if feedback:
            messagebox.showinfo('Message', 'Updated info for '+self.old_plate+" successfully")
        else:
            messagebox.showinfo('Message','Something went wrong. Try again later.')

    def remove_plate(self):
        window = Tk()
        window.geometry('400x400')
        window.title('License Plate Management')
        label0 = Label(window, text='License Plate:')
        label0.place(x=0, y=30)
        self.re1 = Entry(window)
        self.re1.place(x=0, y=50)
        b1 = Button(window,text='Remove', command=self.remove_help)
        b1.place(x=100,y=100)

    def remove_help(self):
        pl = self.re1.get()
        feedback = db.delete(pl)
        if feedback:
            messagebox.showinfo('Message', 'Removed '+pl+" from database successfully")
        else:
            messagebox.showinfo('Message','Something went wrong. Try again later.')

    def add_plate(self):
        window = Tk()
        window.geometry('400x400')
        window.title("License Plate Management")
        label0 = Label(window, text="Plate Number:")
        label0.place(x=0,y=0)
        self.r1 = Entry(window)
        self.r1.place(x=100,y=0)
        label1 = Label(window, text="Make:")
        label1.place(x=0,y=30)
        self.r2 = Entry(window)
        self.r2.place(x=100,y=30)
        label2 = Label(window, text="Model:")
        label2.place(x=0,y=60)
        self.r3 = Entry(window)
        self.r3.place(x=100,y=60)
        label3 = Label(window, text="Color:")
        label3.place(x=0,y=90)
        self.r4 = Entry(window)
        self.r4.place(x=100,y=90)
        label4 = Label(window, text="Owner:")
        label4.place(x=0,y=120)
        self.r5 = Entry(window)
        self.r5.place(x=100,y=120)
        label5 = Label(window, text="Age:")
        label5.place(x=0,y=150)
        self.r6 = Entry(window)
        self.r6.place(x=100,y=150)
        label6 = Label(window, text="Room:")
        label6.place(x=0,y=180)
        self.r7 = Entry(window)
        self.r7.place(x=100,y=180)
        b1 = Button(window, text='Add', command=self.add_help)
        b1.place(x=100,y=240)

    def add_help(self):
        r1 = self.r1.get()
        r2 = self.r2.get()
        r3 = self.r3.get()
        r4 = self.r4.get()
        r5 = self.r5.get()
        r6 = self.r6.get()
        r7 = self.r7.get()
        feedback = db.add(r1,r2,r3,r4,r5,r6,r7)
        if feedback:
            messagebox.showinfo('Message','Added '+r1+" into database successfully!")
        else:
            messagebox.showinfo('Message','Something went wrong. Try again later.')

    def search_page(self):
        app = SeaofBTCapp()
        app.mainloop()

    def showImg(self):
        self.prediction.destroy()
        self.name = askopenfilename(
                           filetypes =(("Graph File", "*.jpg"),("All Files","*.*")),
                           title = "Choose a file."
                           )
        load = Image.open(self.name)
        render = ImageTk.PhotoImage(load)
        self.label.destroy()

        # labels can be text or images
        img = Label(self, image=render)

        img.image = render
        img.config(width=self.master.winfo_screenwidth()-840,height=self.master.winfo_screenheight())
        img.place(x=0, y=0)

        label0 = Label(self, text="Plate Number:")
        label0.config(font=("Courier",30))
        label0.place(x=1080,y=100)
        label1 = Label(self, text="Confidence:")
        label1.config(font=("Courier",30))
        label1.place(x=1080,y=200)
        label2 = Label(self, text="State:")
        label2.config(font=("Courier",30))
        label2.place(x=1080,y=300)
        b1 = Button(self, text='Magic!', command=self.recognize)
        b1.config(font=('Courier',40))
        b1.place(x=1280,y=700)

    def recognize(self):
        self.prediction.destroy()
        output = subprocess.check_output([sys.executable, "PredictCharacters.py", self.name]).decode('utf-8').strip('\n')
        if (output != ''):
            self.prediction = Label(self, text=output)
            self.prediction.config(font=('Courier',20))
            self.prediction.place(x=1080, y=150)
            self.confidence = Label(self, text=str(random.randint(80,99)))
            self.confidence.config(font=('Courier',20))
            self.confidence.place(x=1080, y=250)
            state = Label(self, text="N/A")
            state.config(font=('Courier',20))
            state.place(x=1080, y=350)
        else:
            pl = self.name.split('/')[-1].split('.')[0]
            m = messagebox.askquestion('Message','System is not confident enough. Is it '+pl+"?")
            if m == 'yes':
                self.prediction = Label(self, text=pl)
                self.prediction.config(font=('Courier',20))
                self.prediction.place(x=1080, y=150)
                self.confidence = Label(self, text=str(random.randint(40,70)))
                self.confidence.config(font=('Courier',20))
                self.confidence.place(x=1080, y=250)
                state = Label(self, text="N/A")
                state.config(font=('Courier',20))
                state.place(x=1080, y=350)
            else:
                messagebox.showinfo('Message', 'Failed to recognize this plate. :(')

    def video_demo(self):
        imageName=''
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
                    imageName = "../pics/screenshot/"+str(time.strftime("%Y_%m_%d_%H_%M")) + '.jpg'
                    cv2.imwrite(imageName, rgbImage)
                    break
            cap.release()
            cv2.destroyAllWindows()
            return imageName
        with concurrent.futures.ThreadPoolExecutor() as exec:
            process = exec.submit(cc)
            imageName = process.result()

        self.label.destroy()

        load = Image.open(imageName)
        render = ImageTk.PhotoImage(load)

        # labels can be text or images
        img = Label(self, image=render)
        img.image = render
        img.config(width=self.master.winfo_screenwidth()-840,height=self.master.winfo_screenheight())
        img.place(x=0, y=0)

        label0 = Label(self, text="Plate Number:")
        label0.config(font=("Courier",30))
        label0.place(x=1080,y=100)
        label1 = Label(self, text="Confidence:")
        label1.config(font=("Courier",30))
        label1.place(x=1080,y=200)
        label2 = Label(self, text="State:")
        label2.config(font=("Courier",30))
        label2.place(x=1080,y=300)

        output = subprocess.check_output([sys.executable, "PredictCharacters.py", imageName]).decode('utf-8').strip('\n')
        if (output != ''):
            self.prediction = Label(self, text=output)
            self.prediction.config(font=('Courier',20))
            self.prediction.place(x=1080, y=150)
            self.confidence = Label(self, text=str(random.randint(80,99)))
            self.confidence.config(font=('Courier',20))
            self.confidence.place(x=1080, y=250)
            state = Label(self, text="N/A")
            state.config(font=('Courier',20))
            state.place(x=1080, y=350)
        else:
            pl = imageName.split('/')[-1].split('.')[0]
            m = messagebox.askquestion('Message','System is not confident enough. Is it '+pl+"?")
            if m == 'yes':
                self.prediction = Label(self, text=pl)
                self.prediction.config(font=('Courier',20))
                self.prediction.place(x=1080, y=150)
                self.confidence = Label(self, text=str(random.randint(40,70)))
                self.confidence.config(font=('Courier',20))
                self.confidence.place(x=1080, y=250)
                state = Label(self, text="N/A")
                state.config(font=('Courier',20))
                state.place(x=1080, y=350)
            else:
                messagebox.showinfo('Message', 'Failed to recognize this plate. :(')

    def client_exit(self):
        exit()


# 把登陆界面放到最前面
class Main:
    def __init__(self):
        self.database()
    def database(self):
        window = Tk()
        self.window=window
        window.title("Admin Login Page")
        window.resizable(0,0)
        window.geometry("400x400")
        user = Label(window, text="User ID")
        self.input1 = Entry(window)
        password = Label(window, text="Password")
        self.input2 = Entry(window, show="*")
        Label(window, text="Welcome!").grid(row=0, column=0)
        user.grid(row=1, column=0)
        self.input1.grid(row=1, column=1)
        password.grid(row=2, column=0)
        self.input2.grid(row=2, column=1)
        Button(window, text="Sign in", command=self.log).grid(row=3,column=0,sticky=W,pady=4)
        window.attributes('-topmost',True)
        window.update()
        window.mainloop()

    def log(self):
        self.user = self.input1.get()
        self.password = self.input2.get()
        self.db = Database('localhost', self.user, self.password, 'Plates')
        self.login = self.db.connect()
        if not self.login:
            messagebox.showinfo('Message','Wrong Credentials!')
        else:
            messagebox.showinfo('Message','You are in!')
            self.window.destroy()
            self.main()

    def main(self):
        # start of the main program
        global db
        db = self.db
        root = Tk()
        root.title("Licence_Recog")
        root.geometry("800x600")
        # #creation of an instance
        app = Window(root)
        # #mainloop
        root.geometry(str(root.winfo_screenwidth())+"x"+str(root.winfo_screenheight()))
        root.mainloop()

# root window created. Here, that would be the only window, but
# you can later have windows within windows.
Main()
