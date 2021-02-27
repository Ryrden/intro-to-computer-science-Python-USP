def é_hipotenusa(h):
    ca = 1
    co = 1
    while h > ca:
        while h > co:
            if h**2 == ca**2 + co**2: 
                return True
            co = co + 1
        co = 1
        ca = ca + 1
    return False

def soma_hipotenusas(x):
    soma = 0

    while x > 1:
        k = é_hipotenusa(x)
        
        if k == True:
            soma = soma + x
            
        x = x - 1

    return soma

