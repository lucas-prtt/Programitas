import math
##                  ^
## \                I                   /
##     \            I              /
##        \-angle   I angle  /
##             \    I   /
##                  X
##


def triangulateVectors(v1, angle1, v2, angle2):
    return triangulate(v1[0], v1[1], angle1, v2[0], v2[1], angle2)
def triangulate(x1, y1, angle1, x2, y2, angle2):
    def isAngleValid(angle):
        return angle <=180 and angle >= -180
    if not isAngleValid(angle1) or not isAngleValid(angle2):
        raise Exception("Angles must be between -180 and 180 degrees")

    if x1 == x2 and y1 == y2:
        return (x1, y1)

    if angle1 == angle2:
        raise Exception("Paralell lines never cross on euclidean geometry")
    elif isVertical(angle1) or isVertical(angle2):
        if isVertical(angle1):
            return triangulateWithVerticalLine(x1, x2, y2, angle2)
        else:
            return triangulateWithVerticalLine(x2, x1, y1, angle1)
    else:
        
        # a * x + b = y
        a1 = slope(angle1)
        a2 = slope(angle2)

        # b = y - a * x
        b1 = offset(x1, y1, a1)
        b2 = offset(x2, y2, a2)

        # a1 x + b1 = a2 x + b2
        # (a1 - a2) x = b2 - b1
        # x = (b2 - b1) / (a1 - a2)

        rx = (b2 - b1) / (a1 - a2)
        ry = evaluate(rx, a1, b1)
        return (rx , ry)

def triangulateWithVerticalLine(xvertical, x, y, angle):
    a2 = slope(angle)
    b2 = offset(x, y, a2)
    return (xvertical, evaluate(xvertical, a2, b2))

def isVertical(angle):
    return angle == 0 or angle == 180

def slope(angle):
    return 1 / math.tan(math.radians(angle))

def offset(x, y, slope):
    return y - x * slope

def evaluate(x, slope, offset):
    return x * slope + offset
