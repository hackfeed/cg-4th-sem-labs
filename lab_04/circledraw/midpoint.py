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

    util.tmirrored(dots, x + x_center, y + y_center, x_center, y_center, color)
    delta = 1 - radius

    while x > y:
        y += 1
        if delta > 0:
            x -= 1
            delta -= 2 * x - 2
        delta += 2 * y + 3
        util.tmirrored(dots, x + x_center, y + y_center, x_center, y_center, color)

    return dots


def midpellipse(x_center, y_center, frad, srad, color):
    """
        Implementation of Midpoint ellipse drawing algorithm.
    """

    dots = []
    x = 0
    y = srad

    delta = srad**2 - frad**2 * srad + 0.25 * frad * frad
    dx = 2 * srad**2 * x
    dy = 2 * frad**2 * y

    while dx < dy:
        util.dmirrored(dots, x + x_center, y + y_center, x_center, y_center, color)

        x += 1
        dx += 2 * srad**2

        if delta >= 0:
            y -= 1
            dy -= 2 * frad**2
            delta -= dy

        delta += dx + srad**2

    delta = srad**2 * (x + 0.5)**2 + frad**2 * (y - 1)**2 - frad**2 * srad**2

    while y >= 0:
        util.dmirrored(dots, x + x_center, y + y_center, x_center, y_center, color)

        y -= 1
        dy -= 2 * frad**2

        if delta <= 0:
            x += 1
            dx += 2 * srad**2
            delta += dx

        delta -= dy - frad**2

    return dots
