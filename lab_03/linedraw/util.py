"""
    Drawing utilities.
"""

import tkinter as tk


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
