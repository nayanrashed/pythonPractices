import tkinter as tk
from tkinter import Canvas
win = tk.Tk()
#win.geometry("500x500")
x = 150
y = 230

b = int(input("dis cont.end value: "))
c = int(input("cont.end value: "))
d = int(input("mid value: "))

beam1 = Canvas(win, width=x, height=y, bg="white")
#beam1.pack(pady=30)
beam1.grid(row=0, column=0)
beam1.create_rectangle(15,15,135,215, fill="yellow")
beam1.create_rectangle(25,25,125,205, fill="blue")

def btop12():
    beam1.create_oval(25,25,40,40, fill= "red"),
    beam1.create_oval(110,25,125,40, fill= "red")
    beam1.create_oval(25, 190, 40, 205, fill="red")
    beam1.create_oval(110, 190, 125, 205, fill="red")

def btop13():
    beam1.create_oval(25,25,40,40, fill= "red")
    beam1.create_oval(68,25,83,40, fill= "red")
    beam1.create_oval(110,25,125,40, fill= "red")
    beam1.create_oval(25, 190, 40, 205, fill="red")
    beam1.create_oval(110, 190, 125, 205, fill="red")

def btop14():
    beam1.create_oval(25, 25, 40, 40, fill="red")
    beam1.create_oval(110, 25, 125, 40, fill="red")
    beam1.create_oval(25, 50, 40, 65, fill="red")
    beam1.create_oval(110, 50, 125, 65, fill="red")
    beam1.create_oval(25, 190, 40, 205, fill="red")
    beam1.create_oval(110, 190, 125, 205, fill="red")

def btop15():
    beam1.create_oval(25, 25, 40, 40, fill="red"),
    beam1.create_oval(68,25,83,40, fill= "red"),
    beam1.create_oval(110, 25, 125, 40, fill="red")
    beam1.create_oval(25, 50, 40, 65, fill="red")
    beam1.create_oval(110, 50, 125, 65, fill="red")
    beam1.create_oval(25, 190, 40, 205, fill="red")
    beam1.create_oval(110, 190, 125, 205, fill="red")

def btop16():
    beam1.create_oval(25, 25, 40, 40, fill="red")
    beam1.create_oval(68,25,83,40, fill= "red")
    beam1.create_oval(110, 25, 125, 40, fill="red")
    beam1.create_oval(25, 50, 40, 65, fill="red")
    beam1.create_oval(68, 50, 83, 65, fill="red")
    beam1.create_oval(110, 50, 125, 65, fill="red")
    beam1.create_oval(25, 190, 40, 205, fill="red")
    beam1.create_oval(110, 190, 125, 205, fill="red")

if b == 2:
    btop12()
elif b==3:
    btop13()
elif b==4:
    btop14()
elif b==5:
    btop15()
else:
    btop16()

beam2 = Canvas(win, width=150, height=230, bg="white")
beam2.grid(row=0, column=1)
beam2.create_rectangle(15,15,135,215, fill="yellow")
beam2.create_rectangle(25,25,125,205, fill="blue")
def btop22():
    beam2.create_oval(25,25,40,40, fill= "red"),
    beam2.create_oval(110,25,125,40, fill= "red")

    beam2.create_oval(25, 190, 40, 205, fill="red")
    beam2.create_oval(110, 190, 125, 205, fill="red")


def btop23():
    beam2.create_oval(25,25,40,40, fill= "red")
    beam2.create_oval(68,25,83,40, fill= "red")
    beam2.create_oval(110,25,125,40, fill= "red")

    beam2.create_oval(25, 190, 40, 205, fill="red")
    beam2.create_oval(110,190,125,205, fill= "red")

def btop24():
    beam2.create_oval(25, 25, 40, 40, fill="red")
    beam2.create_oval(110, 25, 125, 40, fill="red")
    beam2.create_oval(25, 50, 40, 65, fill="red")
    beam2.create_oval(110, 50, 125, 65, fill="red")

    beam2.create_oval(25, 190, 40, 205, fill="red")
    beam2.create_oval(110,190,125,205, fill= "red")

def btop25():
    beam2.create_oval(25, 25, 40, 40, fill="red"),
    beam2.create_oval(68,25,83,40, fill= "red"),
    beam2.create_oval(110, 25, 125, 40, fill="red")
    beam2.create_oval(25, 50, 40, 65, fill="red")
    beam2.create_oval(110, 50, 125, 65, fill="red")

    beam2.create_oval(25, 190, 40, 205, fill="red")
    beam2.create_oval(110,190,125,205, fill= "red")

def btop26():
    beam2.create_oval(25, 25, 40, 40, fill="red"),
    beam2.create_oval(68,25,83,40, fill= "red"),
    beam2.create_oval(110, 25, 125, 40, fill="red")
    beam2.create_oval(25, 50, 40, 65, fill="red")
    beam2.create_oval(68, 50, 83, 65, fill="red")
    beam2.create_oval(110, 50, 125, 65, fill="red")

    beam2.create_oval(25, 190, 40, 205, fill="red")
    beam2.create_oval(110,190,125,205, fill= "red")

if c == 2:
    btop22()
elif c==3:
    btop23()
elif c==4:
    btop24()
elif c==5:
    btop25()
else:
    btop26()



beam3: Canvas = Canvas(win, width=150, height=230, bg="white")
beam3.grid(row=0, column=2)
beam3.create_rectangle(15,15,135,215, fill="yellow")
beam3.create_rectangle(25,25,125,205, fill="blue")

def btop32():
    beam3.create_oval(25,190,40,205, fill= "red")
    beam3.create_oval(110,190,125,205, fill= "red")

    beam3.create_oval(25, 25, 40, 40, fill="red")
    beam3.create_oval(110, 25, 125, 40, fill="red")


def btop33():
    beam3.create_oval(25,190,40,205, fill= "red")
    beam3.create_oval(68,190,83,205, fill= "red")
    beam3.create_oval(110,190,125,205, fill= "red")

    beam3.create_oval(25, 25, 40, 40, fill="red")
    beam3.create_oval(110, 25, 125, 40, fill="red")


def btop34():
    beam3.create_oval(25,190,40,205, fill= "red")
    beam3.create_oval(110,190,125,205, fill= "red")
    beam3.create_oval(25,165,40,180, fill= "red")
    beam3.create_oval(110,165,125,180, fill= "red")

    beam3.create_oval(25, 25, 40, 40, fill="red")
    beam3.create_oval(110, 25, 125, 40, fill="red")

def btop35():
    beam3.create_oval(25,190,40,205, fill= "red")
    beam3.create_oval(68,190,83,205, fill= "red")
    beam3.create_oval(110,190,125,205, fill= "red")
    beam3.create_oval(25,165,40,180, fill= "red")
    beam3.create_oval(110,165,125,180, fill= "red")

    beam3.create_oval(25, 25, 40, 40, fill="red")
    beam3.create_oval(110, 25, 125, 40, fill="red")

def btop36():
    beam3.create_oval(25,190,40,205, fill= "red")
    beam3.create_oval(68,190,83,205, fill= "red")
    beam3.create_oval(110,190,125,205, fill= "red")
    beam3.create_oval(25,165,40,180, fill= "red")
    beam3.create_oval(68,165,83,180, fill= "red")
    beam3.create_oval(110,165,125,180, fill= "red")

    beam3.create_oval(25, 25, 40, 40, fill="red")
    beam3.create_oval(110, 25, 125, 40, fill="red")

if d==2:
    btop32()
elif d==3:
    btop33()
elif d==4:
    btop34()
elif d==5:
    btop35()
else:
    btop36()


win.mainloop()