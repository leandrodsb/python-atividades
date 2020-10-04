num = int(input("Insira um número inteiro:"))
soma = 0

while num%10 != 0 or num//10 != 0:
    soma += num%10
    num = num//10

print(soma)
