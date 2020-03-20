"""
    Xiaolin Wu's algorithm.
"""


def fpart(x):
    """
        Get float part of number.
    """

    return x - int(x)


def rpart(x):
    """
        Get real part of number.
    """

    return 1 - fpart(x)


# def wu(x_start, x_end, y_start, y_end, color):
#     """
#         Implementation of Xiaolin Wu algorithm.
#     """

#     dx = x_end - x_start
#     dy = y_end - y_start

#     steep = abs(dx) < abs(dy)
#     def p(px, py): return ((px, py), (py, px))[steep]

#     if steep:
#         x_start, y_start, x_end, y_end, dx, dy = y_start, x_start, y_end, x_end, dy, dx
#     if x_end < x_start:
#         x_start, x_end, y_start, y_end = x_end, x_start, y_end, y_start

#     grad = dy/dx
#     intery = y_start + rpart(x_start) * grad

#     dots = []

#     for x in range(x_start, x_end):
