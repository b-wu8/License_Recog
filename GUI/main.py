from tkinter.filedialog import askopenfilename
from tkinter import *

root = Tk()
def OpenFile():
    name = askopenfilename(initialdir="C:/Users/",
                           filetypes =(("Graph File", "*.jpg"),("All Files","*.*")),
                           title = "Choose a file."
                           )
    print (name)
    #Using try in case user types in unknown file or closes without choosing a file.
    try:
        with open(name,'r') as UseFile:
            print(UseFile.read())
    except:
        print("No file exists")

menu = Menu(root)
root.config(menu=menu)
graphmenu = Menu(menu)
menu.add_cascade(label='Graph', menu=graphmenu)
graphmenu.add_command(label='Open...', command = OpenFile)
#graphmenu.add_command(label='Exit', command=root.quit)
videomenu = Menu(menu)
menu.add_cascade(label='Video', menu=videomenu)
videomenu.add_command(label='Connect Camera')

mainloop()
