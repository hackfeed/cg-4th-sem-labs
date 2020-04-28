def x_cmp(active_edge):
    return active_edge[0]


def fill(root):
    y = root.y_max
    while y > root.y_min:
        current_y = y
        root.check_y_group(y, x_cmp)
        for i in range(0, len(root.active_edges), 2):
            current_y = y
            while root.active_edges[i][2] > 0 and root.active_edges[i+1][2] > 0:
                for x in range(int(root.active_edges[i][0]), round(root.active_edges[i+1][0]) + 1):
                    root.image.put(root.color, (x, current_y))
                current_y -= 1
                root.check_y_group(current_y, x_cmp)
                root.active_edges[i][0] += root.active_edges[i][1]
                root.active_edges[i+1][0] += root.active_edges[i+1][1]
                root.active_edges[i][2] -= 1
                root.active_edges[i+1][2] -= 1
            if root.active_edges[i][2] == 0:
                root.active_edges.pop(i)
            elif root.active_edges[i+1][2] == 0:
                root.active_edges.pop(i+1)
        root.check_y_group(y, x_cmp)
