from tkinter import *
import random
import sys
import pygame.mixer

pygame.mixer.init()
pygame.mixer.music.load("Theme.mp3")
sound_effect_Success = pygame.mixer.Sound("success.mp3")
sound_effect_Faillure = pygame.mixer.Sound("faillure.mp3")
pygame.mixer.music.play(loops=-1)

# selection of operands among list (+/-/x)
operandList = ["+","+"]   # put 2 otherwise program won't always launch
maxindex = len(operandList) - 1
num3 = random.randint(0, maxindex)

operand = operandList[num3]
num1 = None
num2 = None
points = 0

def pickNumbers():
    global num1, num2, operand
    if operand == "-":
        num1 = random.randint(40, 100)
        num2 = random.randint(1, 40)
    elif operand == "x":
        num1 = random.randint(1, 10)
        num2 = random.randint(10, 20)
    else:
        num1 = random.randint(10, 50)
        num2 = random.randint(10, 50)
    return num1, num2

pickNumbers()


###############################---  GUI  ---#################################

window = Tk()
window.title("Math quiz")
window.geometry("600x500")
window["bg"]="black"


labelIntro = Label(text="Welcome to the quiz. Choose your operands")
labelIntro.place(x=100, y=15, width=400, height=20)
labelIntro["bg"]= "black"
labelIntro["fg"]="white"
labelIntro["justify"]="center"

line = Label(text="################################")
line.place(x=100, y=95, width=400, height=20)
line["bg"]= "black"
line["fg"]="grey"

question = Label(text= str(num1) + "    " + operand + "    " + str(num2))
question.place(x=210, y=140, width=180, height=40)
question["bg"]= "dark blue"
question["fg"]="chocolate"
question.config(font=("helvetica", 18))

labelequal = Label(text="Enter result:")
labelequal.place(x=260, y=190, width=80, height=30)
labelequal["bg"]= "black"
labelequal["fg"]="white"

entryVar = StringVar()
entry_box= Entry(textvariable= entryVar)
entry_box.place(x=250, y=220, width=100, height=30)
entry_box["justify"]="center"

score = Label(text="Score: " + str(points))
score.place(x=30, y=250, width=120, height=40)
score["bg"]= "black"
score["fg"]="red"
score.config(font=("courrierNew", 16))

logoimage = Label(window)
logoimage.place(x=200, y=320, width=200, height=150)
logoimage["bg"]="black"

error = Label(text= "")
error.place(x=100, y=480, width=400, height=30)
error["bg"]= "black"
error["fg"]="red"
error["justify"]="center"

########################################################################


true_logo = None   # against garbage memory mecanism
false_logo = None

entry_box.focus()

def changeNum():

    global num1, num2, num3, operand, operandList

    maxindex = len(operandList) - 1
    num3 = random.randint(0, maxindex)
    operand = operandList[num3]
    pickNumbers()

    question.config(text=str(num1) + "    " + operand + "    " + str(num2))


def clearInput():
    entry_box.delete(0, END)

def displayError():
    error.config(text="!!!!!  You must choose at leat one operand  !!!!!")    

def clearError():
    error.config(text="")


def check(event=None):                                            # event = None, pas très clair...
    global true_logo, false_logo, num1, num2, points, score

    if operandList == []:
       displayError()

    else:
        if operand == "+":
            res = num1 + num2
        elif operand == "-":
            res = num1 - num2
        elif operand == "x":
            res = num1 * num2


        proposal = entry_box.get()

        if int(proposal) == res:
            sound_effect_Success.play()
            true_logo = PhotoImage(file="true.gif")
            logoimage.config(image=true_logo)
            logoimage.image = true_logo
            points += 1
            score.config(text="Score: " + str(points))
            
        
        else:
            sound_effect_Faillure.play()
            false_logo = PhotoImage(file="false.gif")
            logoimage.config(image=false_logo)                         # Pourquoi des étapes avec config puis nouvelles référence à l'image ensuite??
            logoimage.image = false_logo

        clearError()
        changeNum()

        clearInput()
        entry_box.focus()

###################--- Modes ---#######################

def addmode():
    global operandList
    if "+" in operandList:
        operandList = [x for x in operandList if x != "+"]  # removes any occurence of "+" in operandList
        buttonAdd["bg"]="grey"

    elif "+" not in operandList:
        operandList.append("+")
        operandList.append("+")
        buttonAdd["bg"]="chartreuse"

        
    
def minusmode():
    global operandList
    if "-" in operandList:
        operandList.remove("-")
        buttonMinus["bg"]="grey"

    elif "-" not in operandList:
        operandList.append("-")
        buttonMinus["bg"]="chartreuse"

        

def multimode():
    global operandList
    if "x" in operandList:
        operandList.remove("x")
        buttonMulti["bg"]="grey"

    elif "x" not in operandList:
        operandList.append("x")
        buttonMulti["bg"]="chartreuse"



buttonAdd = Button(text="+", command= addmode, activebackground="greenyellow", background="chartreuse")
buttonAdd.place(x=153, y=55, width=30, height=20)
buttonAdd.config(font=("helvetica", 16))

buttonMinus = Button(text="-", command= minusmode, activebackground="greenyellow")
buttonMinus.place(x=284, y=55, width=30, height=20)
buttonMinus.config(font=("helvetica", 16))

buttonMulti = Button(text="x", command=multimode, activebackground="greenyellow")
buttonMulti.place(x=417, y=55, width=30, height=20)
buttonMulti.config(font=("helvetica", 16))


buttonCheck= Button(text="Check", command=check, activebackground="black", activeforeground="white")
buttonCheck.place(x=250, y=270, width=100, height=30)

def quit():
    sys.exit()

buttonQuit= Button(text="Quit", command=quit, background="black", foreground="red", activeforeground="navy")
buttonQuit.place(x=515, y=460, width=70, height=25)


window.bind('<Return>', check)


window.mainloop()




