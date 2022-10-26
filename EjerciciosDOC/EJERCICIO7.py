# Realizar una función llamada agregar_una_vez(lista, el) que reciba una lista y un elemento. 
# La función debe añadir el elemento al final de la lista con la condición de no repetir ningún elemento. 
# Además, si este elemento ya se encuentra en la lista se debe invocar un error de tipo ValueError 
# que debes capturar y mostrar este mensaje en su lugar: Error: Imposible añadir elementos duplicados => [elemento].
# Cuando tengas la función intenta añadir los siguientes valores a la lista 10, -2, “Hola” y luego muestre su contenido.

elementos = [1, 5, -2]
print(elementos)

# Completa el ejercicio aquí
def agregar_una_vez(lista, elemento):
    if elemento in lista:
        raise ValueError("ERROR: Imposible añadir elementos duplicados => [{}]".format(elemento))
    lista.append(elemento)
    
try:
    agregar_una_vez(elementos, "Hola")
    agregar_una_vez(elementos, 10)
    agregar_una_vez(elementos, -2)
except ValueError as elemento1:
    print(elemento1.args[0])
else:
    print("Elementos agregados correctamente")
finally:
    print("La lista resultante es ", elementos)
#ERROR: Imposible añadir elementos duplicados => [-2]
#La lista resultante es [1, 5, -2, 10]