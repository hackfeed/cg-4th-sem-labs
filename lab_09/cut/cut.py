def get_vect(dot_start, dot_end):
    return [dot_end[0] - dot_start[0], dot_end[1] - dot_start[1]]


def get_vect_mul(fvector, svector):
    return fvector[0] * svector[1] - fvector[1] * svector[0]


def get_scalar_mul(fvector, svector):
    return fvector[0] * svector[0] + fvector[1] * svector[1]


def get_normal(dot_start, dot_end, dot_check):
    vect = get_vect(dot_start, dot_end)
    normal = None

    if vect[0] == 0:
        normal = [1, 0]
    else:
        normal = [-vect[1] / vect[0], 1]

    if get_scalar_mul(get_vect(dot_end, dot_check), normal) < 0:
        for i in range(len(normal)):
            normal[i] = -normal[i]

    return normal


def get_normals(cut):
    normals = []
    cutlen = len(cut)

    for i in range(cutlen):
        normals.append(get_normal(cut[i], cut[(i + 1) % cutlen], cut[(i + 2) % cutlen]))

    return normals


def check_cut(cut):
    if len(cut) < 3:
        return False

    vect1 = get_vect(cut[0], cut[1])
    vect2 = get_vect(cut[1], cut[2])

    sign = None
    if get_vect_mul(vect1, vect2) > 0:
        sign = 1
    else:
        sign = -1

    for i in range(3, len(cut)):
        vecti = get_vect(cut[i-2], cut[i-1])
        vectj = get_vect(cut[i-1], cut[i])

        if sign * get_vect_mul(vecti, vectj) < 0:
            return False

    if sign < 0:
        cut.reverse()

    return True


def cyrusbeck(root, cut, section, normals):
    t_start = 0
    t_end = 1

    vect = get_vect(section[0], section[1])
    cutlen = len(cut)

    for i in range(cutlen):
        w_vect = get_vect(cut[(i + 1) % cutlen], section[0])
        if cut[i] != section[0]:
            w_vect = get_vect(cut[i], section[0])

        vect_scal = get_scalar_mul(vect, normals[i])
        w_vect_scal = get_scalar_mul(w_vect, normals[i])

        if vect_scal == 0:
            if w_vect_scal < 0:
                return
            continue

        t = -w_vect_scal / vect_scal
        if vect_scal > 0:
            if t > t_start:
                t_start = t
        else:
            if t < t_end:
                t_end = t

        if t_start > t_end:
            break

    if t_start < t_end:
        dot_start = [round(section[0][0] + vect[0] * t_start),
                     round(section[0][1] + vect[1] * t_start)]
        dot_end = [round(section[0][0] + vect[0] * t_end),
                   round(section[0][1] + vect[1] * t_end)]
        root.draw_line(dot_start, dot_end, root.res_color)


def cut(root):
    if not check_cut(root.cut):
        return

    normals = get_normals(root.cut)
    print(normals)
    for section in root.sections:
        cyrusbeck(root, root.cut, section, normals)
