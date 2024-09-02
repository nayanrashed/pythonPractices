import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import tkinter as tk
from tkinter import ttk
win = tk.Tk()

win.title("Beam Design")
#labels
label1 = tk.Label(win, text="Point Load:")
label1.grid(row=0, column=0)

label2 = tk.Label(win, text="Distance (a):")
label2.grid(row=1, column=0)

label3 = tk.Label(win, text="Distance (b):")
label3.grid(row=2, column=0)

label4 = tk.Label(win, text="Maximum Moment:")
label4.grid(row=1, column=3)

mm = tk.StringVar()
label5 = tk.Label(win, text="MM", textvariable = mm )
label5.grid(row=2, column=3)

#Entry box
p_var = tk.IntVar()
p_ebox = tk.Entry(win, width=20, textvariable = p_var )
p_ebox.grid(row=0, column=1)

da_var = tk.IntVar()
da_ebox = tk.Entry(win, width=20, textvariable = da_var)
da_ebox.grid(row=1, column=1)

db_var = tk.IntVar()
db_ebox = tk.Entry(win, width=20, textvariable = db_var)
db_ebox.grid(row=2, column=1)

def maxmoment():
    p_load = p_var.get()
    a = da_var.get()
    b = db_var.get()
    l = a + b
    r1 = (p_load * b) / l
    r2 = (p_load * a) / l
    #print("Reaction R1: ", r1)
    #print("Reaction R2: ", r2)
    a1 = a + 1
    l1 = l + 1
    li1 = list(range(a1))
    li2 = list(range(a, l1))
    li = li1 + li2
    m1 = []
    for x in range(0, a1, 1):
        m = r1 * x
        m1.append(m)
    for x in range(a, l1, 1):
        m = r1 * x - p_load * (x - a)
        m1.append(m)
    #print(li)
    #print(m1)

    max_n = m1[0]
    for n in m1:
        if n > max_n:
            max_n = n
    #print('Maximum Moment;', max_n)
    mm.set(max_n)

    plt.plot(li, m1)
    plt.title("Moment Diagram")
    plt.xlabel("Distance")
    plt.ylabel("Moment")
    plt.show()


# Create Button
submit_button = ttk.Button(win, text="Submit", command=maxmoment)
submit_button.grid(row=3, column=0)



win.mainloop()
