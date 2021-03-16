class Buscador:
    
    def busca_binaria(self, lista, x):
        primeiro = 0 
        ultimo = len(lista)-1

        while primeiro <= ultimo:
            meio = (primeiro + ultimo ) // 2

            if lista[meio] == x:
                return meio
            elif x < lista[meio]:
                ultimo = meio - 1
            else:
                primeio = meio + 1
        
        return -1
    
    
    def busca_sequencial(self, lista, x):
        for i in range(len(lista)):
            if lista [i] == x:
                return i
        return -1