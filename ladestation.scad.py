import sys
from solid import *
from pathlib import Path
import solid
from solid.utils import *
import math
import math
import os

openscad_path = "/sync/hobby_reprap/models/openscad/"
# sys.path.insert(0, openscad_path)
from solidpython_ff import *
import collections

use(os.path.join(openscad_path, "../threads-scad/threads.scad"))
# use(os.path.join(openscad_path, "roundCornersCube.scad"))
# use(os.path.join(openscad_path, "nuts_and_bolts.scad"))
# use(os.path.join(openscad_path, "Nema17.scad"))
r_m3 = 1.7


outer_diam = 20


def modela():
    platten_h = 2
    hole_h = 5
    c = (
        ScrewHoleX(
            outer_diam,
            hole_h + 10,
            position=[0, 0, 0],
            rotation=[0, 0, 0],
            pitch=0,
            tooth_angle=30,
            tolerance=0.8,
            tooth_height=0,
        )
        .down(platten_h)
        .rotate(0, 0, -10)
    )
    c += cy(outer_diam / 2, 20).down(hole_h / 2 + 10 - 0.5)
    b = cy(outer_diam / 2 + 2, hole_h).up(hole_h / 2)
    a = q(25, 25, platten_h).down(platten_h / 2)
    part = b + c.hole() + a
    w = 30 * 4 + 10
    plate = (
        cy(40, h=platten_h)
        - cy(r=1.8, h=100).right(w / 2 - 6).forward(11)
        - cy(r=1.8, h=100).right(w / 2 - 6).back(11)
        - cy(r=1.8, h=100).left(w / 2 - 6).forward(11)
        - cy(r=1.8, h=100).left(w / 2 - 6).back(11)
    )

    ads = union()
    d = 16 + 2
    count = 5
    for xx in range(count):
        for yy in range(count):
            ads += one_ad().right(xx * d).forward(yy * d)
    ads = ads.rotate(0, 0, -45).left(count * d / 2 + d / 4 + 1).back(d / 2)
    ads = intersection()(ads, plate).color("blue")

    out = ads.down(platten_h / 2 + 1.5) + plate.down(platten_h / 2)
    for i in range(4):
        out += (
            part.left(22).rotate(0, 0, i * 90).down(platten_h / 2 - 1).color("purple")
        )
    return out


def one_ad():
    z = 2
    w = 32
    h = 1
    ad = q(z, w, h).forward(w / 2 - z / 2)
    ad += ad.rotate(0, 0, 90)
    for ii in range(4):
        ad += ad.left(2 * z * ii).forward(2 * z * ii)
    ad = ad.forward(z / 2).left(z / 2)
    ad = intersection()(ad, q(w, w, h + 0.01))
    # ad = ad.rotate(0,0,-45)
    return ad


def modelb():
    th = 10 + 4
    a = ScrewThread(
        outer_diam - 0.5,
        10,
        pitch=0,
        tooth_angle=30,
        tolerance=0.8,
        tip_height=0,
        tooth_height=0,
        tip_min_fract=0,
    )
    h = 4
    b = cy(23 / 2.0, h - 1, segments=6).down((h - 1) / 2)
    b += cy(r1=23 / 2.0 - 2, r2=23 / 2.0, h=1, segments=6).down((h - 1) / 2 + 2)

    c = (hull()(cy(3, h=th + 0.1), cy(2.5, r2=3, h=th + 0.1).left(10)).up(th / 2 - h),)
    hx = 2
    c += (
        hull()(cy(r1=3, r2=5, h=hx), cy(r1=2.5, r2=5, h=hx).left(4)).up(
            th - h - hx / 2 + 0.01
        ),
    )
    c += (
        hull()(cy(r1=5, r2=2, h=hx), cy(r2=2.5, r1=5, h=hx).left(10)).down(
            h - hx / 2 + 0.01
        ),
    )
    return a + b - c


def modelc_aa():
    aa = cy(14.0 / 2, h=50.5)
    a = cy(2.5, 54 - 0.5).down(0.25)
    a -= q(2, 20, 6).up(20)
    a -= q(2, 20, 6).down(20)
    h = 2
    out = 14.0 / 2 + 2.5
    b = hull()(
        cy(2.5, h),
        cy(3.5, h).right(out),
    )
    a += (
        (b - cy(6 / 2, 1).down(h / 2 - 0.5 + 0.01).right(out).d())
        .up(50.5 / 2 + h / 2)
        .down(0.5)
    )
    a += b.up(50.5 / 2).down(50.5 + h / 2)
    return a  # + aa.color("blue").right(7.5)


def modelc_aaa():
    bh = 44.25
    bd = 10.35
    aa = cy(bd / 2, h=bh)
    w = 2.5
    a = cy(w, bh)
    a -= q(2, 20, 6).up(bh / 4)
    a -= q(2, 20, 6).down(bh / 4)
    h = 2
    out = bd / 2 + 2.5
    b = hull()(
        cy(w, h),
        cy(w + 1, h).right(out),
    )
    id = 4
    a += (b - cy(id / 2, 1).down(h / 2 - 0.5 + 0.01).right(out).d()).up(bh / 2 + h / 2)
    a += b.down(bh / 2 + h / 2)
    return a  # + aa.color("blue").right(7.5)


dump(modela(), "platte.scad")
dump(modelb(), "schraube.scad")
dump(modelc_aaa(), "cable.scad")
print("done")
# dump(trichter(), "guide.scad")
