"""
    Triangle geometry realization module.
"""

import math


def is_exist(a_side, b_side, c_side):
    """
        Check if triangle exists.
    """

    ab_cond = (a_side + b_side) > c_side
    ac_cond = (a_side + c_side) > b_side
    bc_cond = (b_side + c_side) > a_side

    if ab_cond and ac_cond and bc_cond:
        return True

    return False


def get_sides(a_dot, b_dot, c_dot):
    """
        Calculate triangle's sides.
    """

    a_side = math.hypot(a_dot[0] - b_dot[0], a_dot[1] - b_dot[1])
    b_side = math.hypot(b_dot[0] - c_dot[0], b_dot[1] - c_dot[1])
    c_side = math.hypot(a_dot[0] - c_dot[0], a_dot[1] - c_dot[1])

    return a_side, b_side, c_side
