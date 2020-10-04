#bhaskara

import math

print("\n--- Formato da equação: a.x^2 + b.x^+ c ----\n")
a = float(input("Insira o valor de a:"))
b = float(input("Insira o valor de b:"))
c = float(input("Insira o valor de c:"))

print("\nEquação: "+str(a)+".X^2 + "+str(b)+".X + "+str(c)+" = 0")
delta = b**2 - 4*a*c

def raizes (a,b, delta):
    if(delta > 0):
        X1 = -b + math.sqrt(delta)/2*a
        X2 = -b - math.sqrt(delta)/2*a
        return print("X1 =",X1,"\nX2 =",X2)
    elif(delta == 0):
        return print("X =", -b/(2*a))
    else:
        return print("Não há raízes reais.")

raizes(a,b,delta)









