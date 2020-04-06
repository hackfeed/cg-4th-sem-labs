"""
    Interface viewset module.
"""

import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np
import colorutils as cu
from tkinter import messagebox
from math import cos, sin, radians
from circledraw import canonical as ccan, parametric as cpar, bresenham as cbres, midpoint as cmid

from view import util


def check_shape(root):
    """
        Check if circle or ellipse is chosen.
    """

    try:
        shape_ind = root.shapelst.curselection()[0]
        shape = root.shapelst.get(shape_ind)
    except (IndexError, UnboundLocalError):
        pass

    if shape == "Окружность":
        root.r2sb.configure(state="disabled")
    else:
        root.r2sb.configure(state="normal")


def enable_btns(root):
    """
        Enable draw and drawbunch buttons.
    """

    root.drawbtn.config(state="normal")
    root.drawspectrebtn.config(state="normal")


def disable_btns(root):
    """
        Enable draw and drawbunch buttons.
    """

    root.drawbtn.config(state="disabled")
    root.drawspectrebtn.config(state="disabled")


def clear_selection(root):
    """
        Clear listboxes selection.
    """

    root.shapelst.selection_clear(0, "end")
    root.methodlst.selection_clear(0, "end")
    root.colorlst.selection_clear(0, "end")


def check_lb(event, root):
    """
        Check if something is checked in the listbox.
    """

    shape_select = list(map(int, root.shapelst.curselection()))
    method_select = list(map(int, root.methodlst.curselection()))
    color_select = list(map(int, root.colorlst.curselection()))

    check_shape(root)

    if shape_select != [] and method_select != [] and color_select != []:
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

    shape_ind = root.shapelst.curselection()[0]
    shape = root.shapelst.get(shape_ind)

    method_ind = root.methodlst.curselection()[0]
    method = root.methodlst.get(method_ind)

    color_ind = root.colorlst.curselection()[0]
    color = root.colorlst.get(color_ind)

    dots = None
    x_center, y_center, r1, r2 = None, None, None, None
    color_cu = None

    try:
        x_center = int(root.xcentersb.get())
        y_center = int(root.ycentersb.get())
        r1 = int(root.r1sb.get())
        r2 = int(root.r2sb.get())
    except ValueError:
        messagebox.showerror(
            "Ошибка ввода", "Невозможно получить целое число. Проверьте корректность ввода.")

    if shape == "Окружность":
        r2 = r1

    if color == "Синий":
        color_cu = cu.Color((0, 0, 255))
    else:
        color_cu = cu.Color((255, 255, 255))

    if method == "Каноническое уравнение":
        func = ccan.cancircle
    elif method == "Параметрическое уравнение":
        func = cpar.parcircle
    elif method == "Алгоритм Брезенхема":
        func = cbres.brescircle
    elif method == "Алгоритм средней точки":
        func = cmid.midpcircle
    elif method == "Библиотечная функция":
        root.image.create_oval(x_center - r1, y_center - r2, x_center +
                               r1, y_center + r2, outline=color_cu.hex)
        return

    dots = func(x_center, y_center, r1, color_cu)
    print(dots)

    util.draw_line(root.image, dots)


def draw_bunch(root):
    try:
        radius = int(root.radsb.get())
        step = int(root.stepsb.get())
    except ValueError:
        messagebox.showerror(
            "Ошибка ввода", "Невозможно получить число. Проверьте корректность ввода.")
        return

    # root.image.delete("all")

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
        func = bresenham.bresenham_antialiased
    elif method == "Ву":
        func = wu.wu
    elif method == "Библиотечная функция":
        func = root.image.create_line

    for _ in range(1, lines):
        x_s = x_rotate + (y_start - y_rotate) * sin(radians(step))
        x_e = x_rotate + (y_end - y_rotate) * sin(radians(step))
        y_s = y_rotate + (y_start - y_rotate) * cos(radians(step))
        y_e = y_rotate + (y_end - y_rotate) * cos(radians(step))
        step += fixed_step

        dots.append((int(x_s), int(y_s), int(x_e), int(y_e)))

    for pair in dots:
        if func == root.image.create_line:
            func(pair[0], pair[1], pair[2], pair[3], fill=color_cu.hex)
        else:
            ds = func(pair[0], pair[1], pair[2], pair[3], color_cu)
            util.draw_line(root.image, ds)


def compare_algos(canvas):
    """
        Show diagram with time measurements.
    """

    plt.rcParams["toolbar"] = "None"

    taken_time = util.get_time(canvas)

    objects = list(taken_time.keys())
    performance = list(taken_time.values())

    y_pos = np.arange(len(objects))

    mng = plt.get_current_fig_manager()
    mng.window.showMaximized()

    plt.bar(y_pos, performance, align="center", alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel("Затраченное время, единицы времени")
    plt.title("Временная характеристика алгоритмов построения отрезков")

    plt.show()
