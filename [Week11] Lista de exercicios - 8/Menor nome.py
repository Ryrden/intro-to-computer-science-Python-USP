def menor_nome(nomes):

    menor_lista = []
    tamanho = len(nomes[0]) #tamanho da 1º palavra da lista

    for i in range(len(nomes)): #percorrendo lista
        
        aux = nomes[i].strip() #variável auxiliar para nome percorrido ++ sem espaços

        if len(aux) < tamanho: #se o tamanho da palavra atual é menor que a primeira da lista
            menor_lista.append(aux)

        tamanho = len(aux) #atualizando tamanho para palavra percorrida (anterior na próxima verificação)

    Nome_final = str(menor_lista[-1].capitalize()) #último nome adicionado na lista com a primeira letra Maiúscula

    return Nome_final





def testa_menor_nome(): #TESTADOR 
    if menor_nome(['maria', 'josé', 'PAULO', 'Catarina']) == 'José':
        print("ok1")

    if menor_nome(['maria', ' josé  ', '  PAULO', 'Catarina  ']) == 'José':
        print("ok2")

    if menor_nome(['Bárbara', 'JOSÉ  ', 'Bill']) == 'José':
        print('ok3')
    
    if menor_nome(['cal', 'feynman', 'richard','zé', 'joão da fazendinha']) == 'zé':
        print('ok3')