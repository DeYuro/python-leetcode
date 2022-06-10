import math

scale = 0.5


def drink(time):
    litres = time * scale
    return math.floor(litres)


print(drink(3))
print(drink(6.7))
print(drink(11.8))
