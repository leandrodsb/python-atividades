print("Entre com 3 valores em ordem crescente.")
n1 = int(input("Valor 1:"))
n2 = int(input("Valor 2:"))
n3 = int(input("Valor 3:"))

if(n3>=n2 and n2>=n1):
    print("crescente")
else:
    print("não está na ordem crescente")