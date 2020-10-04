def maior_primo(num):
    nao_primo = True
    j = 2
    while nao_primo:
        if num % j==0 and num != 2:
            nao_primo = True
            num -= 1
            j = 2
        elif j == num-1 and num % j != 0 or num == 2:
            primo = num
            nao_primo = False
        else:
            j = (j + 1)

    return primo

print(maior_primo(100))