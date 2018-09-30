import math


def closest_mod_5(x):
    if x % 5 == 0:
        return x
    return math.ceil(x / 5) * 5


print(closest_mod_5(11))
