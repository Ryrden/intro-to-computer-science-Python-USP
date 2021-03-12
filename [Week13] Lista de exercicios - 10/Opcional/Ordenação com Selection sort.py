def ordena(lista):

    Endlist = len(lista)

    for i in range(Endlist-1):

        Menor_posição = i

        for j in range(i+1, Endlist):
            if lista[j] < lista[Menor_posição]:
                Menor_posição = j

        lista[i], lista[Menor_posição] = lista[Menor_posição], lista[i]

    return lista


# Verificação
if __name__ == "__main__":

    import Listas_grandes

    lista = Listas_grandes.lista_grande(10)

    print(
        f"Antes de ser Ordenada \t-> {lista}\n\n"
        f"Depois de ser Ordenada \t-> {ordena(lista)}"
    )
