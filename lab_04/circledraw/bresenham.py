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
    delta = 2 * (1 - radius)

    util.tmirrored(dots, x + x_center, y + y_center, x_center, y_center, color)

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

        util.tmirrored(dots, x + x_center, y + y_center, x_center, y_center, color)

    return dots


def bresellipse(x_center, y_center, frad, srad, color):
    """
        Implementation of Bresenham ellipse drawing algorithm.
    """

    dots = []
    x = 0
    y = srad
    delta = srad**2 - frad**2 * (2 * srad + 1)

    util.dmirrored(dots, x + x_center, y + y_center, x_center, y_center, color)

    while y > 0:
        if delta <= 0:
            delta_temp = 2 * delta + frad**2 * (2 * y - 1)
            x += 1
            delta += srad**2 * (2 * x + 1)
            if delta_temp >= 0:
                y -= 1
                delta += frad**2 * (-2 * y + 1)

        else:
            delta_temp = 2 * delta + srad**2 * (-2 * x - 1)
            y -= 1
            delta += frad**2 * (-2 * y + 1)
            if delta_temp < 0:
                x += 1
                delta += srad**2 * (2 * x + 1)

        util.dmirrored(dots, x + x_center, y + y_center, x_center, y_center, color)

    return dots
