from math import pi


def function1(name):
    print('My name is %s' %name)

def circle_area(r):
    A = pi*r**2
    return A

def cyl_volume_circumference (r,h):
    Volume = pi*r**2*h
    circumference = 2*pi*r*h
    adade_pi = pi
    return Volume, circumference