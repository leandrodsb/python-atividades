def usuario_escolhe_jogada(n, m):
    num = int(input("Quantas peças você vai tirar?\n"))
    while num<1 or num>m or num>n:
        num = int(input("\nOops! Jogada inválida! Tente de novo.\n"))
    return num

def computador_escolhe_jogada(n, m):
    cont = m
    while cont >= 1:
        if (n - cont)%(m+1) == 0:
            num = cont
            break
        elif (cont == 1):
            num = m
        cont-=1
    return num

def partida():
    n = int(input("Quantas peças?"))
    while(n<1):
        n = int(input("\nValor inválido. Insira novamente.\nQuantas peças?"))
    m = int(input("Limite de peças por jogada?"))
    while (m < 1):
        m = int(input("\nValor inválido. Insira novamente.\nLimite de peças por jogada?"))
        
    if n%(m+1)==0:
        print("\nVocê começa!\n")
        jogada = 1
    else:
        print("\nComputador começa!\n")
        jogada = 2

    winner = False

    while(not winner):

        if jogada%2 != 0:
            escolha = usuario_escolhe_jogada(n, m)
            print("Você tirou uma peça.")

        elif jogada%2 == 0:
            escolha = computador_escolhe_jogada(n, m)
            print("O computador tirou uma peça.")

        n = n - escolha
        if n == 0:
            winner = True
            if jogada%2 != 0:
                print("Fim do jogo! Voce ganhou!\n")
                return True

            else:
                print("Fim do jogo! O computador ganhou!\n")
                return False

        elif n == 1:
            print("Agora resta apenas uma peça no tabuleiro.\n")
        else:
            print("Agora restam", n, "peças no tabuleiro.\n")
        jogada += 1

def campeonato():
    cont = 1
    placar_cpu = 0
    placar_usuario = 0
    while (cont <= 3):
        print("**** Rodada", cont, "****")
        x = partida()
        cont += 1
        if x == True:
            placar_usuario += 1
        elif x == False:
            placar_cpu += 1

    print("\n**** Final do campeonato! ****\n")
    print("Placar: Você",placar_usuario,"X",placar_cpu," Computador")

def main():
    print("Bem - vindo ao jogodo NIM! Escolha:")
    op = int(input("\n1 - para jogar uma partida isolada.\n2 - para jogar um campeonato.\n"))

    while (op != 1 and op != 2):
        print("\nOpção inválida. Insira novamente.\n")
        op = int(input("\n1 - para jogar uma partida isolada.\n2 - para jogar um campeonato.\n"))

    if op == 1:
        print("\nVoce escolheu partida isolada!\n")
        partida()

    elif op == 2:
        print("\nVoce escolheu um campeonato!\n")
        campeonato()

main()

