"""
    Interface viewset module.
"""

import tkinter as tk
from tkinter import messagebox
from copy import deepcopy

from imgact.draw import Fish


def move(root, img, states):
    """
        Move img elsewhere.
    """

    try:
        dx = float(root.dxmove.get())
        dy = float(root.dymove.get())
    except ValueError:
        messagebox.showerror(
            "Ошибка ввода", "Невозможно получить вещественное число. Проверьте корректность ввода.")
    else:
        states.append(deepcopy(img))
        img.move(dx, dy)
        root.image.delete("all")
        img.draw(root.image)
        root.image.create_oval(419, 339, 421, 341, fill="red")
        root.image.create_text(420, 350, text="(420;340)", font="-family {Consolas} -size 14")
        check_states(root, states)


def rotate(root, img, states):
    """
        Rotate img somehow.
    """

    try:
        rx = float(root.xrotate.get())
        ry = float(root.yrotate.get())
        angle = float(root.angrotate.get())
    except ValueError:
        messagebox.showerror(
            "Ошибка ввода", "Невозможно получить вещественное число. Проверьте корректность ввода.")
    else:
        states.append(deepcopy(img))
        img.rotate(rx, ry, angle)
        root.image.delete("all")
        img.draw(root.image)
        root.image.create_oval(419, 339, 421, 341, fill="red")
        root.image.create_text(420, 350, text="(420;340)", font="-family {Consolas} -size 14")
        check_states(root, states)


def scale(root, img, states):
    """
        Scale img somehow.
    """

    try:
        mx = float(root.xscale.get())
        my = float(root.yscale.get())
        kx = float(root.kxscale.get())
        ky = float(root.kyscale.get())
    except ValueError:
        messagebox.showerror(
            "Ошибка ввода", "Невозможно получить вещественное число. Проверьте корректность ввода.")
    else:
        states.append(deepcopy(img))
        img.scale(mx, my, kx, ky)
        root.image.delete("all")
        img.draw(root.image)
        root.image.create_oval(419, 339, 421, 341, fill="red")
        root.image.create_text(420, 350, text="(420;340)", font="-family {Consolas} -size 14")
        check_states(root, states)


def step_back(root, img, states):
    """
        Rollback to previous state.
    """

    root.image.delete("all")
    imgn = states.pop()
    if states == []:
        states.clear()
        img.reset()
        img.scale(420, 340, 0.7, 0.7)
    imgn.draw(root.image)
    root.image.create_oval(419, 339, 421, 341, fill="red")
    root.image.create_text(420, 350, text="(420;340)", font="-family {Consolas} -size 14")
    check_states(root, states)


def reset(root, img, states):
    """
        Reset image to starting state.
    """

    root.dxmove.delete(0, "end")
    root.dymove.delete(0, "end")
    root.xrotate.delete(0, "end")
    root.yrotate.delete(0, "end")
    root.angrotate.delete(0, "end")
    root.xscale.delete(0, "end")
    root.yscale.delete(0, "end")
    root.kxscale.delete(0, "end")
    root.kyscale.delete(0, "end")

    root.dxmove.insert(tk.END, "0")
    root.dymove.insert(tk.END, "0")
    root.xrotate.insert(tk.END, "420")
    root.yrotate.insert(tk.END, "340")
    root.angrotate.insert(tk.END, "0")
    root.xscale.insert(tk.END, "420")
    root.yscale.insert(tk.END, "340")
    root.kxscale.insert(tk.END, "1")
    root.kyscale.insert(tk.END, "1")

    root.image.delete("all")
    states.clear()
    img.reset()
    img.scale(420, 340, 0.7, 0.7)
    img.draw(root.image)
    root.image.create_oval(419, 339, 421, 341, fill="red")
    root.image.create_text(420, 350, text="(420;340)", font="-family {Consolas} -size 14")
    check_states(root, states)


def check_states(root, states):
    """
        Check states list.
    """

    if states == []:
        root.backbtn.configure(state="disabled")
    else:
        root.backbtn.configure(state="normal")
