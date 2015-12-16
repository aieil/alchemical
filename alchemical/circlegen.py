import sys
from math import sqrt
from alchemizer import *
from svgdraw import *

#finds the greatest magnitude in a circle
#magnitude of n is truncated n/maginum
def greatest_mag(circle):
    greatest = 0

    for e in circle:
        if e[1] > greatest:
            greatest = e[1]

    return greatest

#finds the average magnitude of a circle
def average_mag(circle):
    total = 0

    for e in circle:
        total += e[1]

    return float(total)/len(circle)

#converts a list of base maginum integers to a valid circle
#the digit of least order is kept while the remaining digits are converted
#to base 10 to be used in an svg file
def circleconvert(transmutation):
    return [(e[0], base_ten(e[1:])) if len(e) > 1 \
            else (e[0], 0) if len(e) == 1 else (0, 0) for e in transmutation]

#converts a valid circle back into the base maginum representation
def transconvert(circle):
    return [[e[0]] + base_magi(e[1]) if e[1] > 0 else e[0] if e[0] > 0 else [] \
            for e in circle]

#places gets coordinates for all the values of a circle in a spiral pattern
#and the size of the svg file
#  ____
# | __ ||
# || _|||
# ||__//
# |___|
def place_circle(circle, gmag):
    incr = 4 #used to set the distance between points
    size = (average_mag(circle)/2) * incr + gmag
    centre = size/2
    cursor = [centre, centre]
    placements = [cursor[:]]
    setting = 0

    #moves cursor in a squared spiral pattern, layering out at each iteration
    #which is the square of an odd number
    for i in range(1, len(circle)):
        if (setting == 0):
            cursor[0] += incr
            setting = 1
        elif (setting == 1):
            if (sqrt(i) == int(sqrt(i)) and sqrt(i) % 2 == 1):
                cursor[0] += incr
            
            cursor[1] -= incr

            if ([cursor[0] - incr, cursor[1] + incr] in placements and
                    [cursor[0] - incr, cursor[1]] not in placements):
                setting = 2
        elif (setting == 2):
            cursor[0] -= incr

            if ([cursor[0] + incr, cursor[1] + incr] in placements and
                    [cursor[0], cursor[1] + incr] not in placements):
                setting = 3
        elif (setting == 3):
            cursor[1] += incr

            if([cursor[0] + incr, cursor[1] - incr] in placements and
                    [cursor[0] + incr, cursor[1]] not in placements):
                setting = 4
        else:
            cursor[0] += incr

            if([cursor[0] - incr, cursor[1] - incr] in placements and
                    [cursor[0], cursor[1] - incr] not in placements):
                setting = 1

        placements.append(cursor[:])
                    
    return placements, size

#given a circle and positions for all the points, outputs svg
def make_svg(circle, placements):
    svg = svg_base()

    angles = (0, 45, 90, 135, 180, 225, 270, 315)

    for i in range(len(circle)):
        if circle[i][0] == 0:
            svg_insert_circle(svg, placements[i][0], placements[i][1], \
                    int(circle[i][1] / 2))
        else:
            svg_insert_line(svg, placements[i][0], placements[i][1], \
                    circle[i][1], angles[circle[i][0] - 1])

    write_svg(svg)

def main():
    f = sys.argv[1]

    transmutation = alchemize(get_reagents(f))

    circle = circleconvert(transmutation)

    gmag = 2 * greatest_mag(circle)
    
    scirc = place_circle(circle, gmag)
    
    set_size(scirc[1], scirc[1])
    set_width(0.2)

    make_svg(circle, scirc[0])
    
main()
