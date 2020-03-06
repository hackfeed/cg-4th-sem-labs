from math import pi, sin, cos, sqrt


class Fish:
    """
        Fish representation.
    """

    eps = 1e-6
    body_color = "#4266f5"
    limb_color = "#f50a7f"
    eye_color = "#28b549"

    def __init__(self, *args, **kwargs):
        self.body = self.get_body(200, 70)
        self.head = self.get_head()
        self.eye = self.get_eye()
        self.mouth = self.get_mouth()
        self.upper_fin = self.get_upper_fin()
        self.lower_fin = self.get_lower_fin()
        self.tail = self.get_tail()

    def get_body(self, a, b):
        body = []
        t = 0

        while 2 * pi - t > Fish.eps:
            body.extend([-a*cos(t) + 420, b*sin(t) + 340])
            t += 0.1

        body = body[10:]
        body = body[:len(body)-10]

        return body

    def get_head(self):
        body = self.body
        start_p = [body[0], body[1]]
        end_p = [body[len(body)-2], body[len(body) - 1]]

        r = sqrt((start_p[0] - end_p[0])**2 + (start_p[1] - end_p[1])**2) / 2

        head = []
        t = 0

        while 2 * pi - t > Fish.eps:
            head.extend([r*cos(t) + start_p[0], r*sin(t) + start_p[1] - r])
            t += 0.1

        head.extend([head[0], head[1]])

        return head

    def get_eye(self):
        head = self.head
        eye = []
        t = 0
        r = 7
        h_r = (head[0] - head[len(head) // 2]) / 2

        while 2 * pi - t > Fish.eps:
            eye.extend([r*cos(t) + head[0] - h_r * 1.5, r*sin(t) + head[1] - h_r * 0.3])
            t += 0.1

        return eye

    def get_mouth(self):
        head = self.head
        h_r = (head[0] - head[len(head) // 2]) / 2
        mouth = [
            head[0] - h_r * 1.7, head[1] + h_r * 0.3,
            head[0] - h_r * 1.3, head[1] + h_r * 0.3
        ]

        return mouth

    def get_upper_fin(self):
        body = self.body
        upper_fin = [
            body[len(body)-14], body[len(body)-13],
            body[len(body)-14] + 20, body[len(body) - 13] - 50,
            body[len(body)-28] + 20, body[len(body) - 13] - 50,
            body[len(body)-28], body[len(body)-27]
        ]

        return upper_fin

    def get_lower_fin(self):
        body = self.body
        lower_fin = [
            body[14], body[15],
            body[14] + 20, body[15] + 50,
            body[28] + 20, body[15] + 50,
            body[28], body[29]
        ]

        return lower_fin

    def get_tail(self):
        body = self.body
        tail = [
            body[len(body) // 2 + 5], body[len(body) // 2 + 6],
            body[len(body) // 2 + 5] + 70, body[len(body) // 2 + 6] - 100,
            body[len(body) // 2 + 5] + 120, body[len(body) // 2 + 6] - 100,
            body[len(body) // 2 + 5] + 120, body[len(body) // 2 + 6] - 40,
            body[len(body) // 2 + 5] + 90, body[len(body) // 2 + 6] - 20,
            body[len(body) // 2 + 5] + 120, body[len(body) // 2 + 6],
            body[len(body) // 2 + 5] + 120, body[len(body) // 2 + 6] + 60,
            body[len(body) // 2 - 5], body[len(body) // 2 - 4]
        ]

        return tail

    def draw(self, canvas):
        canvas.create_line(*self.body, fill=Fish.body_color, width=2)
        canvas.create_line(*self.head, fill=Fish.limb_color, width=2)
        canvas.create_line(*self.eye, fill=Fish.eye_color, width=2)
        canvas.create_line(*self.mouth, fill=Fish.body_color, width=2)
        canvas.create_line(*self.upper_fin, fill=Fish.limb_color, width=2)
        canvas.create_line(*self.lower_fin, fill=Fish.limb_color, width=2)
        canvas.create_line(*self.tail, fill=Fish.limb_color, width=2)


fish = Fish()
