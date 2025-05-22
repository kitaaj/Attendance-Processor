import math


radii = [3,5,7]
for radius in radii:
     circumference = 2 * math.pi * radius
     print ( f"Radius {radius}: Circumference = {circumference:.2f}")


def circumference(r):
    r=3
    s=2*r*3.14
    print(s)

    r=5
    s=2*r*3.14
    print(s)

    r=7
    s=2*r*3.14
    print(s)
