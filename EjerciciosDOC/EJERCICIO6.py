#Realiza una función separar(lista) que toma una lista de números enteros y devuelve dos listas ordenadas. 
#la primera con los números pares y la segunda con los números impares.
#Para ordenar una lista automáticamente puedes utilizar el método sort()
lista = [17, 24, 2, 13, 5, 4, 6, 1, 89, 0, 3, 7, 55, 25, 30, 8, 68, 156]

def separar(lista):
    pares = []
    impares = []

    for num in lista:
        if num%2 == 0:
            pares.append(num)
        else:
            impares.append(num)
         
    pares.sort()
    impares.sort()
 
    return pares, impares
 
pares, impares= separar(lista)
print('Pares: ', pares)
print('Impares: ', impares)


#otra

lista=[76,3,2,45,32,12,43,1,2,3,4,5,6,7,8,6,3,6,7,3,0]

def separar():
    pares=[]
    impares=[]
    for i in lista:
        if i%2==0:
            pares.append(i)
        else:
            impares.append(i)
    pares.sort()
    impares.sort()
    return pares, impares

pares, impares = separar()
print("lista de pares: ", pares)
print("lista de impares: ", impares)

