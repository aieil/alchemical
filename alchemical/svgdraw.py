#it draws circles and lines
import hashlib
from re import sub

uniwidth=0.5
unicol="red"
size_x=100
size_y=100

#gets and sets because who knows why
def set_size(x, y):
    global size_x, size_y
    size_x = x
    size_y = y

def get_size():
    return (size_x, size_y)

def set_col(new_col):
    global unicol
    unicol = new_col

def get_col():
    return unicol

def set_width(new_width):
    global uniwidth
    uniwidth = new_width

def get_width():
    return uniwidth

#base lines required for svg
def svg_base():
    return ["<?xml version='1.0'?>",
            "<svg width='%d' height='%d' viewPort='0 0 %d %d' version='1.1'>" 
            % (size_x, size_y, size_x, size_y),
            "</svg>"]

#outputs svg to file
def write_svg(svg_ls):
    svg_st = '\n'.join(svg_ls)
    svg_code = str(hashlib.md5(svg_st.encode('utf-8')).digest())
    svg = open(sub('[\W_]', '', svg_code)[1:] + ".svg", 'w')
    svg.write(svg_st)

#adds a line to the svg list
def svg_insert_line(svg_ls, x, y, mag, angle):
    #starts with a horizontal line and rotates from there
    svg_insert(svg_ls, '<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" \
stroke-width="%f" transform="rotate(%d %d %d)"/>'
            % (x, y, x, y + mag, unicol, uniwidth, angle, x, y))

#adds a circle to the svg list
def svg_insert_circle(svg_ls, x, y, mag):
    svg_insert(svg_ls, "<circle cx='%d' cy='%d' r='%d' stroke='%s' \
stroke-width='%f' fill='none'/>"
            % (x, y, mag, unicol, uniwidth))

#adds a line (of text) to the svg list
def svg_insert(svg_ls, line):
    svg_ls.insert(-1, line)
