"""
    Triangle viewset module.
"""

import tkinter as tk
from tkinter import messagebox


def dot(dotwindow, root, mode):
    try:
        xcoord = float(dotwindow.xentry.get())
        ycoord = float(dotwindow.yentry.get())
        if mode == 1:
            ind = root.dotslist.curselection()
            root.dotslist.delete(ind[0])
            root.dotslist.insert(ind, f"{xcoord};{ycoord}")
            dotwindow.destroy()
            disable_btns(root)
        else:
            root.dotslist.insert(tk.END, f"{xcoord};{ycoord}")
            disable_btns(root)
    except ValueError:
        messagebox.showerror("Input error", "Can't get float data. Check ypur input.")


def disable_btns(root):
    root.delbtn.configure(state="disabled")
    root.editbtn.configure(state="disabled")


def enable_btns(root):
    root.delbtn.configure(state="normal")
    root.editbtn.configure(state="normal")


def check_lb(event, root, listbox):
    if list(map(int, listbox.curselection())) != []:
        enable_btns(root)


def del_dot(root):
    root.dotslist.delete(tk.ANCHOR)
    disable_btns(root)


def clean_scr(root):
    root.dotslist.delete(0, tk.END)
    root.image.delete("all")
    disable_btns(root)


def draw_triangle(root, trcoords, trparts):
    winx = 800
    winy = 600

    xmax = trcoords[0][0]
    xmin = trcoords[0][0]

    ymax = trcoords[0][1]
    ymin = trcoords[0][1]

    for dot in trcoords:
        if dot[0] > xmax:
            xmax = dot[0]
        if dot[0] < xmin:
            xmin = dot[0]
        if dot[1] > ymax:
            ymax = dot[1]
        if dot[1] < ymin:
            ymin = dot[1]

    scalex = (winx - 20) / (xmax - xmin)
    scaley = (winy - 20) / (ymax - ymin)

    offsetx = -xmin * scalex + 10
    offsety = -ymin * scaley + 10

    result_draw = list()

    for i in range(len(result_set)):
        x_cord = result_set[i][0] * scalex + offsetx
        result_draw.append(x_cord)
        y_cord = winy - (result_set[i][1] * scaley + offsety)
        result_draw.append(y_cord)

    draw_canvas.create_line(*result_draw, result_draw[0], result_draw[1],
                            width=4, fill="blue")
