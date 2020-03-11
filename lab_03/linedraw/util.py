"""
    Drawing utilities.
"""

import tkinter as tk


def set_pixel(canvas, x, y):
    """
        Draw single pixel.
    """

    canvas.create_line(x, y, x+1, y)


def draw_line(canvas, line):
    """
        Draw line by setting pixels.
    """

    for dot in line:
        set_pixel(canvas, dot[0], dot[1])
