"""
    Drawing utilities.
"""

import tkinter as tk
import time
import colorutils as cu
from circledraw import bresenham, canonical, midpoint, parametric


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
        Get time taken by circle creation of different algorithms.
    """

    taken_time = {
        "Canonical": [canonical.cancircle, canonical.canellipse],
        "Parametric": [parametric.parcircle, parametric.parellipse],
        "Bresenham": [bresenham.brescircle, bresenham.bresellipse],
        "Midpoint": [midpoint.midpcircle, midpoint.midpellipse],
        "Tkinter create_oval": [canvas.create_oval, canvas.create_oval]
    }

    color = cu.Color((0, 0, 255))

    for method in taken_time:
        circle_res = []
        ellipse_res = []
        for radius in range(1000, 40000, 2000):
            r1 = radius
            r2 = 2 * radius
            if taken_time[method][0] == canvas.create_oval:
                cfunc = taken_time[method][0](0 - r1, 0 - r1, 0 + r1, 0 + r1, outline=color.hex)
                efunc = taken_time[method][1](0 - r1, 0 - r2, 0 + r1, 0 + r2, outline=color.hex)
            else:
                cfunc = taken_time[method][0](0, 0, r1, color)
                efunc = taken_time[method][1](0, 0, r1, r2, color)
            start_time = time.time()

            for _ in range(1000):
                cfunc
            end_time = time.time()
            circle_res.append((end_time - start_time) / 1000)

            start_time = time.time()
            for _ in range(1000):
                efunc
            end_time = time.time()
            ellipse_res.append((end_time - start_time) / 1000)

        taken_time[method][0] = circle_res
        taken_time[method][1] = ellipse_res

    canvas.delete("all")

    return taken_time, [x for x in range(1000, 40000, 2000)]
