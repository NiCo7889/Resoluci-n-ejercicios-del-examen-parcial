lista = [17, 24, 2, 13, 5, 4, 6, 1, 89, 0, 3, 7, 55, 25, 30, 8, 68, 156]

def separar(lista):
    pares = []
    impares = []

    for n in lista:
        if n%2 == 0:
            pares.append(n)
        else:
            impares.append(n)
         
    pares.sort()
    impares.sort()
 
    return pares, impares
 
pares, impares= separar(lista)
print('Pares: ', pares)
print('Impares: ', impares)