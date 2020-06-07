from math import pi, sin, cos
from numpy import arange

from fhorizon import funcs


def rotate_mat(root, mat):
    res_mat = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]

    for i in range(4):
        for j in range(4):
            for k in range(4):
                res_mat[i][j] += root.mat[i][k] * mat[k][j]

    root.mat = res_mat


def trans_dot(root, dot):
    dot.append(1)
    res_dot = [0, 0, 0, 0]
    for i in range(4):
        for j in range(4):
            res_dot[i] += dot[j] * root.mat[j][i]

    for i in range(3):
        res_dot[i] *= root.scale

    res_dot[0] += root.canv_width / 2
    res_dot[1] += root.canv_height / 2

    return res_dot[:3]


def xrotate(root):
    val = float(root.xrotatesb.get()) / 180 * pi
    mat = [[1, 0, 0, 0],
           [0, cos(val), sin(val), 0],
           [0, -sin(val), cos(val), 0],
           [0, 0, 0, 1]]
    rotate_mat(root, mat)


def yrotate(root):
    val = float(root.yrotatesb.get()) / 180 * pi
    mat = [[cos(val), 0, -sin(val), 0],
           [0, 1, 0, 0],
           [sin(val), 0, cos(val), 0],
           [0, 0, 0, 1]]
    rotate_mat(root, mat)


def zrotate(root):
    val = float(root.yrotatesb.get()) / 180 * pi
    mat = [[cos(val), sin(val), 0, 0],
           [-sin(val), cos(val), 0, 0],
           [0, 0, 1, 0],
           [0, 0, 0, 1]]
    rotate_mat(root, mat)


def predraw_horizon(root, fdot, sdot, uphor, lowhor):
    if fdot[0] > sdot[0]:
        fdot, sdot = sdot, fdot

    dx = sdot[0] - fdot[0]
    dy = sdot[1] - fdot[1]

    l = None
    if dx > dy:
        l = dx
    else:
        l = dy

    dx /= l
    dy /= l

    x, y = fdot[0], fdot[1]

    for _ in range(int(l) + 1):
        if not root.draw_dot(int(round(x)), y, uphor, lowhor):
            return

        x += dx
        y += dy


def draw_horizon(root, func, uphor, lowhor, start, end, step, z):
    def f(x): return func(x, z)
    prev = None

    for x in arange(start, end + step, step):
        cur = trans_dot(root, [x, f(x), z])
        if prev:
            predraw_horizon(root, prev, cur, uphor, lowhor)
        prev = cur


def fhorizon(root):
    root.reset()

    func_ind = root.funclst.curselection()[0]
    func = funcs.funcs[root.funclst.get(func_ind)]
    uphor = [0 for _ in range(root.canv_width)]
    lowhor = [root.canv_height for _ in range(root.canv_width)]

    for z in arange(root.z_from, root.z_to + root.z_step):
        draw_horizon(root, func, uphor, lowhor, root.x_from, root.x_to, root.x_step, z)

    for z in arange(root.z_from, root.z_to, root.z_step):
        fdot = trans_dot(root, [root.x_from, func(root.x_from, z), z])
        sdot = trans_dot(root, [root.x_from, func(root.x_from, z + root.z_step), z + root.z_step])
        root.draw_line(fdot, sdot, root.color)
        fdot = trans_dot(root, [root.x_to, func(root.x_to, z), z])
        sdot = trans_dot(root, [root.x_to, func(root.x_to, z + root.z_step), z + root.z_step])
        root.draw_line(fdot, sdot, root.color)
