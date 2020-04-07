"""
    Utility module.
"""


def tmirrored(dots, x, y, x_center, y_center, color):
    """
        Mirror given dots by X, Y and Bis.
    """

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
