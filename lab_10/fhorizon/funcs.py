from math import sin, cos, sqrt

funcs = {
    "sin^2(x) + cos^2(z) - y = 0": lambda x, z: sin(x)**2 + cos(z)**2,
    "sqrt(|sin(cos(x))|) + z / 2 - y = 0": lambda x, z: sqrt(abs(sin(cos(x)))) + z / 2,
    "sin(x) - cos(x) + x*z - y = 0": lambda x, z: sin(x) - cos(z) + x*z
}
