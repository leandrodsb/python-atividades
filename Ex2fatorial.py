#coeficiente binomial

def fatorial (n):
    if n == 0:
        return 1
    elif n > 0:
        return n*fatorial(n-1)

def binomial (n,k):
    return fatorial(n)/(fatorial(k)*fatorial(n-k))

def testeFatorial(i):
    cont = 0
    while (cont<=i):
        print(str(cont)+"! =",fatorial(cont))
        cont+=1

i = 10
print (testeFatorial(i))