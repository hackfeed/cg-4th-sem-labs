"""
    Triangle geometry realization module.
"""

import math
from itertools import combinations
from collections import deque


def altitudep(ax, ay, bx, by, cx, cy):
    """
        Find altitude point, located on the base from A point.
    """
    bcx = cx - bx
    bcy = cy - by
    bax = ax - bx
    bay = ay - by

    t = (bcx * bax + bcy * bay) / (bcx * bcx + bcy * bcy)

    alx = (bx + t * bcx)
    aly = (by + t * bcy)

    return alx, aly


def bisectorp(ax, ay, bx, by, cx, cy):
    """
        Find bisector point, located on the base from A point.
    """
    ab = math.sqrt((ax - bx)**2 + (ay - by)**2)
    ac = math.sqrt((ax - cx)**2 + (ay - cy)**2)

    bisx = (ac * bx + ab * cx) / (ab + ac)
    bisy = (ac * by + ab * cy) / (ab + ac)

    return bisx, bisy


def ang(ax, ay, bx, by, cx, cy):
    """
        Find angle in triangle using cosine theorem.
    """
    ab = math.sqrt((ax - bx)**2 + (ay - by)**2)
    ac = math.sqrt((ax - cx)**2 + (ay - cy)**2)
    bc = math.sqrt((bx - cx)**2 + (by - cy)**2)

    return math.acos((ac**2 + ab**2 - bc**2) / 2 / ac / ab)


def is_oneline(ax, ay, bx, by, cx, cy):
    """
        Check if three dots are lying on the same line.
    """
    eps = 1e-6
    return abs((cx - ax) * (by - ay) - (bx - ax) * (cy - ay)) <= eps


def find_solution(dots):
    """
        Find flex solution.
    """
    best_ang = 0
    solution = None
    for dset in combinations(dots, 3):
        dset = deque(dset)
        if is_oneline(dset[0][0], dset[0][1], dset[1][0],
                      dset[1][1], dset[2][0], dset[2][1]):
            continue
        i = 1
        while i < 3:
            altitude = altitudep(dset[0][0], dset[0][1], dset[1][0],
                                 dset[1][1], dset[2][0], dset[2][1])
            bisector = bisectorp(dset[0][0], dset[0][1], dset[1][0],
                                 dset[1][1], dset[2][0], dset[2][1])
            try:
                angle = ang(dset[0][0], dset[0][1],
                            altitude[0], altitude[1],
                            bisector[0], bisector[1])
            except ValueError:
                angle = 0
            if angle > best_ang:
                best_ang = angle
                sset = dset.copy()
                solution = (sset, altitude, bisector, best_ang)
            dset.rotate(-i)
            i += 1

    return solution
