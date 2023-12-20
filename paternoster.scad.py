import sys
from solid import *
from pathlib import Path
import solid
from solid.utils import *
import math
import math
import os

from solidpython_ff import *
import collections

# that's from https://github.com/rcolyer/threads-scad
use("../threads-scad/threads.scad")
r_m3 = 1.7 # how big are the wholes for an m3 screw


outer_diam = 125 + 20
h = 7
spoke_w = 7


def ring(r, h):
    a = circle(r=h).left(r)
    return rotate_extrude(segments=150)(a)


def modela():
    a = (
        cy(r=outer_diam / 2, h=h, segments=150)
        + ring(r=outer_diam / 2, h=2.5).color("blue").h()
    )
    outer = a - cy(r=outer_diam / 2 - 5, h=h + 1, segments=150).color("red")
    inner = (
        cy(r=11 + 5, h=h, segments=150)
        - cy(r=11.1, h=h + 1).hole()
        + cy(11 + 2, h=1).color("red").up(h / 2 + 0.5)
        - cy(r=11.1 - 0.5, h=h + 5).hole()
    )
    spokes = union()
    for ii in range(0, 360, 60):
        spokes += q(outer_diam, h, spoke_w).rotate(0, 0, ii).color("green")
    return outer + inner + spokes


def modelb():

    a = q(22, 22, 44)
    a -= cy(4.5, 100).rotate(0, 90, 0).up(44 / 2 - 22 / 2).d()
    a -= cy(4.5, 100).rotate(90, 00, 0).down(44 / 2 - 22 / 2).d()
    return a


def modelc():
    x = 3
    a = q(22 + 2 * x, 22 + 2 * x, 22)
    a -= q(21.5, 21.5, 100).hole()
    a -= cy(2.8, 100).rotate(0,90,0)
    b = hull()(q(22 + 2 * x, 3, 22), cy(4 + x, 22+2*x).rotate(0, 90, 0).back(5))
    b += cy(4 + x, 22+2*x+4).rotate(0, 90, 0).back(5).left(2)
    b += cy(4 + 1, 22+2*x+5).rotate(0, 90, 0).back(5).left(2.5)
    b -= cy(4.2, h=100).rotate(0,90,0).back(5).h()
    return a + b.back(22-11+1.5).color('blue')


dump(modela(), "pulley.scad")
dump(modelb(), "quer.scad")
dump(modelc(), "wheel_attach.scad")
print("done")
