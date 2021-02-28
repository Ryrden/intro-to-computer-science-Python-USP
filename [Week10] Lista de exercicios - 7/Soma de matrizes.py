def soma_matrizes(m1, m2):

    if len(m1) == len(m1):

        if len(m1[0]) == len(m2[0]):
            lista_final = []
            lista_transporte = []

            for i in range(len(m1)):

                for j in range(0, (len(m1[i]))):
                    aux = 0
                    aux = m1[i][j] + m2[i][j]
                    lista_transporte.append(aux)
                lista_final.append(lista_transporte)
                lista_transporte = []

            return lista_final

        else:
            return False
    else:
        return False


m1 = [[1, 2, 3], [4, 5, 6]]
m2 = [[2, 3, 4], [5, 6, 7]]

soma_matrizes(m1, m2)
