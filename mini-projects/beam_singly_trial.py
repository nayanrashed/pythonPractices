import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math
import tkinter as tk
from tkinter import ttk
from tkinter import Canvas

win = tk.Tk()
win.title("Beam Design(singly) v1.0.1")

frame = tk.LabelFrame(win, text="INPUT DATA", padx=5, pady=5)
frame.grid(row=0, column=0)


# labels A
label0 = tk.Label(frame, text="Beam Geometry", font="arial", fg="red")
label0.grid(row=0, column=0)
label1 = tk.Label(frame, text="Beam ID")
label1.grid(row=1, column=0, sticky=tk.W)

label2 = tk.Label(frame, text="Beam Span/Length in ft:")
label2.grid(row=2, column=0, sticky=tk.W)
label3 = tk.Label(frame, text="Beam Width(b) in inch:")
label3.grid(row=3, column=0, sticky=tk.W)
label4 = tk.Label(frame, text="Beam Height(h) in inch:")
label4.grid(row=4, column=0, sticky=tk.W)
label5 = tk.Label(frame, text="Loaded Area in sft:")
label5.grid(row=5, column=0, sticky=tk.W)

# Entry box A
bid_var = tk.StringVar()
bid_ebox = tk.Entry(frame, width=5, textvariable=bid_var)
bid_ebox.grid(row=1, column=1)

l_var = tk.StringVar()
l_ebox = tk.Entry(frame, width=5, textvariable=l_var)
l_ebox.grid(row=2, column=1)
l_ebox.focus()

b_var = tk.StringVar()
b_ebox = tk.Entry(frame, width=5, textvariable=b_var)
b_ebox.grid(row=3, column=1)
h_var = tk.StringVar()
h_ebox = tk.Entry(frame, width=5, textvariable=h_var)
h_ebox.grid(row=4, column=1)

a_var = tk.StringVar()
a_ebox = tk.Entry(frame, width=5, textvariable=a_var)
a_ebox.grid(row=5, column=1)

# labels B
label6 = tk.Label(frame, text="Loading Data", font="arial", fg="red")
label6.grid(row=6, column=0)

label7 = tk.Label(frame, text="Wall (length, width, height in ft):")
label7.grid(row=7, column=0, sticky=tk.W)
label8 = tk.Label(frame, text="Slab Thickness(inch):")
label8.grid(row=8, column=0, sticky=tk.W)
label9 = tk.Label(frame, text="Floor Finish(psf):")
label9.grid(row=9, column=0, sticky=tk.W)
label10 = tk.Label(frame, text="Partition Wall Load(psf):")
label10.grid(row=10, column=0, sticky=tk.W)
label11 = tk.Label(frame, text="live Load(psf):")
label11.grid(row=11, column=0, sticky=tk.W)
label12 = tk.Label(frame, text="Wall Load(psf):")
label12.grid(row=12, column=0, sticky=tk.W)
label13 = tk.Label(frame, text="Weight of Slab(psf):")
label13.grid(row=13, column=0, sticky=tk.W)
label14 = tk.Label(frame, text="Total Dead Load(psf):")
label14.grid(row=14, column=0, sticky=tk.W)
label15 = tk.Label(frame, text="Self weight of Beam(plf):")
label15.grid(row=15, column=0, sticky=tk.W)

# Entry box B
walll_var = tk.StringVar()
walll_ebox = tk.Entry(frame, width=5, textvariable=walll_var)
walll_ebox.grid(row=7, column=1)
wallw_var = tk.StringVar()
wallw_ebox = tk.Entry(frame, width=5, textvariable=wallw_var)
wallw_ebox.grid(row=7, column=2)
wallh_var = tk.StringVar()
wallh_ebox = tk.Entry(frame, width=5, textvariable=wallh_var)
wallh_ebox.grid(row=7, column=3)

slab_var = tk.StringVar()
slab_ebox = tk.Entry(frame, width=5, textvariable=slab_var)
slab_ebox.grid(row=8, column=1)

ff_var = tk.StringVar()
ff_ebox = tk.Entry(frame, width=5, textvariable=ff_var)
ff_ebox.grid(row=9, column=4)

pwl_var = tk.StringVar()
pwl_ebox = tk.Entry(frame, width=5, textvariable=pwl_var)
pwl_ebox.grid(row=10, column=4)

ll_var = tk.StringVar()
ll_ebox = tk.Entry(frame, width=5, textvariable=ll_var)
ll_ebox.grid(row=11, column=4)

wall_load = tk.StringVar()
label14 = tk.Label(frame, text="wall_load", textvariable=wall_load)
label14.grid(row=12, column=4)

slab_load = tk.StringVar()
label15 = tk.Label(frame, text="slab_load", textvariable=slab_load)
label15.grid(row=13, column=4)

tdead_load = tk.StringVar()
label17 = tk.Label(frame, text="self wt. Beam_load", textvariable=tdead_load)
label17.grid(row=14, column=4)

swtb_load = tk.StringVar()
label16 = tk.Label(frame, text="self wt. Beam_load", textvariable=swtb_load)
label16.grid(row=15, column=4)


def LoadCal():
    bid = bid_var.get()
    l = float(l_var.get())
    b = float(b_var.get())
    h = float(h_var.get())
    a = float(a_var.get())
    ll = float(ll_var.get())
    sl_t = float(slab_var.get())
    ff = float(ff_var.get())
    pwl = float(pwl_var.get())

    d = h - 2.5

    wl = float(walll_var.get())
    ww = float(wallw_var.get())
    wh = float(wallh_var.get())
    wl_load = (wl * ww * wh * 120) / a
    wallload = round(wl_load,3)
    wall_load.set(wallload)

    sl_load = (sl_t / 12) * 150
    slload = round(sl_load,3)
    slab_load.set(slload)

    swb = (((b * h) / 144) * l * 150) / l
    swtbload = round(swb,3)
    swtb_load.set(swtbload)

    tdl = sl_load + ff + pwl + wl_load
    tdeadload= round(tdl,3)
    tdead_load.set(tdeadload)

     # for Design data
    tdl1 = (tdl*a)/(l*1000)+(swb/1000)
    tdl1load = round(tdl1,3)
    tdl1_load.set(tdl1load)

    ll1 = (ll*a)/(l*1000)
    ll1load = round(ll1,3)
    ll1_load.set(ll1load)

    w = 1.4 * tdl1 + 1.7 * ll1
    wload = round(w,3)
    w_load.set(wload)
    return w, l, h, d, b

submit_button = ttk.Button(frame, text="Calculate Load", command=LoadCal)
submit_button.grid(row=16, column=0)

#Design Data

frame2 = tk.LabelFrame(win, text="DESIGN DATA", padx=10, pady=10)
frame2.grid(row=1, column=0)

labeltdl = tk.Label(frame2, text="Total Dead Load on Beam:")
labeltdl.grid(row=0, column=0, sticky=tk.W)
labeltll = tk.Label(frame2, text="Total Live Load on Beam:")
labeltll.grid(row=1, column=0, sticky=tk.W)
labellf = tk.Label(frame2, text="Load Factor:")
labellf.grid(row=2, column=0)
labelw = tk.Label(frame2, text="Design (Factored) Load (w):")
labelw.grid(row=3, column=0, sticky=tk.W)

Fy = tk.Label(frame2, text="Fy in ksi:")
Fy.grid(row=4, column=0, sticky=tk.W)
Fc = tk.Label(frame2, text="Fc in ksi:")
Fc.grid(row=5, column=0, sticky=tk.W)

Fy_var = tk.StringVar()
Fy_ebox = tk.Entry(frame2, width=5, textvariable=Fy_var)
Fy_ebox.grid(row=4, column=1)

Fc_var = tk.StringVar()
Fc_ebox = tk.Entry(frame2, width=5, textvariable=Fc_var)
Fc_ebox.grid(row=5, column=1)

tdl1_load = tk.StringVar()
labeltdl1 = tk.Label(frame2, text="tdl_load", textvariable=tdl1_load)
labeltdl1.grid(row=0, column=1)

ll1_load = tk.StringVar()
labelll1 = tk.Label(frame2, text="ll1_load", textvariable=ll1_load)
labelll1.grid(row=1, column=1)


labellf1 = tk.Label(frame2, text="1.4*DL + 1.7*LL")
labellf1.grid(row=2, column=1)

w_load = tk.StringVar()
labelw1 = tk.Label(frame2, text="Design Load", textvariable=w_load)
labelw1.grid(row=3, column=1)


def beamdesign():
    w, l, h, d, b = LoadCal()
    fy = float(Fy_var.get())
    fc = float(Fc_var.get())

    moment_de = (w * l * l) / 16
    moment_ce = (w * l * l) / 9
    moment_mspan = (w * l * l) / 14

    a1 = h/8
    As1 = (moment_de * 12) / (.9 * fy * (d - a1 / 2))
    a2 = (As1 * fy) / (.85 * fc * b)
    mdeAs = (moment_de * 12) / (.9 * fy * (d - a2/2))
    dend_as.set(mdeAs)


    As2 = (moment_ce * 12) / (.9 * fy * (d - a1 / 2))
    a3 = (As2 * fy) / (.85 * fc * b)
    mceAs = (moment_ce * 12) / (.9 * fy * (d - a3 / 2))
    #mceAs1=round(mceAs,3)
    cend_as.set(mceAs)


    As3 = (moment_mspan * 12) / (.9 * fy * (d - a1 / 2))
    a4 = (As3 * fy) / (.85 * fc * b)
    mmsAs = (moment_mspan * 12) / (.9 * fy * (d - a4 / 2))
    #mmsAs1=round(mmsAs,3)
    mspan_as.set(mmsAs)

    return mdeAs, mceAs, mmsAs



submit_button = ttk.Button(frame2, text="Design Beam", command=beamdesign)
submit_button.grid(row=6, column=0)

#Output

frame3 = tk.LabelFrame(win, text="OUTPUT", padx=5, pady=5)
frame3.grid(row=0, column=1)

labelout1 = tk.Label(frame3, text="Rebar Zone")
labelout1.grid(row=0, column=0)
labelout2 = tk.Label(frame3, text="Rebar Area(As)")
labelout2.grid(row=0, column=1)
labelout3 = tk.Label(frame3, text="Rebar Dia")
labelout3.grid(row=0, column=2)
labelout4 = tk.Label(frame3, text="Number of Rebar")
labelout4.grid(row=0, column=4)

dend = tk.Label(frame3, text="Rebar at Discontinuous End(in^2):")
dend.grid(row=1, column=0, sticky=tk.W)
dend_as = tk.StringVar()
labeldend = tk.Label(frame3, text="Design As dend", textvariable=dend_as)
labeldend.grid(row=1, column=1)

cend = tk.Label(frame3, text="Rebar at Continuous End(in^2):")
cend.grid(row=2, column=0, sticky=tk.W)
cend_as = tk.StringVar()
labelcend = tk.Label(frame3, text="Design As cend", textvariable = cend_as)
labelcend.grid(row=2, column=1)

mspan = tk.Label(frame3, text="Rebar at Mid Span(in^2):")
mspan.grid(row=3, column=0, sticky=tk.W)
mspan_as = tk.StringVar()
labelmspan = tk.Label(frame3, text="Design As mid span", textvariable = mspan_as)
labelmspan.grid(row=3, column=1)

Asnos1 = tk.StringVar()
labelAs1 = tk.Label(frame3, text="Design As mid span", textvariable = Asnos1)
labelAs1.grid(row=1, column=4)

Asnos2 = tk.StringVar()
labelAs2 = tk.Label(frame3, text="Design As mid span", textvariable = Asnos2)
labelAs2.grid(row=2, column=4)

Asnos3 = tk.StringVar()
labelAs3 = tk.Label(frame3, text="Design As mid span", textvariable = Asnos3)
labelAs3.grid(row=3, column=4)

#function for rebar presentation beam1
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

#combo box 01

def selected1():
    mdeAs, mceAs, mmeAs = beamdesign()
    mdeas = float(mdeAs)
    if clicked1.get() == "10 mm":
        As1 = math.ceil(mdeas/.11)
    elif clicked1.get() == "12 mm":
        As1 = math.ceil(mdeas//.2)
    elif clicked1.get() == "16 mm":
        As1 = math.ceil(mdeas / .31)
    elif clicked1.get() == "20 mm":
        As1 = math.ceil(mdeas / .44)
    elif clicked1.get() == "22 mm":
        As1 = math.ceil(mdeas / .6)
    elif clicked1.get() == "25 mm":
        As1 = math.ceil(mdeas / .79)
    elif clicked1.get() == "28 mm":
        As1 = math.ceil(mdeas / 1)
    else:
        As1 = math.ceil(mdeas / 1.27)
    Asnos1.set(As1)
    bars1 = int(As1)
    if bars1 == 2 or As1 < 2:
        btop12()
    elif bars1 == 3:
        btop13()
    elif bars1 == 4:
        btop14()
    elif bars1 == 5:
        btop15()
    else:
        btop16()

rebar_dia1 = ["10 mm", "12 mm", "16 mm", "20 mm", "22 mm", "25 mm", "28 mm", "32 mm"]

clicked1 = tk.StringVar()
clicked1.set(rebar_dia1[0])

drop1 = ttk.OptionMenu(frame3, clicked1, *rebar_dia1)
drop1.grid(row=1, column=2)

button1 = ttk.Button(frame3, text="Bars", command=selected1)
button1.grid(row=1, column=3)

#function for rebar presentation beam1
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

#combo box 02
def selected2():
    mdeAs, mceAs, mmeAs = beamdesign()
    mceas = float(mceAs)
    if clicked2.get() == "10 mm":
        As2 = math.ceil(mceas/.11)
    elif clicked2.get() == "12 mm":
        As2 = math.ceil(mceas//.2)
    elif clicked2.get() == "16 mm":
        As2 = math.ceil(mceas / .31)
    elif clicked2.get() == "20 mm":
        As2 = math.ceil(mceas / .44)
    elif clicked2.get() == "22 mm":
        As2 = math.ceil(mceas / .6)
    elif clicked2.get() == "25 mm":
        As2 = math.ceil(mceas / .79)
    elif clicked2.get() == "28 mm":
        As2 = math.ceil(mceas / 1)
    else:
        As2 = math.ceil(mceas / 1.27)
    Asnos2.set(As2)
    bars2 = int(As2)
    if bars2 == 2 or As2 < 2:
        btop22()
    elif bars2 == 3:
        btop23()
    elif bars2 == 4:
        btop24()
    elif bars2 == 5:
        btop25()
    else:
        btop26()


rebar_dia2 = ["10 mm", "12 mm", "16 mm", "20 mm", "22 mm", "25 mm", "28 mm", "32 mm"]

clicked2 = tk.StringVar()
clicked2.set(rebar_dia2[0])

drop2 = ttk.OptionMenu(frame3, clicked2, *rebar_dia2)
drop2.grid(row=2, column=2)

button2 = ttk.Button(frame3, text="Bars", command=selected2)
button2.grid(row=2, column=3)

#function for rebar presentation beam1
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



#combo box 03
def selected3():
    mdeAs, mceAs, mmeAs = beamdesign()
    mmeas = float(mmeAs)
    if clicked3.get() == "10 mm":
        As3 = math.ceil(mmeas/.11)
    elif clicked3.get() == "12 mm":
        As3 = math.ceil(mmeas//.2)
    elif clicked3.get() == "16 mm":
        As3 = math.ceil(mmeas / .31)
    elif clicked3.get() == "20 mm":
        As3 = math.ceil(mmeas / .44)
    elif clicked3.get() == "22 mm":
        As3 = math.ceil(mmeas / .6)
    elif clicked3.get() == "25 mm":
        As3 = math.ceil(mmeas / .79)
    elif clicked3.get() == "28 mm":
        As3 = math.ceil(mmeas / 1)
    else:
        As3 = math.ceil(mmeas / 1.27)
    Asnos3.set(As3)
    bars3 = int(As3)
    if bars3 == 2 or As3 < 2:
        btop32()
    elif bars3 == 3:
        btop33()
    elif bars3 == 4:
        btop34()
    elif bars3 == 5:
        btop35()
    else:
        btop36()

rebar_dia3 = ["10 mm", "12 mm", "16 mm", "20 mm", "22 mm", "25 mm", "28 mm", "32 mm"]

clicked3 = tk.StringVar()
clicked3.set(rebar_dia3[0])

drop3 = ttk.OptionMenu(frame3, clicked3, *rebar_dia3)
drop3.grid(row=3, column=2)

button3 = ttk.Button(frame3, text="Bars", command=selected3)
button3.grid(row=3, column=3)



# Grafical Presentation

frame1 = tk.LabelFrame(win, text="Beam Section", padx=5, pady=5)
frame1.grid(row=1, column=1)

beam1 = Canvas(frame1, width=150, height=230, bg="white")
beam1.grid(row=17, column=5)
label_beam1 = tk.Label(frame1, text="Reabar at Discontinuous End(Top)")
label_beam1.grid(row=18, column=5)
beam1.create_rectangle(15, 15, 135, 215, fill="yellow")
beam1.create_rectangle(25, 25, 125, 205, fill="blue")

beam2 = Canvas(frame1, width=150, height=230, bg="white")
beam2.grid(row=17, column=6)
label_beam2 = tk.Label(frame1, text="Reabar at Continuous End(Top)")
label_beam2.grid(row=18, column=6)
beam2.create_rectangle(15, 15, 135, 215, fill="yellow")
beam2.create_rectangle(25, 25, 125, 205, fill="blue")

beam3 = Canvas(frame1, width=150, height=230, bg="white")
beam3.grid(row=17, column=7)
label_beam3 = tk.Label(frame1, text="Rebar at Mid Span(Bottom)")
label_beam3.grid(row=18, column=7)
beam3.create_rectangle(15, 15, 135, 215, fill="yellow")
beam3.create_rectangle(25, 25, 125, 205, fill="blue")


win.mainloop()