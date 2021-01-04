n = 0
m = 0
def usuario_escolhe_jogada(n, m):
    x = m
    x = int(input("Quantas peças você vai tirar? "))
    while  x > m or x > n or x <= 0:
        print("Oops! Jogada inválida! Tente de novo.")
        x = int(input("Quantas peças você vai tirar? "))
  
    print("Você tirou", x, "peças")
    n = n - x
    if n == 0:
        print("Fim do jogo! Você ganhou!")
    return x

def computador_escolhe_jogada(n,m):
    x = m
    if n-x == 0:
        return m

    while x >= 0:
        k = (n-x) % (m+1)
        if k == 0:
            print("o computador tirou", m, "peças")
            return x
        x = x - 1
        if x == 0:
            print("o computador tirou", m, "peças")
            return m
        
    else:
        print("o computador tirou", x, "peças")
        if n == 0: #FINAL DO JOGO
            print("Fim do jogo! O computador ganhou!")
    return x

def partida(n,m):
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    k = n % (m+1)
    if k == 0:
        print("Você começa!")
        valid = True
        while valid:
            ret = usuario_escolhe_jogada(n,m) #chamando usuario
            n = n - ret
            if n == 0:
                print("Fim do jogo! Você ganhou!")
                return False
                
            print("Agora restam", n, "peças no tabuleiro")
            ret2 = computador_escolhe_jogada(n,m) #chamando maquina
            n = n - ret2
            if n == 0:
                print("Fim do jogo! O computador ganhou!")
                return True
                
            print("Agora restam", n, "peças no tabuleiro")
    else:
        print("Computador começa!")
        valid = True
        while valid:
            ret = computador_escolhe_jogada(n,m) #chamando maquina
            n = n - ret
            if n == 0:
                print("Fim do jogo! O computador ganhou!")
                return True
                
            print("Agora restam", n, "peças no tabuleiro")
            ret2 = usuario_escolhe_jogada(n,m) #chamando usuario
            n = n - ret2
            if n == 0:
                print("Fim do jogo! Você ganhou!")
                return False
                 
            print("Agora restam", n, "peças no tabuleiro")

def campeonato(n,m):                                                       #FAZ ISSO OUTRO DIA!!!!!!!!
    PC = 0
    U = 0
    x = partida(n,m) 
    y = partida(n,m)
    z = partida(n,m)

    lista = [x,y,z]

    for i in lista:
        if i == True:
            PC = PC + 1
        else:
            U = U + 1

    return print("Placar: Você", U, "X", PC, "Computador")
    
print("Bem-vindo ao jogo do NIM! Escolha:")
print("1 - para jogar uma partida isolada")
tipo_jogo = int(input("2 - para jogar uma partida campeonato "))

if tipo_jogo == 1: 
    print("voce escolheu uma partida isolada!")
    partida(n,m)
if tipo_jogo == 2:
    print("voce escolheu um campeonato!")
    campeonato(n,m)