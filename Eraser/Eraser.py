import tkinter as tk
from tkinter import PhotoImage, filedialog
from tkinter import ttk
import os
import sys
from cryptography.fernet import Fernet 

root = tk.Tk()
root.title("Eraser")
root.geometry("600x450")
bg = PhotoImage(file="./blurry.png")

background_label = tk.Label(root, image=bg)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Global variable to store the selected file path
selected_file_path = None

########################## Functions


#####--------> Erase File

def erase_file_window():
    windowFile = tk.Toplevel(root)
    windowFile.geometry("600x700")
    windowFile.title("Erase file")
    windowFile["bg"] = "black"

    bg = PhotoImage(file="./eraseFile.png")

    background_label = tk.Label(windowFile, image=bg, border=0)
    background_label.image = bg
    background_label.pack(pady=20)

    def select_file():
        global selected_file_path
        file_path = filedialog.askopenfilename()
        if file_path:
            selected_file_path = file_path
            selected_file_label.config(text=f"---> Selected file: {file_path}", foreground="chartreuse1")

    select_button = tk.Button(windowFile, text="Select file", command=select_file, highlightthickness=0, background="darkorange1")
    select_button.pack(pady=20)

    about_label = tk.Label(windowFile, text="Click the above button and select a file (not a directory) in your file system.\n Please ignore all files and directories starting with a dot (ex: '.filename')\n as they are hidden files that you are mostly likely not supposed to alter.\n Be careful to select and erase only well-known files as you might\n destroy your whole system ;)", background="black", foreground="white")
    about_label.pack(pady=20)

    global selected_file_label
    selected_file_label = tk.Label(windowFile, text="---> No file selected yet", background="black", foreground="White")
    selected_file_label.pack(pady=10)

    progress = ttk.Progressbar(windowFile, orient="horizontal", length=300, mode="determinate")
    progress.pack(pady=20)

    def erase_file():
        global selected_file_path
        if not selected_file_path:
            selected_file_label.config(text="---> No file selected to erase", foreground="red")
            return

        file_path = selected_file_path
        if not os.path.isfile(file_path):
            selected_file_label.config(text="---> Invalid file selected", foreground="red")
            return
        
        # single file encryption

        def encrypt_file(file_path):
            key_gen = Fernet.generate_key()
            key = Fernet(key_gen)
            with open(file_path, 'rb') as file:
                file_content = file.read()
                print(file_content)
                # ok until here
                encrypted_content = key.encrypt(file_content)
            with open(file_path, 'wb') as file:
                file.write(encrypted_content)

            with open(file_path, "rb") as encrypted_file:
                test = encrypted_file.read()
                print(test)

        ### Initialize encryption
        encrypt_file(file_path)


        file_size = os.path.getsize(file_path)
        num_passes = 12

        try:
            with open(file_path, "r+b") as file:
                for pass_num in range(num_passes):
                    file.seek(0)
                    file.write(os.urandom(file_size))
                    file.flush()
                    os.fsync(file.fileno())

                    # Update the progress bar
                    progress["value"] = (pass_num + 1) / num_passes * 100
                    windowFile.update_idletasks()

            with open(file_path, "r+b") as file:
                file.truncate(0)

            os.remove(file_path)
            selected_file_label.config(text="---> File erased successfully", foreground="chartreuse1")
        except Exception as e:
            selected_file_label.config(text=f"Error erasing file: {e}", foreground="red")

    erase_button = tk.Button(windowFile, text="Erase file", command=erase_file, highlightthickness=0, background="firebrick1")
    erase_button.pack(pady=30)

    windowFile.grab_set()





#####--------> Clean Device


def clean_device_window():
    windowDevice = tk.Toplevel(root)
    windowDevice.geometry("600x700")
    windowDevice.title("Erase file")
    windowDevice["bg"] = "black"

    bg = PhotoImage(file="./eraseFile.png")

    background_label = tk.Label(windowDevice, image=bg, border=0)
    background_label.image = bg
    background_label.pack(pady=20)
    windowDevice.grab_set()

    # multi file encryption (use os module to gather all file from device into one array of files and use a loop after wards to )




#####--------> Quit


def quit_app():
    sys.exit()

##################### Main Buttons

button1 = tk.Button(root, text="Erase file", command=erase_file_window, highlightthickness=0, activebackground="orangered1")
button1.place(x=200, y=200, width=200, height=40)
button1["bg"] = "lightpink"

button2 = tk.Button(root, text="Clean device", command=clean_device_window, highlightthickness=0, activebackground="orangered2")
button2.place(x=200, y=270, width=200, height=40)
button2["bg"] = "lightpink2"

button3 = tk.Button(root, text="Quit", command=quit_app, highlightthickness=0, activebackground="orangered3")
button3.place(x=200, y=340, width=200, height=40)
button3["bg"] = "lightpink4"

root.mainloop()
