def dimensoes(matriz):
    colunas = 0

    linhas = len(matriz)  # Quantas linhas tem

    for i in matriz[0]:  # Quantas colunas tem
        colunas += 1

    return print(linhas, 'X', colunas, sep='') 
