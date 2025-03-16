import utils.graphics as Gr
import utils.triangulation as Tr

x1 = int(input("Input x value of first position "))
y1 = int(input("Input y value of second position: "))
ang1 = int(input("Input first angle measured: "))
x2 = int(input("Input x value of second position: "))
y2 = int(input("Input y value of secondo position: "))
ang2 = int(input("Input second angle measured: "))

result = Tr.triangulate(x1, y1, ang1, x2, y2, ang2)
print("Objective found at ({:.1f} ; {:.1f})".format(result[0], result[1]))

def drawLine(origin, ang, color):
    Gr.line(Tr.slope(ang), Tr.offset(origin[0], origin[1], Tr.slope(ang)), color)

def v2Sum (v1, v2):
    return(v1[0] + v2[0], v1[1] + v2[1])

def vectorSize(vector):
    return Gr.distance((0, 0), vector)

size = max([vectorSize((x1, y1)), vectorSize((x2, y2)), vectorSize(result)]) + 30
Gr.reset((round(size+50), round(size+50)))

offset = Gr.center()

def applyOffset(vector):
    return v2Sum(vector, offset)

drawLine(applyOffset((x2, y2)), ang2, (200, 200, 200))
drawLine(applyOffset((x1, y1)), ang1, (200, 200, 200))
Gr.cross(offset, (255, 255, 255))
Gr.square(applyOffset((x1, y1)), round(size/50)+1, (200, 0, 0))
Gr.square(applyOffset((x2, y2)), round(size/50)+1, (200, 0, 0))
Gr.diamond(applyOffset(result), round(size/30)+2, (50, 140, 230))
Gr.show()