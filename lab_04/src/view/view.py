"""
    Interface viewset module.
"""

import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np
import colorutils as cu
from tkinter import messagebox
from math import cos, sin, radians
from circledraw import canonical, parametric, bresenham, midpoint

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
    func = None

    try:
        x_center = int(root.xcentersb.get())
        y_center = int(root.ycentersb.get())
        r1 = int(root.r1sb.get())
        r2 = int(root.r2sb.get())
    except ValueError:
        messagebox.showerror(
            "Ошибка ввода", "Невозможно получить целое число. Проверьте корректность ввода.")

    if color == "Синий":
        color_cu = cu.Color((0, 0, 255))
    else:
        color_cu = cu.Color((255, 255, 255))

    if shape == "Окружность":
        r2 = r1

        if method == "Каноническое уравнение":
            func = canonical.cancircle
        elif method == "Параметрическое уравнение":
            func = parametric.parcircle
        elif method == "Алгоритм Брезенхема":
            func = bresenham.brescircle
        elif method == "Алгоритм средней точки":
            func = midpoint.midpcircle
        elif method == "Библиотечная функция":
            root.image.create_oval(x_center - r1, y_center - r2, x_center +
                                   r1, y_center + r2, outline=color_cu.hex)
            return

        dots = func(x_center, y_center, r1, color_cu)
    else:
        if method == "Каноническое уравнение":
            func = canonical.canellipse
        elif method == "Параметрическое уравнение":
            func = parametric.parellipse
        elif method == "Алгоритм Брезенхема":
            func = bresenham.bresellipse
        elif method == "Алгоритм средней точки":
            func = midpoint.midpellipse
        elif method == "Библиотечная функция":
            root.image.create_oval(x_center - r1, y_center - r2, x_center +
                                   r1, y_center + r2, outline=color_cu.hex)
            return

        dots = func(x_center, y_center, r1, r2, color_cu)

    util.draw_line(root.image, dots)


def draw_spectre(root):
    try:
        rs1 = int(root.rs1sb.get())
        rs2 = int(root.rs2sb.get())
        x_center = int(root.xscentersb.get())
        y_center = int(root.yscentersb.get())
        step = int(root.stepsb.get())
        n = int(root.nsb.get())
    except ValueError:
        messagebox.showerror(
            "Ошибка ввода", "Невозможно получить число. Проверьте корректность ввода.")
        return

    # root.image.delete("all")

    color_cu = None
    func = None

    shape_ind = root.shapelst.curselection()[0]
    shape = root.shapelst.get(shape_ind)

    method_ind = root.methodlst.curselection()[0]
    method = root.methodlst.get(method_ind)

    color_ind = root.colorlst.curselection()[0]
    color = root.colorlst.get(color_ind)

    if color == "Синий":
        color_cu = cu.Color((0, 0, 255))
    else:
        color_cu = cu.Color((255, 255, 255))

    if shape == "Окружность":
        if method == "Каноническое уравнение":
            func = canonical.cancircle
        elif method == "Параметрическое уравнение":
            func = parametric.parcircle
        elif method == "Алгоритм Брезенхема":
            func = bresenham.brescircle
        elif method == "Алгоритм средней точки":
            func = midpoint.midpcircle
        elif method == "Библиотечная функция":
            func = root.image.create_oval

        if rs1 == 0:
            rs1 = rs2 - step * n
        if rs2 == 0:
            rs2 = rs1 + step * n
        if step == 0:
            step = (rs2 - rs1) // n

        for radius in range(rs1, rs2, step):
            if func == root.image.create_oval:
                func(x_center - radius,
                     y_center - radius,
                     x_center + radius,
                     y_center + radius,
                     outline=color_cu.hex)
            else:
                dots = func(x_center, y_center, radius, color_cu)
                util.draw_line(root.image, dots)

        return

    if method == "Каноническое уравнение":
        func = canonical.canellipse
    elif method == "Параметрическое уравнение":
        func = parametric.parellipse
    elif method == "Алгоритм Брезенхема":
        func = bresenham.bresellipse
    elif method == "Алгоритм средней точки":
        func = midpoint.midpellipse
    elif method == "Библиотечная функция":
        func = root.image.create_oval

    for _ in range(n):
        if func == root.image.create_oval:
            func(x_center - rs1,
                 y_center - rs2,
                 x_center + rs1,
                 y_center + rs2,
                 outline=color_cu.hex)
        else:
            dots = func(x_center, y_center, rs1, rs2, color_cu)
            util.draw_line(root.image, dots)

        rs1 += step
        rs2 += step


def compare_algos(canvas):
    """
        Show diagram with time measurements.
    """

    plt.rcParams["toolbar"] = "None"

    taken_time, radiuses = util.get_time(canvas)

    plt.title("Сравнение алгоритмов")

    mng = plt.get_current_fig_manager()
    mng.window.showMaximized()

    for method in taken_time:
        plt.plot(radiuses, taken_time[method][0], label=method)

    plt.legend()

    plt.ylabel("Затраченное время, единицы времени")
    plt.title("Временная характеристика алгоритмов построения окружностей")

    plt.grid()
    plt.show()
