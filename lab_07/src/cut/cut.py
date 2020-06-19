from math import sqrt

LEFT = 0b0001
RIGHT = 0b0010
BOTTOM = 0b0100
TOP = 0b1000


def set_code(dot, cut):
    code = 0b0000
    if dot[0] < cut[0]:
        code += LEFT
    if dot[1] < cut[1]:
        code += TOP
    if dot[0] > cut[2]:
        code += RIGHT
    if dot[1] > cut[3]:
        code += BOTTOM

    return code


def get_distance(dot_start, dot_end):
    return sqrt((dot_start[0] - dot_end[0])**2 + (dot_start[1] - dot_end[1])**2)


def midpointcut(root, cut, dot_start, dot_end, eps):
    i = 1
    while True:
        code_start = set_code(dot_start, cut)
        code_end = set_code(dot_end, cut)

        if code_start == 0 and code_end == 0:
            root.draw_line(dot_start, dot_end, root.res_color)
            return

        if code_start & code_end:
            return

        if i > 2:
            root.draw_line(dot_start, dot_end, root.res_color)
            return

        dot_r = dot_start

        if code_end == 0:
            dot_start, dot_end = dot_end, dot_r
            i += 1
            continue

        while get_distance(dot_start, dot_end) >= eps:
            dot_middle = [(dot_start[0] + dot_end[0]) / 2, (dot_start[1] + dot_end[1]) / 2]
            dot_tmp = dot_start
            dot_start = dot_middle

            code_start = set_code(dot_start, cut)
            code_end = set_code(dot_end, cut)

            if code_start & code_end:
                dot_start = dot_tmp
                dot_end = dot_middle

        dot_start, dot_end = dot_end, dot_r
        i += 1


def cut(root):
    for section in root.sections:
        midpointcut(root, root.cut, section[0], section[1], 1e-1)
