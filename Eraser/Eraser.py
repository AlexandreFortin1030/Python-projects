from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import sys
import random


root = Tk()
root.title("Eraser")
root.geometry("600x450")
bg = PhotoImage(file = "./blurry.png") 

background_label = Label(root, image=bg)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

########################## Functions

def erase_file_window():
    windowFile = tk.Toplevel(root) 
    windowFile.geometry("600x300")
    windowFile.title("Erase file")

    def select_file():
        file_path = filedialog.askopenfilename()
        if file_path:
            selected_file_label.config(text=f"Selected file: {file_path}")

    select_button = Button(windowFile, text="Select File", command=select_file)
    select_button.pack(pady=20)

    selected_file_label = Label(windowFile, text="Click the above button and select a file in your file system.\n Please ignore all files and directories starting with a dot (ex: '.filename')\n as they are hidden files that you are mosty likely not supposed to alter.\n Becareful to select and erase only well known files as you might\n destroy your whole system ;)")
    selected_file_label.pack(pady=20)

    # Selected file label = file path to be erased.
    # Need to write erase function similar to shed or other os built in methods
    # filter hidden files as only adds complexity and probs of messing up



    windowFile.grab_set()


def clean_device_window():
    windowDevice = tk.Toplevel(root) 
    windowDevice.geometry("600x300")
    windowDevice.title("Clean device")

    buttonCleanDevice = Button(text="Clean selected device")




    windowDevice.grab_set()
    windowDevice.mainloop()

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