from math import pi, sin, cos, sqrt


class Fish:
    """
        Fish representation.
    """

    def __init__(self, *args, **kwargs):
        self.body = get_body(200, 70)
        self.head = get_head(self.body)
        self.eye = get_eye(self.head)
        self.mouth = get_mouth(self.head)
        self.upper_fin = get_upper_fin(self.body)


def get_body(a, b):
    body = []
    eps = 1e-6
    t = 0

    while 2 * pi - t > eps:
        body.extend([-a*cos(t) + 420, b*sin(t) + 340])
        t += 0.1

    body = body[10:]
    body = body[:len(body)-10]

    return body


def get_head(body):
    start_p = [body[0], body[1]]
    end_p = [body[len(body)-2], body[len(body) - 1]]

    r = sqrt((start_p[0] - end_p[0])**2 + (start_p[1] - end_p[1])**2) / 2

    head = []
    eps = 1e-6
    t = 0

    while 2 * pi - t > eps:
        head.extend([r*cos(t) + start_p[0], r*sin(t) + start_p[1] - r])
        t += 0.1

    head.extend([head[0], head[1]])

    return head


def get_eye(head):
    eye = []
    eps = 1e-6
    t = 0
    r = 7
    h_r = (head[0] - head[len(head) // 2]) / 2

    while 2 * pi - t > eps:
        eye.extend([r*cos(t) + head[0] - h_r * 1.5, r*sin(t) + head[1] - h_r * 0.3])
        t += 0.1

    return eye


def get_mouth(head):
    h_r = (head[0] - head[len(head) // 2]) / 2
    mouth = [
        head[0] - h_r * 1.7, head[1] + h_r * 0.3,
        head[0] - h_r * 1.3, head[1] + h_r * 0.3
    ]

    return mouth


def get_upper_fin(body):
    upper_fin = [
        body[len(body)-14], body[len(body)-13],
        body[len(body)-14] + 20, body[len(body) - 13] - 50,
        body[len(body)-28] + 20, body[len(body) - 13] - 50,
        body[len(body)-28], body[len(body)-27]
    ]

    return upper_fin


fish = Fish()
