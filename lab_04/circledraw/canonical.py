"""
    Canonical equation.
"""

from math import sqrt
from circledraw import util


def cancircle(x_center, y_center, radius, color):
    """
        Implementation of canonical equation method.
    """

    dots = []

    for x in range(x_center, x_center + int(radius / sqrt(2)) + 1):
        y = sqrt(radius**2 - (x - x_center)**2) + y_center
        util.add_mirrored(dots, x, y, x_center, y_center, color)

    return dots
