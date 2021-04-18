from tkinter import *
from PIL import ImageTk, Image
import pyperclip
import keyboard

root = Tk()
root.geometry("480x480")
root.attributes('-alpha', 0.5)
root.title("Karel Hack")
root.resizable(False, False)
img = ImageTk.PhotoImage(Image.open("C:/Code/Pyhton/KarelChallenge/test.png"))
label = Label(image = img)
label.pack()
#root.mainloop() 



global file
file = open("C:\\Code\\Pyhton\\KarelChallenge\\karelChallenge.txt", "w")


rotation = ""


def wPressed():
    global rotation
    file = open("C:\\Code\\Pyhton\\KarelChallenge\\karelChallenge.txt", "a")
    if rotation == "down":
        file.write("\nturnAround();" + "\nmove();")
        rotation = "up"
    elif rotation == "left":
        file.write("\nturnRight();" + "\nmove();")
        rotation = "up"
    elif rotation == "right":
        file.write("\nturnLeft();" + "\nmove();")
        rotation = "up"
    else:
        file.write("\nmove();")
    file.close()

def aPressed():
    global rotation
    file = open("C:\\Code\\Pyhton\\KarelChallenge\\karelChallenge.txt", "a")
    if rotation == "down":
        file.write("\nturnRight();" + "\nmove();")
        rotation = "left"
    elif rotation == "up":
        file.write("\nturnLeft();" + "\nmove();")
        rotation = "left"
    elif rotation == "right":
        file.write("\nturnAround();" + "\nmove();")
        rotation = "left"
    else:
        file.write("\nmove();")
    file.close()

def sPressed():
    global rotation
    file = open("C:\\Code\\Pyhton\\KarelChallenge\\karelChallenge.txt", "a")
    if rotation == "up":
        file.write("\nturnAround();" + "\nmove();")
        rotation = "down"
    elif rotation == "left":
        file.write("\nturnLeft();" + "\nmove();")
        rotation = "down"
    elif rotation == "right":
        file.write("\nturnRight();" + "\nmove();")
        rotation = "down"
    else:
        file.write("\nmove();")
    file.close()

def dPressed():
    global rotation
    file = open("C:\\Code\\Pyhton\\KarelChallenge\\karelChallenge.txt", "a")
    if rotation == "down":
        file.write("\nturnLeft();" + "\nmove();")
        rotation = "right"
    elif rotation == "left":
        file.write("\nturnAround();" + "\nmove();")
        rotation = "right"
    elif rotation == "up":
        file.write("\nturnRight();" + "\nmove();")
        rotation = "right"
    else:
        file.write("\nmove();")
    file.close()

def enterPressed():
    global rotation
    file = open("C:\\Code\\Pyhton\\KarelChallenge\\karelChallenge.txt", "r")
    pyperclip.copy(file.read())
    file.close()
    file = open("C:\\Code\\Pyhton\\KarelChallenge\\karelChallenge.txt", "w")
    file.write("")

def backspacePressed():
    file = open("C:\\Code\\Pyhton\\KarelChallenge\\karelChallenge.txt", "r")
    lines = file.readlines()
    del lines[len(lines) - 1]
    backRes = ""
    for line in lines:
        backRes += line
    file.close()
    file = open("C:\\Code\\Pyhton\\KarelChallenge\\karelChallenge.txt", "w")
    file.write(backRes)
    file.close()

def globalReset():
    file = open("C:\\Code\\Pyhton\\KarelChallenge\\karelChallenge.txt", "a")
    file.write("\nglobalReset();")
    file.close()

def remove():
    file = open("C:\\Code\\Pyhton\\KarelChallenge\\karelChallenge.txt", "a")
    file.write("\nRemoveWall();")
    file.close()

def teleport(): 
    file = open("C:\\Code\\Pyhton\\KarelChallenge\\karelChallenge.txt", "a")
    file.write("\nteleport();")
    file.close()

def beeper():
    file = open("C:\\Code\\Pyhton\\KarelChallenge\\karelChallenge.txt", "a")
    file.write("\npickBeeper();")
    file.close()

def tray():
    file = open("C:\\Code\\Pyhton\\KarelChallenge\\karelChallenge.txt", "a")
    file.write("\nputBeeperInTray();")
    file.close()

while True:
    if(keyboard.is_pressed('w')):
        while keyboard.is_pressed("w"):
            pass
        wPressed()

    if(keyboard.is_pressed('a')):
        while keyboard.is_pressed("a"):
            pass
        aPressed()

    if(keyboard.is_pressed('s')):
        while keyboard.is_pressed("s"):
            pass
        sPressed()

    if(keyboard.is_pressed('d')):
        while keyboard.is_pressed("d"):
            pass
        dPressed()

    if(keyboard.is_pressed('Enter')):
        while keyboard.is_pressed("Enter"):
            pass
        enterPressed()

    if(keyboard.is_pressed('Backspace')):
        while keyboard.is_pressed("Backspace"):
            pass
        backspacePressed()
#globalReset
    if(keyboard.is_pressed('g')):
        while keyboard.is_pressed("g"):
            pass
        globalReset()
#removeWall
    if(keyboard.is_pressed('r')):
        while keyboard.is_pressed("r"):
            pass
        remove()
#teleport
    if(keyboard.is_pressed('t')):
        while keyboard.is_pressed("t"):
            pass
        teleport()
#pickBeper
    if(keyboard.is_pressed('f')):
        while keyboard.is_pressed("f"):
            pass
        beeper()
#putBeeperInTray
    if(keyboard.is_pressed('shift')):
        while keyboard.is_pressed("shift"):
            pass
        tray()

    if(keyboard.is_pressed('up')):
        while keyboard.is_pressed("up"):
            pass
        rotation = "up"

    if(keyboard.is_pressed('down')):
        while keyboard.is_pressed("down"):
            pass
        rotation = "down"

    if(keyboard.is_pressed('right')):
        while keyboard.is_pressed("right"):
            pass
        rotation = "right"

    if(keyboard.is_pressed('left')):
        while keyboard.is_pressed("left"):
            pass
        rotation = "left"
        
    