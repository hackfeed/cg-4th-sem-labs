"""
    Drawing utilities.
"""

import tkinter as tk
import timeit


def set_pixel(canvas, x, y, color):
    """
        Draw single pixel.
    """

    canvas.create_line(x, y, x+1, y, fill=color.hex)


def draw_line(canvas, line):
    """
        Draw line by setting pixels.
    """

    for dot in line:
        set_pixel(canvas, dot[0], dot[1], dot[2])


def get_time(canvas):
    """
        Get time taken by line creation of different algorithms.
    """

    taken_time = {
        "DDA": dda.dda,
        "Bresenham (int)": bresenham.bresenham_int,
        "Bresenham (float)": bresenham.bresenham_db,
        "Bresenham (anti-aliased)": bresenham.bresenham_antialiased,
        "Xiaolin Wu": wu.wu,
        "Tkinter create_line": canvas.create_line
    }

    color = cu.Color((0, 0, 255))

    for method in taken_time:
        if taken_time[method] == canvas.create_line:
            func = taken_time[method](0, 0, 500, 500, fill=color.hex)
        else:
            func = taken_time[method](0, 0, 500, 500, color)
        taken_time[method] = timeit.timeit(lambda: func, number=1000) * 1e7

    canvas.delete("all")

    return taken_time
