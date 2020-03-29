"""
    Canonical equation.
"""

from math import sqrt


def cancircle(x_center, y_center, radius, color):
    """
        Implementation of canonical equation method.
    """

    dots = []

    for x in range(x_center, x_center + int(radius / sqrt(2)) + 1):
        y = sqrt(radius**2 - (x - x_center)**2) + y_center
        dots.extend([
            [x, y, color],
            [y, x, color],
            [2*x_center-x, y, color],
            [x, 2*y_center-y, color],
            [2*x_center-y, x, color],
            [y, 2*y_center-x, color],
            [2*x_center-x, 2*y_center-y, color],
            [2*x_center-y, 2*y_center-x, color]
        ])

    return dots
