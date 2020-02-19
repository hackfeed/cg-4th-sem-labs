"""
    Triangle viewset module.
"""

import tkinter as tk


def draw_triangle(root, trcoords, trparts):
    draw_window = tk.Toplevel(root)
    draw_window.grab_set()
    draw_window.iconbitmap("icon.ico")
    draw_window.geometry("800x600+425+250")
    draw_window.resizable(False, False)
    draw_window.title("Визуализация треугольника")
    draw_window.config(bg="white")

    draw_canvas = tk.Canvas(draw_window, width=800, height=600, bg="white")
    draw_canvas.focus_set()
    draw_canvas.pack()

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
