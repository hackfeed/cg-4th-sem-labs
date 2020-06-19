"""
    Parametric equation.
"""

import numpy as np
from math import sin, cos, radians, pi
from circledraw import util


def parcircle(x_center, y_center, radius, color):
    """
        Implementation of circle parametric equation method.
    """

    dots = []
    step = 1 / radius

    for t in np.arange(0, pi / 4 + step, step):
        x = x_center + radius * cos(t)
        y = y_center + radius * sin(t)
        util.tmirrored(dots, x, y, x_center, y_center, color)

    return dots


def parellipse(x_center, y_center, frad, srad, color):
    """
        Implemetation of ellipse parametric euqation method.
    """

    dots = []
    step = 1 / frad if frad > srad else 1 / srad

    for t in np.arange(0, pi / 2 + step, step):
        x = x_center + frad * cos(t)
        y = y_center + srad * sin(t)
        util.dmirrored(dots, x, y, x_center, y_center, color)

    return dots
