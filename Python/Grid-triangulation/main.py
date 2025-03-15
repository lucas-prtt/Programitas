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
