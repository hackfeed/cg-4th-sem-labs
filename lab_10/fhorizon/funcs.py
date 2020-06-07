from math import sin, cos, pi

funcs = {
    "func1": lambda x, z: sin(x) * sin(z),
    "func2": lambda x, z: sin(cos(x) * sin(z)),
    "func3": lambda x, z: cos(x) * z / 3
}
