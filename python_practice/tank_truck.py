"""
To introduce the problem think to my neighbor who drives a tanker truck. The
level indicator is down and he is worried because he does not know if he will
be able to make deliveries. We put the truck on a horizontal ground and
measured the height of the liquid in the tank.

Fortunately the tank is a perfect cylinder and the vertical walls on each end
are flat. The height of the remaining liquid is h, the diameter of the cylinder
is d, the total volume is vt (h, d, vt are positive or null integers). You can
assume that h <= d.

Could you calculate the remaining volume of the liquid? Your function
tankvol(h, d, vt) returns an integer which is the truncated result (e.g floor)
of your float calculation.

Examples:

tankvol(40,120,3500) should return 1021 (calculation gives: 1021.26992027)

tankvol(60,120,3500) should return 1750

tankvol(80,120,3500) should return 2478 (calculation gives: 2478.73007973)
"""

import math


def tankvol(h, d, vt):
    # Circle variables to solve for circle area
    radius = d / 2
    height_liquid = h
    circle_area = math.pi * (radius**2)

    # triangle variables to solve for triangle area
    side_c = radius
    side_b = radius - height_liquid
    side_a = math.sqrt(side_c**2 - side_b**2)
    triangle_area = (((radius - height_liquid) * (side_a * 2)) / 2)

    # angle variables to solve for slice area
    angle_a = (side_b**2 + side_c**2 - side_a**2) / (2 * side_b * side_c)
    key_angle = math.degrees(math.acos(angle_a)) * 2  # angle of triangle top
    slice_percent = (key_angle / 360) * 100
    slice_area = (circle_area * .01) * slice_percent

    # calculating liquid(h) percentage of circle
    flat_liquid = slice_area - triangle_area
    liquid_percent = (flat_liquid / circle_area) * 100

    # calculate final volume of liquid(h) in cylinder(vt)
    liquid_volume = (vt / 100) * liquid_percent
    print('liquid volume: ', round(liquid_volume))


tankvol(40, 120, 3500)
tankvol(80, 120, 3500)
tankvol(5, 7, 3848)
