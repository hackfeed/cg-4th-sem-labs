import time
import colorutils as cu


def hex_to_dec(hex):
    return (int(hex[1:3], 16), int(hex[3:5], 16), int(hex[5:7], 16))


def fill(root):
    delay = root.modelst.get(root.modelst.curselection()[0])
    if delay == "С задержкой":
        delay = True
    else:
        delay = False

    color = hex_to_dec(root.color)

    while root.stack:
        point = root.stack.pop()
        root.image.put(root.color, (point[0], point[1]))

        x, y = point[0] + 1, point[1]
        while root.image.get(x, y) != color:
            root.image.put(root.color, (x, y))
            x += 1
        rx = x - 1

        x = point[0] - 1
        while root.image.get(x, y) != color:
            root.image.put(root.color, (x, y))
            x -= 1
        lx = x + 1

        sign = [1, -1]

        for i in sign:
            x = lx
            y = point[1] + i

            while x <= rx:
                is_exist = False
                while root.image.get(x, y) != color and x <= rx:
                    is_exist = True
                    x += 1
                if is_exist:
                    root.stack.extend([[x - 1, y]])
                    is_exist = False
                xi = x
                while root.image.get(x, y) != color and x <= rx:
                    x += 1
                if x == xi:
                    x += 1

        if delay:
            time.sleep(0.01)
            root.canvas.update()
