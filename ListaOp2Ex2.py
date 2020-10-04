

print("Insira os valores das constantes da equação de segundo grau:\n(Formato: ax^2 + bx + c)")
a = float(input("a:"))
b = float(input("b:"))
c = float(input("c:"))

delta = b**2 - 4*a*c
if delta > 0:
    x1 = (-b+delta**0.5)/(2*a)
    x2 = (-b-delta**0.5)/(2*a)
    if x1>=x2:
        print("as raízes da equação são",x2,"e",x1)
    else:
        print("as raízes da equação são", x1, "e", x2)

elif delta == 0:
    x1 = -b/(2*a)
    print("a raiz desta equação é",x1)
else:
    print("esta equação não possui raízes reais")