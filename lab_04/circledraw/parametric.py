"""
    Parametric equation.
"""

import numpy as np
from math import sin, cos, radians, pi
from circledraw import util


def parcircle(x_center, y_center, radius, color):
    """
        Implementation of parametric equation method.
    """

    dots = []
    step = 1 / radius

    for t in np.arange(0, pi / 4 + step, step):
        x = x_center + radius * cos(t)
        y = y_center + radius * sin(t)
        util.add_mirrored(dots, x, y, x_center, y_center, color)

    return dots
