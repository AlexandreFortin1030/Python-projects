from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import sys
import random
import os


root = Tk()
root.title("Eraser")
root.geometry("600x450")
bg = PhotoImage(file = "./blurry.png") 

background_label = Label(root, image=bg)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

########################## Functions



###---------> Erase File _

def erase_file_window():
    windowFile = tk.Toplevel(root) 
    windowFile.geometry("600x600")
    windowFile.title("Erase file")
    windowFile["bg"]= "black"

    bg = PhotoImage(file = "./eraseFile.png") 

    background_label = Label(windowFile, image=bg, border=0)
    background_label.image = bg
    background_label.pack(pady=20)


    def select_file():
        global file_path
        file_path = filedialog.askopenfilename()
        if file_path:
            selected_file_label.config(text=f"---> Selected file: {file_path}", foreground="chartreuse1")

    select_button = Button(windowFile, text="Select file", command=select_file, highlightthickness=0, background="darkorange1")
    select_button.pack(pady=20)

    selected_file_label = Label(windowFile, text="---> No file selected yet", background="black", foreground="White")
    selected_file_label.pack(pady=10)

    About_label = Label(windowFile, text="Click the above button and select a file (not a directory) in your file system.\n Please ignore all files and directories starting with a dot (ex: '.filename')\n as they are hidden files that you are mosty likely not supposed to alter.\n Becareful to select and erase only well known files as you might\n destroy your whole system ;)", background="black", foreground="white")
    About_label.pack(pady=20)


    def erase_file(file_path, num_passes=6 ):
        if not os.path.isfile(file_path):
            raise ValueError("The provided path does not point to a valid file")

        file_size = os.path.getsize(file_path)

        with open(file_path, "r+b") as file:
            for i in range (num_passes):
                file.seek(0)
                file.write(os.uramdom(file_size))
                file.slush()
                


    erase_button = Button(windowFile, text="   Erase file   ", command=erase_file, highlightthickness=0, background="firebrick1")
    erase_button.pack(pady=30)



    windowFile.grab_set()



###---------> Cleab Device _

def clean_device_window():
    windowDevice = tk.Toplevel(root) 
    windowDevice.geometry("600x300")
    windowDevice.title("Clean device")

    buttonCleanDevice = Button(text="Clean selected device")




    windowDevice.grab_set()
    windowDevice.mainloop()



###---------> Quit _
    

def quit():
    sys.exit()

##################### Main Buttons

button1 = Button(text="Erase file", command=erase_file_window, highlightthickness=0, activebackground="orangered1")
button1.place(x=200, y=200, width=200, height=40)
button1["bg"]="lightpink"

button2 = Button(text="Clean device", command=clean_device_window, highlightthickness=0, activebackground="orangered2")
button2.place(x=200, y=270, width=200, height=40)
button2["bg"]="lightpink2"

button3 = Button(text="Quit", command=quit, highlightthickness=0, activebackground="orangered3")
button3.place(x=200, y=340, width=200, height=40)
button3["bg"]="lightpink4"







root.mainloop()


# Remains:
# finish basic logic and functions for erase file and clean device windows
# add a progress hint for each process as it takes a long time.