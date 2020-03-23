"""
    Xiaolin Wu's algorithm.
"""


def fpart(x):
    """
        Get float part of number.
    """

    return x - int(x)


def rfpart(x):
    """
        Get real part of number.
    """

    return 1 - fpart(x)


def wu(x_start, y_start, x_end, y_end, color):
    """
        Implementation of Xiaolin Wu algorithm.
    """

    dx = x_end - x_start
    dy = y_end - y_start

    steep = abs(dx) < abs(dy)

    def p(px, py):
        return ([px, py], [py, px])[steep]

    if steep:
        x_start, y_start, x_end, y_end, dx, dy = y_start, x_start, y_end, x_end, dy, dx
    if x_end < x_start:
        x_start, x_end, y_start, y_end = x_end, x_start, y_end, y_start

    m = dy / dx
    intery = y_start + rfpart(x_start) * m

    dots = []

    def get_endpoint(x_s, y_s):
        x_e = round(x_s)
        y_e = y_s + (x_e - x_s) * m
        x_gap = rfpart(x_s + 0.5)

        px, py = int(x_e), int(y_e)

        dens1 = rfpart(y_e) * x_gap
        dens2 = fpart(y_e) * x_gap

        dots.extend([[*p(px, py), color + (255 * dens2, 255 * dens2, 255)]])
        dots.extend([[*p(px, py), color + (255 * dens1, 255 * dens1, 255)]])

        return px

    x_s = get_endpoint(x_start, y_start) + 1
    x_e = get_endpoint(x_end, y_end)

    for x in range(x_s, x_e):
        y = int(intery)

        dens1 = rfpart(intery)
        dens2 = fpart(intery)

        dots.extend([[*p(x, y), color + (255 * dens2, 255 * dens2, 255)]])
        dots.extend([[*p(x, y+1), color + (255 * dens1, 255 * dens1, 255)]])

        intery += m

    return dots
