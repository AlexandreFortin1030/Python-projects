from tkinter import *
import tkinter as tk
import sys


windowMenu = Tk()
windowMenu.title("Mail Archiver")
windowMenu.geometry("600x400")
windowMenu["bg"]="mediumorchid2"

#############################################
#############################################
def read():
    windowRead = Tk()
    windowRead.title("Mail Archiver")
    windowRead.geometry("1600x900")
    windowRead["bg"]="plum1"

    canvasLeft = tk.Canvas(windowRead, width=300, height=850, highlightthickness=0)
    canvasLeft.pack()
    canvasLeft.create_rectangle(0, 0, 300, 850, fill="mediumorchid2")
    canvasLeft.place(x=0,y=50)

    canvasTop = tk.Canvas(windowRead, width=1600, height=50, highlightthickness=0)
    canvasTop.pack()
    canvasTop.create_rectangle(0, 0, 1600, 50, fill="black")
    canvasTop.place(x=0,y=0)

    titleMain = Label(windowRead, text="***-- Read mode --***", font=20, background="maroon1")
    titleMain.place(x=650, y=5, width=300, height=40)

    titleAuthor = Label(windowRead, text="*- Authors' list -*", background="lightpink1", font=16)
    titleAuthor.place(x=50, y=85, width=200, height=30)



    listbox_frameLeft = tk.Frame(windowRead)
    listbox_frameLeft.place(x=25, y=150, width=250, height=300)

    listboxLeft = Listbox(listbox_frameLeft,)
    listboxLeft.pack(side="left", fill="both", expand=True)

    scrollbarLeft = Scrollbar(listbox_frameLeft, orient="vertical", command=listboxLeft.yview)
    scrollbarLeft.pack(side="right", fill="y")
    listboxLeft.config(yscrollcommand=scrollbarLeft.set)

    buttonLoadLeft = Button(windowRead, text="Load messages",background="maroon1", activebackground="palegreen", font=18, highlightthickness=0)
    buttonLoadLeft.place(x=50, y=600, width=200, height=40)



    listbox_frameMain = tk.Frame(windowRead)
    listbox_frameMain.place(x=400, y=150, width=1100, height=650)

    listboxMain = Listbox(listbox_frameMain,)
    listboxMain.pack(side="left", fill="both", expand=True)

    scrollbarMain = Scrollbar(listbox_frameMain, orient="vertical", command=listboxMain.yview)
    scrollbarMain.pack(side="right", fill="y")
    listboxMain.config(yscrollcommand=scrollbarMain.set)






##############################################
##############################################
def add():
    windowAdd = Tk()
    windowAdd.title("Mail Archiver")
    windowAdd.geometry("1600x900")
    windowAdd["bg"]="plum1"

    canvasLeft = tk.Canvas(windowAdd, width=300, height=850, highlightthickness=0)
    canvasLeft.pack()
    canvasLeft.create_rectangle(0, 0, 300, 850, fill="mediumorchid2")
    canvasLeft.place(x=0,y=50)

    canvasTop = tk.Canvas(windowAdd, width=1600, height=50, highlightthickness=0)
    canvasTop.pack()
    canvasTop.create_rectangle(0, 0, 1600, 50, fill="black")
    canvasTop.place(x=0,y=0)


    titleMain = Label(windowAdd, text="***-- Add mode --***", font=18, background="maroon1")
    titleMain.place(x=650, y=10, width=300, height=30)

    titleAuthor = Label(windowAdd, text="*- Authors' list -*", font=16, background="lightpink1")
    titleAuthor.place(x=50, y=85, width=200, height=30)


    listbox_frameLeft = tk.Frame(windowAdd)
    listbox_frameLeft.place(x=25, y=150, width=250, height=300)

    listboxLeft = Listbox(listbox_frameLeft,)
    listboxLeft.pack(side="left", fill="both", expand=True)

    scrollbarLeft = Scrollbar(listbox_frameLeft, orient="vertical", command=listboxLeft.yview)
    scrollbarLeft.pack(side="right", fill="y")
    listboxLeft.config(yscrollcommand=scrollbarLeft.set)


    titleEnterAuthor = Label(windowAdd, text="- Enter author -", font=14, background="lightpink1")
    titleEnterAuthor.place(x=75, y=480, width=150, height=30)

    inputAuthor = Entry(windowAdd)
    inputAuthor.place(x=50, y=520, width=200, height=30)
    inputAuthor["justify"]="center"


    titleEnterDate = Label(windowAdd, text="- Enter date -", font=14, background="lightpink1")
    titleEnterDate.place(x=75, y=580, width=150, height=30)

    inputDate = Entry(windowAdd)
    inputDate.place(x=50, y=620, width=200, height=30)
    inputDate["justify"]="center"
    inputDate.insert(0, "jj/mm/yy")

    def archive():
        print("hello")

    buttonArchive = Button(windowAdd, text="Archive message", command=archive, background="maroon1", activebackground="palegreen", font=18, highlightthickness=0)
    buttonArchive.place(x=50, y=690, width=200, height=40)



    listbox_frameMain = tk.Frame(windowAdd)
    listbox_frameMain.place(x=400, y=150, width=1100, height=650)

    listboxMain = Listbox(listbox_frameMain,)
    listboxMain.pack(side="left", fill="both", expand=True)

    scrollbarMain = Scrollbar(listbox_frameMain, orient="vertical", command=listboxMain.yview)
    scrollbarMain.pack(side="right", fill="y")
    listboxMain.config(yscrollcommand=scrollbarMain.set)




##############################################
def readme():
    windowAdd = Tk()
    windowAdd.title("Mail Archiver // Read me")
    windowAdd.geometry("600x450")
    windowAdd["bg"]="black"

    titleReadme = Label(windowAdd, text="### To read archived messages, go to Read mode,\n enter one author from the list in the form\n and click load messages.\n\n\n### To add a message to the archive, select the Add mode,\n enter an existing author from the list or a new one,\n a date in the right format and finally paste and edit\n your message in the main input form. You can then click\n the archive button and be safe.", font=14, background="palegreen")
    titleReadme.place(x=30, y=50, width=540, height=350)

##############################################

def quit():
    sys.exit()

buttonRead = Button(text="Read archive", command=read, background="maroon1", activebackground="palegreen", foreground="white", highlightthickness=0, font=18)
buttonRead.place(x=200, y=60, width=200, height=40)

buttonAdd = Button(text="Add to archive", command=add, background="maroon1", activebackground="palegreen",foreground="white", highlightthickness=0, font=18)
buttonAdd.place(x=200, y=140, width=200, height=40)

buttonReadme = Button(text="Read me", command=readme, background="mediumorchid1", activebackground="coral",foreground="white", highlightthickness=0, font=18)
buttonReadme.place(x=225, y=220, width=150, height=30)

buttonQuit = Button(text="Quit", command=quit, background="black", activebackground="orangered", foreground="white", highlightthickness=0)
buttonQuit.place(x=250, y=300, width=100, height=40)



windowMenu.mainloop()