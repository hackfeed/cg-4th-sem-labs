"""
    Bresenham method.
"""

from circledraw import util


def brescircle(x_center, y_center, radius, color):
    """
        Implementation of Bresenham circle drawing algorithm.
    """

    dots = []
    x = 0
    y = radius
    delta = 3 - 2 * radius

    util.add_mirrored(dots, x + x_center, y + y_center, x_center, y_center, color)

    while x < y:
        if delta <= 0:
            delta_temp = 2 * (delta + y) - 1
            x += 1
            if delta_temp >= 0:
                delta += 2 * (x - y + 1)
                y -= 1
            else:
                delta += 2 * x + 1

        else:
            delta_temp = 2 * (delta - x) - 1
            y -= 1
            if delta_temp < 0:
                delta += 2 * (x - y + 1)
                x += 1
            else:
                delta -= 2 * y - 1
        util.add_mirrored(dots, x + x_center, y + y_center, x_center, y_center, color)

    return dots
