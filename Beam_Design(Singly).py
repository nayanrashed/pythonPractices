import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import tkinter as tk
from tkinter import ttk
from tkinter import Canvas
win = tk.Tk()
frame = tk.LabelFrame(win, text=" Input Data", padx=5, pady=5)
frame.grid

win.title("Beam Design(singly) v1.0.1")

#labels A
label0 = tk.Label(win, text="Input data")
label0.grid(row=0, column=0)
label1 = tk.Label(win, text="Beam Geometry")
label1.grid(row=1, column=0)

label2 = tk.Label(win, text="Beam Span/Length(l, ft) in ft:")
label2.grid(row=2, column=0)
label3 = tk.Label(win, text="Beam Width(b) in ft:")
label3.grid(row=3, column=0)
label4 = tk.Label(win, text="Beam Height(h) in ft:")
label4.grid(row=4, column=0)
label5 = tk.Label(win, text="Loaded Area in sft:")
label5.grid(row=5, column=0)

#Entry box A
l_var = tk.StringVar()
l_ebox = tk.Entry(win, width=7, textvariable = l_var)
l_ebox.grid(row=2, column=1)

b_var = tk.StringVar()
b_ebox = tk.Entry(win, width=7, textvariable = b_var)
b_ebox.grid(row=3, column=1)

h_var = tk.StringVar()
h_ebox = tk.Entry(win, width=7, textvariable = h_var)
h_ebox.grid(row=4, column=1)

a_var = tk.StringVar()
a_ebox = tk.Entry(win, width=7, textvariable = a_var)
a_ebox.grid(row=5, column=1)

#labels B
label6 = tk.Label(win, text="Loading Data")
label6.grid(row=6, column=0)

label7 = tk.Label(win, text="Wall (length, width, height in ft):")
label7.grid(row=7, column=0)
label8 = tk.Label(win, text="Slab Thickness(psf):")
label8.grid(row=8, column=0)
label9 = tk.Label(win, text="Floor Finish(psf):")
label9.grid(row=9, column=0)
label10 = tk.Label(win, text="Partition Wall Load(psf):")
label10.grid(row=10, column=0)
label11 = tk.Label(win, text="live Load(psf):")
label11.grid(row=11, column=0)
label12= tk.Label(win, text="Wall Load(psf):")
label12.grid(row=12, column=0)
label13 = tk.Label(win, text="Weight of Slab(psf):")
label13.grid(row=13, column=0)
label14 = tk.Label(win, text="Total Dead Load(psf):")
label14.grid(row=14, column=0)
label15 = tk.Label(win, text="Self weight of Beam(plf):")
label15.grid(row=15, column=0)


#Entry box B
walll_var = tk.StringVar()
walll_ebox = tk.Entry(win, width=7, textvariable = walll_var)
walll_ebox.grid(row=7, column=1)
wallw_var = tk.StringVar()
wallw_ebox = tk.Entry(win, width=7, textvariable = wallw_var)
wallw_ebox.grid(row=7, column=2)
wallh_var = tk.StringVar()
wallh_ebox = tk.Entry(win, width=7, textvariable = wallh_var)
wallh_ebox.grid(row=7, column=3)

slab_var = tk.StringVar()
slab_ebox = tk.Entry(win, width=7, textvariable = slab_var)
slab_ebox.grid(row=8, column=1)

ff_var = tk.StringVar()
ff_ebox = tk.Entry(win, width=7, textvariable = ff_var)
ff_ebox.grid(row=9, column=4)

pwl_var = tk.StringVar()
pwl_ebox = tk.Entry(win, width=7, textvariable = pwl_var)
pwl_ebox.grid(row=10, column=4)

ll_var = tk.StringVar()
ll_ebox = tk.Entry(win, width=7, textvariable = ll_var)
ll_ebox.grid(row=11, column=4)

wall_load = tk.StringVar()
label14 = tk.Label(win, text="wall_load", textvariable = wall_load )
label14.grid(row=12, column=4)

slab_load = tk.StringVar()
label15 = tk.Label(win, text="slab_load", textvariable = slab_load )
label15.grid(row=13, column=4)

tdead_load = tk.StringVar()
label17 = tk.Label(win, text="self wt. Beam_load", textvariable = tdead_load )
label17.grid(row=14, column=4)

swtb_load = tk.StringVar()
label16 = tk.Label(win, text="self wt. Beam_load", textvariable = swtb_load )
label16.grid(row=15, column=4)



def LoadCal():
    l = float(l_var.get())
    b = float(b_var.get())
    h = float(h_var.get())
    a = float(a_var.get())
    ll = float(ll_var.get())
    sl_t = float(slab_var.get())
    ff = float(ff_var.get())
    pwl = float(pwl_var.get())

    d = h-2.5

    wl = float(walll_var.get())
    ww = float(wallw_var.get())
    wh = float(wallh_var.get())
    wl_load = (wl * ww * wh*120)/a

    wall_load.set(wl_load)

    sl_load = (sl_t/12)*150
    slab_load.set(sl_load)

    swb = (((b*h)/144)*l*150)/l
    swtb_load.set(swb)

    tdl = sl_load+ff+pwl+wl_load
    tdead_load.set(tdl)
    


submit_button = ttk.Button(win, text="Calculate Load", command=LoadCal)
submit_button.grid(row=16, column=0)

#Grafical Presentation


beam1 = Canvas(win, width=150, height=230, bg="white")
beam1.grid(row=17, column=5)
label_beam1 = tk.Label(win, text="Reabar at Discontinuous End(Top)")
label_beam1.grid(row=18, column=5)

beam1.create_rectangle(15,15,135,215, fill="yellow")
beam1.create_rectangle(25,25,125,205, fill="blue")
beam1.create_oval(25,25,40,40, fill= "red")
beam1.create_oval(68,25,83,40, fill= "red")
beam1.create_oval(110,25,125,40, fill= "red")
beam1.create_oval(25,50,40,65, fill= "red")
beam1.create_oval(68,50,83,65, fill= "red")
beam1.create_oval(110,50,125,65, fill= "red")


beam2 = Canvas(win, width=150, height=230, bg="white")
beam2.grid(row=17, column=6)
label_beam2 = tk.Label(win, text="Reabar at Continuous End(Top)")
label_beam2.grid(row=18, column=6)
beam2.create_rectangle(15,15,135,215, fill="yellow")
beam2.create_rectangle(25,25,125,205, fill="blue")
beam2.create_oval(25,25,40,40, fill= "red")
beam2.create_oval(68,25,83,40, fill= "red")
beam2.create_oval(110,25,125,40, fill= "red")
beam2.create_oval(25,50,40,65, fill= "red")
beam2.create_oval(68,50,83,65, fill= "red")
beam2.create_oval(110,50,125,65, fill= "red")

beam3 = Canvas(win, width=150, height=230, bg="white")
beam3.grid(row=17, column=7)
label_beam3 = tk.Label(win, text="Rebar at Midlle Portion(Bottom)")
label_beam3.grid(row=18, column=7)
beam3.create_rectangle(15,15,135,215, fill="yellow")
beam3.create_rectangle(25,25,125,205, fill="blue")
beam3.create_oval(25,190,40,205, fill= "red")
beam3.create_oval(68,190,83,205, fill= "red")
beam3.create_oval(110,190,125,205, fill= "red")
beam3.create_oval(25,165,40,180, fill= "red")
beam3.create_oval(68,165,83,180, fill= "red")
beam3.create_oval(110,165,125,180, fill= "red")

win.mainloop()