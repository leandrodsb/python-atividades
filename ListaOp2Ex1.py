import math

print("Coordenadas 1:")
x1 = float(input("X1 = "))
y1 = float(input("Y1 = "))

print("Coordenadas 2:")
x2 = float(input("X2 = "))
y2 = float(input("Y2 = "))

d = math.sqrt((x1-x2)**2+(y1-y2)**2)

if d>=10:
    print("longe")
else:
    print("perto")