"""
    Utility module.
"""


def tmirrored(dots, x, y, x_center, y_center, color):
    """
        Mirror given dots by X, Y and Bis.
    """

    dots.extend([
        [x, y, color],
        [2*x_center-x, y, color],
        [x, 2*y_center-y, color],
        [2*x_center-x, 2*y_center-y, color],
        [y + x_center - y_center, x + y_center - x_center, color],
        [-y + x_center + y_center, x + y_center - x_center, color],
        [y + x_center - y_center, -x + y_center + x_center, color],
        [-y + x_center + y_center, -x + y_center + x_center, color]
    ])


def dmirrored(dots, x, y, x_center, y_center, color):
    """
        Mirror given dots by X, Y.
    """

    dots.extend([
        [x, y, color],
        [2*x_center-x, y, color],
        [x, 2*y_center-y, color],
        [2*x_center-x, 2*y_center-y, color]
    ])
