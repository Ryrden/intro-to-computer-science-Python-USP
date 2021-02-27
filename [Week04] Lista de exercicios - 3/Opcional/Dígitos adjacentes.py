valor = int(input("Digite um valor: "))

aux = 0

while valor >= 1:
    x = valor % 10
    k = valor // 10
    y = k % 10
    valor = valor // 10
    if x == y:
        aux = 1

if (aux == 1):
    print("sim")
else:
    print("não")