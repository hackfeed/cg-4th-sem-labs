"""
    Triangle viewset module.
"""

import tkinter as tk
from tkinter import messagebox
from trgeom import geom


def disable_btns(root):
    root.delbtn.configure(state="disabled")
    root.editbtn.configure(state="disabled")


def enable_btns(root):
    root.delbtn.configure(state="normal")
    root.editbtn.configure(state="normal")


def clean_scr(root):
    root.dotslist.delete(0, tk.END)
    root.image.delete("all")
    disable_btns(root)


def check_lb(event, root, listbox):
    if list(map(int, listbox.curselection())) != []:
        enable_btns(root)


def is_present(dot, root):
    raw = root.dotslist.get(0, tk.END)
    for item in raw:
        if dot == item:
            return True

    return False


def config_dot(dotwindow, root, mode, ind):
    try:
        xcoord = float(dotwindow.xentry.get())
        ycoord = float(dotwindow.yentry.get())
        dot = f"{xcoord};{ycoord}"
        if is_present(dot, root):
            messagebox.showinfo("Dot info", "Dot already exists")
            return
        if mode == 1:
            root.dotslist.delete(ind)
            root.dotslist.insert(ind, dot)
            dotwindow.destroy()
            disable_btns(root)
        else:
            root.dotslist.insert(tk.END, dot)
            disable_btns(root)
    except ValueError:
        messagebox.showerror("Input error", "Can't get float data. Check ypur input.")


def del_dot(root):
    root.dotslist.delete(tk.ANCHOR)
    disable_btns(root)


def get_dots(root):
    raw = root.dotslist.get(0, tk.END)
    items = []
    for item in raw:
        items.append(list(map(float, item.split(";"))))

    return items


def draw_triangle(root):
    root.image.delete("all")
    dots = get_dots(root)
    solution = geom.find_solution(dots)
    trcoords = solution[0]

    winx = 580
    winy = 580

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

    scalex = (winx - 100) / (xmax - xmin)
    scaley = (winy - 100) / (ymax - ymin)

    scale = scalex if scalex < scaley else scaley

    offsetx = -xmin * scale + 50
    offsety = -ymin * scale + 50

    result_draw = []

    altitude_draw = [
        trcoords[0][0] * scale + offsetx,
        winy - (trcoords[0][1] * scale + offsety),
        solution[1][0] * scale + offsetx,
        winy - (solution[1][1] * scale + offsety)
    ]

    bisector_draw = [
        trcoords[0][0] * scale + offsetx,
        winy - (trcoords[0][1] * scale + offsety),
        solution[2][0] * scale + offsetx,
        winy - (solution[2][1] * scale + offsety)
    ]

    for dot in trcoords:
        x_cord = dot[0] * scale + offsetx
        result_draw.append(x_cord)
        y_cord = winy - (dot[1] * scale + offsety)
        result_draw.append(y_cord)
    result_draw.append(result_draw[0])
    result_draw.append(result_draw[1])

    root.image.create_line(*result_draw, width=4, fill="blue")
    root.image.create_line(*altitude_draw, width=4, fill="green")
    root.image.create_line(*bisector_draw, width=4, fill="red")
