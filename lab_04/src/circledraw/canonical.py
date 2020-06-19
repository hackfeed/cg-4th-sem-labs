"""
    Canonical equation.
"""

from math import sqrt
from circledraw import util


def cancircle(x_center, y_center, radius, color):
    """
        Implementation of circle canonical equation method.
    """

    dots = []

    for x in range(x_center, x_center + int(radius / sqrt(2)) + 1):
        y = sqrt(radius**2 - (x - x_center)**2) + y_center
        util.tmirrored(dots, x, y, x_center, y_center, color)

    return dots


def canellipse(x_center, y_center, frad, srad, color):
    """
        Implementation of ellipse canonical equation method.
    """

    dots = []
    limit = int(x_center + frad / sqrt(1 + srad**2 / frad**2))

    for x in range(x_center, limit + 1):
        y = sqrt(frad**2 * srad**2 - (x - x_center)**2 * srad**2) / frad + y_center
        util.dmirrored(dots, x, y, x_center, y_center, color)

    limit = int(y_center + srad / sqrt(1 + frad**2 / srad**2))

    for y in range(limit, y_center - 1, -1):
        x = sqrt(frad**2 * srad**2 - (y - y_center)**2 * frad**2) / srad + x_center
        util.dmirrored(dots, x, y, x_center, y_center, color)

    return dots
