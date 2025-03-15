from PIL import Image
import triangulation as Tr

im = Image.new("RGB", (1024, 1024))

def reset(size):
    im = Image.new("RGB", size)
def paint(position, color):
    im.putpixel(position, color)
def line(slope, offset, color):
    for x in range(0, im.width):
        paint((x, min(Tr.evaluate(x, slope, offset), im.height-1)), color)

line(3, 400, (255, 0, 0))

im.show()