num = int(input("Digite o valor de n:"))
EndProcess = False
fatorial = 1

while not EndProcess:
    if (num == 0):
        EndProcess = True
    else:
        fatorial = num*fatorial
        num=num-1

print(fatorial)