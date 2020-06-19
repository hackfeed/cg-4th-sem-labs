"""
    Fish drawing class representation.
"""


from math import pi, sin, cos, sqrt, radians


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

    def reset(self):
        self.__init__()

    def get_body(self, a, b):
        """
            Get fish body dots.
        """

        body = []
        t = 0

        while 2 * pi - t > Fish.eps:
            body.extend([-a*cos(t) + 420, b*sin(t) + 340])
            t += 0.1

        body = body[10:]
        body = body[:len(body)-10]

        return body

    def get_head(self):
        """
            Get fish head dots.
        """

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
        """
            Get fish eye dots.
        """

        head = self.head
        eye = []
        t = 0
        r = 7
        h_r = (head[0] - head[len(head) // 2]) / 2

        while 2 * pi - t > Fish.eps:
            eye.extend([r*cos(t) + head[0] - h_r * 1.5, r*sin(t) + head[1] - h_r * 0.3])
            t += 0.1

        eye.extend([eye[0], eye[1]])

        return eye

    def get_mouth(self):
        """
            Get fish mouth dots.
        """

        head = self.head
        h_r = (head[0] - head[len(head) // 2]) / 2
        mouth = [
            head[0] - h_r * 1.7, head[1] + h_r * 0.3,
            head[0] - h_r * 1.3, head[1] + h_r * 0.3
        ]

        return mouth

    def get_upper_fin(self):
        """
            Get fish upper fin dots.
        """

        body = self.body
        upper_fin = [
            body[len(body)-14], body[len(body)-13],
            body[len(body)-14] + 20, body[len(body) - 13] - 50,
            body[len(body)-28] + 20, body[len(body) - 13] - 50,
            body[len(body)-28], body[len(body)-27]
        ]

        return upper_fin

    def get_lower_fin(self):
        """
            Get fish lower fin dots.
        """

        body = self.body
        lower_fin = [
            body[14], body[15],
            body[14] + 20, body[15] + 50,
            body[28] + 20, body[15] + 50,
            body[28], body[29]
        ]

        return lower_fin

    def get_tail(self):
        """
            Get fish tail dots.
        """

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
        """
            Draw fish to canvas.
        """

        canvas.create_line(*self.body, fill=Fish.body_color, width=2)
        canvas.create_line(*self.head, fill=Fish.limb_color, width=2)
        canvas.create_line(*self.eye, fill=Fish.eye_color, width=2)
        canvas.create_line(*self.mouth, fill=Fish.body_color, width=2)
        canvas.create_line(*self.upper_fin, fill=Fish.limb_color, width=2)
        canvas.create_line(*self.lower_fin, fill=Fish.limb_color, width=2)
        canvas.create_line(*self.tail, fill=Fish.limb_color, width=2)

    def move(self, dx, dy):
        """
            Move model.
        """

        for i in range(0, len(self.body), 2):
            self.body[i] += dx
            self.body[i+1] += dy

        for i in range(0, len(self.head), 2):
            self.head[i] += dx
            self.head[i+1] += dy

        for i in range(0, len(self.eye), 2):
            self.eye[i] += dx
            self.eye[i+1] += dy

        for i in range(0, len(self.mouth), 2):
            self.mouth[i] += dx
            self.mouth[i+1] += dy

        for i in range(0, len(self.upper_fin), 2):
            self.upper_fin[i] += dx
            self.upper_fin[i+1] += dy

        for i in range(0, len(self.lower_fin), 2):
            self.lower_fin[i] += dx
            self.lower_fin[i+1] += dy

        for i in range(0, len(self.tail), 2):
            self.tail[i] += dx
            self.tail[i+1] += dy

    def rotate(self, rx, ry, angle):
        """
            Rotate model.
        """

        cosa = cos(radians(angle))
        sina = sin(radians(angle))

        for i in range(0, len(self.body), 2):
            x = self.body[i]
            y = self.body[i+1]
            self.body[i] = rx + (x - rx) * cosa + (y - ry) * sina
            self.body[i+1] = ry - (x - rx) * sina + (y - ry) * cosa

        for i in range(0, len(self.head), 2):
            x = self.head[i]
            y = self.head[i+1]
            self.head[i] = rx + (x - rx) * cosa + (y - ry) * sina
            self.head[i+1] = ry - (x - rx) * sina + (y - ry) * cosa

        for i in range(0, len(self.eye), 2):
            x = self.eye[i]
            y = self.eye[i+1]
            self.eye[i] = rx + (x - rx) * cosa + (y - ry) * sina
            self.eye[i+1] = ry - (x - rx) * sina + (y - ry) * cosa

        for i in range(0, len(self.mouth), 2):
            x = self.mouth[i]
            y = self.mouth[i+1]
            self.mouth[i] = rx + (x - rx) * cosa + (y - ry) * sina
            self.mouth[i+1] = ry - (x - rx) * sina + (y - ry) * cosa

        for i in range(0, len(self.upper_fin), 2):
            x = self.upper_fin[i]
            y = self.upper_fin[i+1]
            self.upper_fin[i] = rx + (x - rx) * cosa + (y - ry) * sina
            self.upper_fin[i+1] = ry - (x - rx) * sina + (y - ry) * cosa

        for i in range(0, len(self.lower_fin), 2):
            x = self.lower_fin[i]
            y = self.lower_fin[i+1]
            self.lower_fin[i] = rx + (x - rx) * cosa + (y - ry) * sina
            self.lower_fin[i+1] = ry - (x - rx) * sina + (y - ry) * cosa

        for i in range(0, len(self.tail), 2):
            x = self.tail[i]
            y = self.tail[i+1]
            self.tail[i] = rx + (x - rx) * cosa + (y - ry) * sina
            self.tail[i+1] = ry - (x - rx) * sina + (y - ry) * cosa

    def scale(self, sx, sy, kx, ky):
        """
            Scale model.
        """

        for i in range(0, len(self.body), 2):
            self.body[i] = kx * self.body[i] + (1 - kx) * sx
            self.body[i+1] = ky * self.body[i+1] + (1 - ky) * sy

        for i in range(0, len(self.head), 2):
            self.head[i] = kx * self.head[i] + (1 - kx) * sx
            self.head[i+1] = ky * self.head[i+1] + (1 - ky) * sy

        for i in range(0, len(self.eye), 2):
            self.eye[i] = kx * self.eye[i] + (1 - kx) * sx
            self.eye[i+1] = ky * self.eye[i+1] + (1 - ky) * sy

        for i in range(0, len(self.mouth), 2):
            self.mouth[i] = kx * self.mouth[i] + (1 - kx) * sx
            self.mouth[i+1] = ky * self.mouth[i+1] + (1 - ky) * sy

        for i in range(0, len(self.upper_fin), 2):
            self.upper_fin[i] = kx * self.upper_fin[i] + (1 - kx) * sx
            self.upper_fin[i+1] = ky * self.upper_fin[i+1] + (1 - ky) * sy

        for i in range(0, len(self.lower_fin), 2):
            self.lower_fin[i] = kx * self.lower_fin[i] + (1 - kx) * sx
            self.lower_fin[i+1] = ky * self.lower_fin[i+1] + (1 - ky) * sy

        for i in range(0, len(self.tail), 2):
            self.tail[i] = kx * self.tail[i] + (1 - kx) * sx
            self.tail[i+1] = ky * self.tail[i+1] + (1 - ky) * sy
