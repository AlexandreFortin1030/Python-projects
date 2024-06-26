from tkinter import *
import tkinter as tk
from tkinter import scrolledtext
import sys
import json
import os
import datetime


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


###################################### --- Functions


    def read_file_names(folder_path):

        file_names = []
        
        for file in os.listdir(folder_path):
            
            full_path = os.path.join(folder_path, file)
            if os.path.isfile(full_path):
                file_name_with_extension = os.path.basename(file)
                file_name, file_extension = os.path.splitext(file_name_with_extension)
                file_names.append(file_name)
        
        return file_names
    
    


##################### --- Main Read



    titleMain = Label(windowRead, text="***-- Read mode --***", font=20, background="maroon1")
    titleMain.place(x=650, y=5, width=300, height=40)

    listbox_frameMain = tk.Frame(windowRead)
    listbox_frameMain.place(x=400, y=100, width=1100, height=750)

    listboxMain = Listbox(listbox_frameMain,)
    listboxMain.pack(side="left", fill="both", expand=True)

    scrollbarMain = Scrollbar(listbox_frameMain, orient="vertical", command=listboxMain.yview)
    scrollbarMain.pack(side="right", fill="y")
    listboxMain.config(yscrollcommand=scrollbarMain.set)


##################### --- Left Read


    titleAuthor = Label(windowRead, text="*- Authors' list -*", background="lightpink1", font=16)
    titleAuthor.place(x=50, y=85, width=200, height=30)


    listbox_frameLeft = tk.Frame(windowRead)
    listbox_frameLeft.place(x=25, y=150, width=250, height=300)


    listboxLeft = Listbox(listbox_frameLeft,)
    listboxLeft.pack(side="left", fill="both", expand=True)

    folder_path = "/home/alexandre/Documents/soloDevProjects/python/Python_projects/MailArchiver/Archive"   # !! Une fois compilé, le path change car plus sur mon arborescence perso!!
    file_names = read_file_names(folder_path)
    for file_name in file_names:
        listboxLeft.insert(tk.END, file_name)


    scrollbarLeft = Scrollbar(listbox_frameLeft, orient="vertical", command=listboxLeft.yview)
    scrollbarLeft.pack(side="right", fill="y")
    listboxLeft.config(yscrollcommand=scrollbarLeft.set)


    chooseAuthor = Label(windowRead, text="- Enter author -", background="lightpink1", font=16)
    chooseAuthor.place(x=75, y=480, width=150, height=30)

    inputAuthor = Entry(windowRead)
    inputAuthor.place(x=50, y=520, width=200, height=30)
    inputAuthor["justify"]="center"


    def loadMessage():

        folder_path = "/home/alexandre/Documents/soloDevProjects/python/Python_projects/MailArchiver/Archive"  # Remplacez par votre chemin
        file_name = inputAuthor.get() + ".json"
        file_path = os.path.join(folder_path, file_name)

        
        with open(file_path, "r") as json_file:
            data = json.load(json_file)
            listboxMain.delete(0, tk.END)
            for key, value in data.items():
                listboxMain.insert(tk.END, key)
                listboxMain.insert(tk.END, "#")
                listboxMain.insert(tk.END, "#")
                listboxMain.insert(tk.END, "#")
                listboxMain.insert(tk.END, value)
                listboxMain.insert(tk.END, "#")
                listboxMain.insert(tk.END, "#")
                listboxMain.insert(tk.END, "#")
                listboxMain.insert(tk.END, "#")
                listboxMain.insert(tk.END, "#")
                listboxMain.insert(tk.END, "###########################################################################################################")


    buttonLoadLeft = Button(windowRead, text="Load messages", command=loadMessage, background="maroon1", activebackground="palegreen", font=18, highlightthickness=0)
    buttonLoadLeft.place(x=50, y=590, width=200, height=40)




##############################################
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

##################### --- Main Add

    titleMain = Label(windowAdd, text="***-- Add mode --***", font=18, background="maroon1")
    titleMain.place(x=650, y=10, width=300, height=30)

    inputMessage = scrolledtext.ScrolledText(windowAdd, wrap=tk.WORD)
    inputMessage.place(x=400, y=100, width=1100, height=750)


##################### --- Left Add


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

##################### --- Fonctions

    def show_popup():
    
        popup = Tk()
        popup.title("Status")
        popup.geometry("350x130")
        popup["bg"]="black"
        
        label = Label(popup, text="Message archived successfully", font=16, background="palegreen" )
        label.place(x=25,y=35, width=300, height=60)
        
        popup.after(2000, popup.destroy)
        
        popup.mainloop()

    def archive():
        author = inputAuthor.get()
        date = inputDate.get()
        message = inputMessage.get("1.0", tk.END)

        newdata = {date : message}
        folder_path = "/home/alexandre/Documents/soloDevProjects/python/Python_projects/MailArchiver/Archive"
        file_name = f"{author}.json"
        file_path = os.path.join(folder_path, file_name)

        if os.path.exists(file_path):
            with open(file_path, "r") as json_file:
                data = json.load(json_file)
        else:
            data = {}

        data.update(newdata)

        sorted_data = dict(sorted(data.items(), key=lambda item: datetime.datetime.strptime(item[0], "%d/%m/%y")))

        with open (file_path, "w") as json_file:
            json.dump(sorted_data, json_file, indent=4)

        inputAuthor.delete("0", tk.END)
        inputDate.delete("0", tk.END)
        inputMessage.delete("1.0", tk.END)

        show_popup()


        
       


    buttonArchive = Button(windowAdd, text="Archive message", command=archive, background="maroon1", activebackground="palegreen", font=18, highlightthickness=0)
    buttonArchive.place(x=50, y=690, width=200, height=40)






##############################################
def readme():
    windowAdd = Tk()
    windowAdd.title("Mail Archiver // Read me")
    windowAdd.geometry("600x450")
    windowAdd["bg"]="black"

    titleReadme = Label(windowAdd, text="### To read archived messages, go to Read mode,\n enter one author from the list in the form\n and click load messages.\n\n\n### To add a message to the archive, select the Add mode,\n enter an existing author from the list or a new one,\n a date in the right format and finally paste and edit\n your message in the main input form. You can then click\n the archive button and be safe.\n\n\n -cCrapiXx-", font=14, background="palegreen")
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