def check_active_edges(active_edges):
    i = 0
    while i < len(active_edges):
        active_edges[i][0] += active_edges[i][1]
        active_edges[i][1] -= 1
        if active_edges[i][2] < 1:
            active_edges.pop(i)
        else:
            i += 1


def add_active_edges(y_groups, active_edges, y):
    if y in y_groups:
        for edge in y_groups[y]:
            active_edges.append(edge)
    active_edges.sort(key=lambda edge: edge[0])


def fill(root):
    y_end = root.y_max
    y_start = root.y_min
    while y_end > y_start:
        check_active_edges(root.active_edges)
        add_active_edges(root.y_groups, root.active_edges, y_end)
        for i in range(0, len(root.active_edges), 2):
            for x in range(int(root.active_edges[i][0]), round(root.active_edges[i+1][0])):
                root.image.put(root.color, (x, y_end))
        y_end -= 1
