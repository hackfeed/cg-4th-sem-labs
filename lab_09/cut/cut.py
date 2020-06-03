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


def unique(sections):
    for section in sections:
        section.sort()
    return list(filter(lambda section: (sections.count(section) % 2) == 1, sections))


def is_in_section(point, section):
    fvect = get_vect(point, section[0])
    svect = get_vect(*section)

    if abs(get_vect_mul(fvect, svect)) <= 1e-6:
        if section[0] < point < section[1] or section[1] < point < section[0]:
            return True

    return False


def get_sections(section, points):
    new_points = [*section]
    for point in points:
        if is_in_section(point, section):
            new_points.append(point)

    new_points.sort()

    sections = []
    for i in range(len(new_points) - 1):
        sections.append([new_points[i], new_points[i + 1]])

    return sections


def get_unique_sections(figure):
    sections = []
    points = figure[2:]
    figlen = len(figure)
    for i, _ in enumerate(figure):
        section = [figure[i], figure[(i + 1) % figlen]]
        sections.extend(get_sections(section, points))
        points.pop(0)
        points.append(figure[i])

    return unique(sections)


def check_vis(point, dot_start, dot_end):
    fvect = get_vect(dot_start, dot_end)
    svect = get_vect(dot_start, point)

    if get_vect_mul(fvect, svect) >= 0:
        return True

    return False


def get_intersection(section, edge, normal):
    vect = get_vect(section[0], section[1])
    w_vect = get_vect(edge[0], section[0])

    vect_scal = get_scalar_mul(vect, normal)
    w_wect_scal = get_scalar_mul(w_vect, normal)

    diff = [section[1][0] - section[0][0], section[1][1] - section[0][1]]
    t = -w_wect_scal / vect_scal

    return [section[0][0] + diff[0] * t, section[0][1] + diff[1] * t]


def get_cut(figure, edge, normal):
    res_figure = []
    figlen = len(figure)

    if figlen < 3:
        return []

    pcheck = check_vis(figure[0], *edge)

    for i in range(1, figlen + 1):
        ccheck = check_vis(figure[i % figlen], *edge)

        if pcheck:
            if ccheck:
                res_figure.append(figure[i % figlen])
            else:
                res_figure.append(get_intersection(
                    [figure[i - 1], figure[i % figlen]], edge, normal))

        else:
            if ccheck:
                res_figure.append(get_intersection(
                    [figure[i - 1], figure[i % figlen]], edge, normal))
                res_figure.append(figure[i % figlen])

        pcheck = ccheck

    return res_figure


def sutherlandhodgman(figure, cut, normals):
    res_figure = figure
    for i, _ in enumerate(cut):
        edge = [cut[i], cut[(i + 1) % len(cut)]]
        print(f"Сторона - {edge}, нормаль - {normals[i]}")
        res_figure = get_cut(res_figure, edge, normals[i])
        if len(res_figure) < 3:
            return []

    return res_figure


def cut(root):
    if not check_cut(root.cut):
        return

    normals = get_normals(root.cut)
    figure = sutherlandhodgman(root.figure, root.cut, normals)
    root.draw_figure(get_unique_sections(figure), root.res_color)
