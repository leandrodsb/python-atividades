

print("Insira os valores das constantes da equação de segundo grau:\n(Formato: ax^2 + bx + c)")
a = float(input("a:"))
b = float(input("b:"))
c = float(input("c:"))

delta = b**2 - 4*a*c
if delta > 0:
    x1 = (-b+delta**0.5)/(2*a)
    x2 = (-b-delta**0.5)/(2*a)
    print("Raízes da equação:\nX1 =",x1,"\nX2 =",x2)
elif delta == 0:
    x1 = -b/(2*a)
    print("Raíz da equação:\nX =",x1)
else:
    print("Não há raízes reais para a equação.")