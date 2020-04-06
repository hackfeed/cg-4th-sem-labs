"""
    Midpoint method.
"""

from circledraw import util


def midpcircle(x_center, y_center, radius, color):
    """
        Implementation of Midpoint circle drawing algorithm.
    """

    dots = []
    x = radius
    y = 0

    util.add_mirrored(dots, x + x_center, y + y_center, x_center, y_center, color)
    delta = 1 - radius

    while x > y:
        y += 1
        if delta > 0:
            x -= 1
            delta -= 2 * x - 2
        delta += 2 * y + 3
        util.add_mirrored(dots, x + x_center, y + y_center, x_center, y_center, color)

    return dots
