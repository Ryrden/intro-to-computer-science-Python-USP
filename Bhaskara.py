import math

def delta(a, b, c):
    return (b**2) - (4*a*c)

def main():
    a_digitado = float(input("dado ax²+ bx + c = 0 Defina o valor de a: "))
    b_digitado = float(input("dado ax²+ bx + c = 0 Defina o valor de b: "))
    c_digitado = float(input("dado ax²+ bx + c = 0 Defina o valor de c: "))
    imprime_raizes(a_digitado, b_digitado, c_digitado)

def imprime_raizes(a, b, c):
    if (a != 0 and b != 0 and c != 0): 

        d = delta(a, b, c)
        
        if (d > 0):
            x1 = -b + math.sqrt(d)/2*a 
            x2 = -b - math.sqrt(d)/2*a
            print ("você tem duas raizes distintas")
            print("suas duas raizes são x1 =", x1, "e  x2 =", x2)

        elif (d == 0):
            print("você tem uma raiz dupla")
            print("suas duas raizes são x1 =", x1, "e  x2 =", x2)

        elif (d < 0):
            print("você não tem nenhuma raiz real")
            print("suas duas raizes são x1 =", x1, "e  x2 =", x2)

    else:
        print("0 não é um número valido para uma equação do 2º grau")

main()
