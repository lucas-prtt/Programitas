from PIL import Image

im = Image.new("RGB", (1024, 1024))

def reset(size):
    im = Image.new("RGB", size)
def paint(position, color):
    im.putpixel((position[0], im.height-position[1]-1), color)
def line(slope, offset, color):
    for x in range(0, im.width):
        pos = (x, x * slope + offset)
        if pos[1] <= im.height:
            paint(pos, color)
def shape(center, radius, color, condition):
    for x in range(center[0] - radius, center[0] + radius):
        for y in range(center[1] - radius, center[1] + radius) :
            if condition(x, y):
                paint((x, y), color)
def square(center, radius, color):
    shape(center, radius, color, lambda x, y : True)
def diamond(center, radius, color):
    shape(center, radius, color, lambda x, y : manhattanDistance(center, (x, y))<radius)
def circle(center, radius, color):
    shape(center, radius, color, lambda x, y : distance(center, (x, y))<radius)
def cross(center, color):
    for x in range(0, im.width):
        paint((x, center[1]), color)
    for y in range(0, im.height):
        paint((center[0], y), color)


def manhattanDistance(vector1, vector2):
    return abs(vector1[0] - vector2[0]) + abs(vector1[1] - vector2[1])

def distance(vector1, vector2):
    return ((vector1[0] - vector2[0])**2 + (vector1[1] - vector2[1])**2)**0.5

"""
line(3, 400, (255, 0, 0))
square((400, 400), 10 , (200, 0, 140))
diamond((700, 700), 20, (40, 240, 20))
circle((200, 200), 30, (130, 130, 170))
cross((500, 500), (255, 255, 255))
im.show()
"""
