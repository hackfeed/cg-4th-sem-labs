"""
    Digital differential analyzer algoritghm.
"""


def dda(x_start, y_start, x_end, y_end, color):
    """
        Implementation of DDA algorithm.
    """

    dx = x_end - x_start
    dy = y_end - y_start

    l = abs(dx) if abs(dx) > abs(dy) else abs(dy)

    dx /= l
    dy /= l

    x = x_start
    y = y_start

    dots = [[x, y, color]]

    for _ in range(l):
        x += dx
        y += dy
        dots.extend([[x, y, color]])

    return dots
