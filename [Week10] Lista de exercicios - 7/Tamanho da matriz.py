def dimensoes(matriz):
    colunas = 0

    linhas = len(matriz)  # Quantas linhas tem

    for i in [x[0] for x in matriz]:  # Quantas colunas tem
        colunas += 1

    return print(linhas, 'X', colunas, sep='')
