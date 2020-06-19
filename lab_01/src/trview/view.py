"""
    Triangle viewset module.
"""

import tkinter as tk
from tkinter import messagebox
import math
from trgeom import geom


def disable_btns(root):
    """
        Disable delete and edit buttons.
    """
    root.delbtn.configure(state="disabled")
    root.editbtn.configure(state="disabled")


def enable_btns(root):
    """
        Enable delete and edit buttons.
    """
    root.delbtn.configure(state="normal")
    root.editbtn.configure(state="normal")


def clean_scr(root):
    """
        Clean listbox and canvas from the root window.
    """
    root.dotslist.delete(0, tk.END)
    root.image.delete("all")
    disable_btns(root)


def check_lb(event, root, listbox):
    """
        Check if something is checked in the listbox.
    """
    if list(map(int, listbox.curselection())) != []:
        enable_btns(root)


def is_present(dot, root):
    """
        Check if dot is already in the listbox.
    """
    raw = root.dotslist.get(0, tk.END)
    for item in raw:
        if dot == item:
            return True

    return False


def config_dot(dotwindow, root, mode, ind):
    """
        Add or edit dot.
    """
    try:
        xcoord = float(dotwindow.xentry.get())
        ycoord = float(dotwindow.yentry.get())
        dot = f"{xcoord};{ycoord}"
        if is_present(dot, root):
            messagebox.showinfo("Информация о точке", "Такая точка уже существует")
            return
        if mode == 1:
            root.dotslist.delete(ind)
            root.dotslist.insert(ind, dot)
            dotwindow.destroy()
            disable_btns(root)
            root.image.delete("all")
        else:
            root.dotslist.insert(tk.END, dot)
            disable_btns(root)
            root.image.delete("all")
    except ValueError:
        messagebox.showerror(
            "Ошибка ввода", "Невозможно получить вещественное число. Проверьте корректность ввода.")


def del_dot(root):
    """
        Delete dot from the listbox.
    """
    root.dotslist.delete(tk.ANCHOR)
    disable_btns(root)
    root.image.delete("all")


def get_dots(root):
    """
        Get all dots from the listbox.
    """
    raw = root.dotslist.get(0, tk.END)
    items = []
    for item in raw:
        items.append(list(map(float, item.split(";"))))

    return items


def draw_triangle(root):
    """
        Draw flex triangle.
    """
    root.image.delete("all")
    dots = get_dots(root)
    solution = geom.find_solution(dots)

    if solution is None:
        messagebox.showinfo("Невозможно найти решение", "Для заданного набора точек невозможно "
                            "найти решение.")
        return

    trcoords = solution[0]  # .extend(solution)

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

    for i in range(1, 6, 2):
        if result_draw[i] == max(result_draw[1], result_draw[3], result_draw[5]):
            root.image.create_text(result_draw[i-1],
                                   result_draw[i] + 15,
                                   fill="black",
                                   font="-family {Consolas} -size 14",
                                   text=f"({trcoords[i // 2][0]};{trcoords[i // 2][1]})")
        elif result_draw[i] == min(result_draw[1], result_draw[3], result_draw[5]):
            root.image.create_text(result_draw[i-1],
                                   result_draw[i] - 15,
                                   fill="black",
                                   font="-family {Consolas} -size 14",
                                   text=f"({trcoords[i // 2][0]};{trcoords[i // 2][1]})")
        elif result_draw[i - 1] == max(result_draw[0], result_draw[2], result_draw[4]):
            root.image.create_text(result_draw[i-1] + 10,
                                   result_draw[i] + 15,
                                   fill="black",
                                   font="-family {Consolas} -size 14",
                                   text=f"({trcoords[i // 2][0]};{trcoords[i // 2][1]})")
        else:
            root.image.create_text(result_draw[i-1] - 10,
                                   result_draw[i] + 15,
                                   fill="black",
                                   font="-family {Consolas} -size 14",
                                   text=f"({trcoords[i // 2][0]};{trcoords[i // 2][1]})")
    root.image.create_line(*result_draw, width=4, fill="blue")
    root.image.create_line(*altitude_draw, width=4, fill="green")
    root.image.create_line(*bisector_draw, width=4, fill="red")
    messagebox.showinfo("Решение", "Координаты построенного треугольника "
                        "Вы можете увидеть в окне с построением.\n"
                        "Красный отрезок - биссектриса.\n Зеленый отрезок - высота.\n"
                        "Угол между биссектрисой и высотой равен "
                        f"{math.degrees(solution[3]):.2f} градусов.")
