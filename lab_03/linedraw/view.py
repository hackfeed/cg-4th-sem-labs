"""
    Interface viewset module.
"""

import colorutils as cu
import tkinter as tk
from tkinter import messagebox
from math import cos, sin, radians

from linedraw import bresenham, dda, wu, util


def enable_btns(root):
    """
        Enable draw and drawbunch buttons.
    """

    root.drawbtn.config(state="normal")
    root.drawbunchbtn.config(state="normal")


def disable_btns(root):
    """
        Enable draw and drawbunch buttons.
    """

    root.drawbtn.config(state="disabled")
    root.drawbunchbtn.config(state="disabled")


def clear_selection(root):
    """
        Clear listboxes selection.
    """

    root.methodlst.selection_clear(0, "end")
    root.colorlst.selection_clear(0, "end")


def check_lb(event, root):
    """
        Check if something is checked in the listbox.
    """

    method_select = list(map(int, root.methodlst.curselection()))
    color_select = list(map(int, root.colorlst.curselection()))

    if method_select != [] and color_select != []:
        enable_btns(root)


def reset(root):
    """
        Reset all fields to start state.
    """

    root.image.delete("all")
    disable_btns(root)
    clear_selection(root)


def draw(root):
    """
        Draw lines using different algorithms.
    """

    method_ind = root.methodlst.curselection()[0]
    method = root.methodlst.get(method_ind)

    color_ind = root.colorlst.curselection()[0]
    color = root.colorlst.get(color_ind)

    dots = None
    x_start, x_end, y_start, y_end = None, None, None, None
    color_cu = None

    try:
        x_start = int(root.xstartsb.get())
        y_start = int(root.ystartsb.get())
        x_end = int(root.xendsb.get())
        y_end = int(root.yendsb.get())
    except ValueError:
        messagebox.showerror(
            "Ошибка ввода", "Невозможно получить целое число. Проверьте корректность ввода.")

    if color == "Синий":
        color_cu = cu.Color((0, 0, 255))
    else:
        color_cu = cu.Color((255, 255, 255))

    if method == "ЦДА":
        func = dda.dda
    elif method == "Брезенхем (int)":
        func = bresenham.bresenham_int
    elif method == "Брезенхем (float)":
        func = bresenham.bresenham_db
    elif method == "Брезенхем (сглаживание)":
        pass
    elif method == "Ву":
        pass
    elif method == "Библиотечная функция":
        root.image.create_line(x_start, y_start, x_end, y_end, fill=color_cu.hex)

    dots = func(x_start, y_start, x_end, y_end, color_cu)
    util.draw_line(root.image, dots)


def draw_bunch(root):
    try:
        radius = int(root.radsb.get())
        step = int(root.stepsb.get())
    except ValueError:
        messagebox.showerror(
            "Ошибка ввода", "Невозможно получить число. Проверьте корректность ввода.")
        return

    root.image.delete("all")

    color_cu = None

    lines = 360 // step

    x_start = 420
    y_start = 340 - radius
    x_end = 420
    y_end = 340

    x_rotate = 420
    y_rotate = 340

    dots = [(x_start, y_start, x_end, y_end)]
    fixed_step = step

    method_ind = root.methodlst.curselection()[0]
    method = root.methodlst.get(method_ind)

    color_ind = root.colorlst.curselection()[0]
    color = root.colorlst.get(color_ind)

    if color == "Синий":
        color_cu = cu.Color((0, 0, 255))
    else:
        color_cu = cu.Color((255, 255, 255))

    if method == "ЦДА":
        func = dda.dda
    elif method == "Брезенхем (int)":
        func = bresenham.bresenham_int
    elif method == "Брезенхем (float)":
        func = bresenham.bresenham_db
    elif method == "Брезенхем (сглаживание)":
        pass
    elif method == "Ву":
        pass
    elif method == "Библиотечная функция":
        func = root.image.create_line

    for _ in range(1, lines):
        x_s = x_rotate + (y_start - y_rotate) * sin(radians(step))
        x_e = x_rotate + (y_end - y_rotate) * sin(radians(step))
        y_s = y_rotate + (y_start - y_rotate) * cos(radians(step))
        y_e = y_rotate + (y_end - y_rotate) * cos(radians(step))
        step += fixed_step

        dots.append((int(x_s), int(y_s), int(x_e), int(y_e)))

    print(dots)

    for pair in dots:
        print(pair)
        if func == root.image.create_line:
            func(pair[0], pair[1], pair[2], pair[3], fill=color_cu.hex)
        else:
            ds = func(pair[0], pair[1], pair[2], pair[3], color_cu)
            util.draw_line(root.image, ds)
