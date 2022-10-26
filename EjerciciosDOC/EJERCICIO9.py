#Crea una función modificar() que a partir de una lista de números realice las siguientes tareas sin modificar la original:
#Borrar los elementos duplicados
#ordenar la lista de mayor a menor
#eliminar todos los números impares
#     realizar una suma de todos los números que quedan     
#añadir como primer elemento de la lista la suma realizada
#devolver la lista modificada
#finalmente, después de ejecutar la función, comprueba que la suma de todos los números a partir del segundo, 
# concuerdan con el primer número de la lista tal que así:

lista = [17, 24, 2, 13, 5, 5, 5, 4, 6, 1, 89, 0, 3, 7, 55, 25, 30, 8, 68, 156, 7, 13, 68]
print("Esta es la lista original: ", lista)
print("\n\n")

def modificar():
  lista1=list(set(lista))
  print("Esta es la lista sin los números repetidos:", lista1)
  print("\n\n")

  lista1.sort(reverse=True)
  print("Esta es la lista ordenada de mayor a menor:", lista1)
 
  print("\n\n")

  lista2=[]
  for n in lista1:
    if n % 2 == 0:
      lista2.append(n)
    else:
      pass

  print("Esta es la lista sin impares y ordenada de mayor a menor:", (lista2))

  print("\n\n")

  sumalista2= sum(lista2)
  print("La suma de los elementos de la lista sin impares es:",           sumalista2)

  print("\n\n")

  lista2.append(sumalista2)
  lista2=sorted(lista2, reverse=True)

  print("Esta es la lista con el valor de la suma como primer elmento de la lista:",lista2)
  print("\n\n")

  print("*",lista2[0]==sum(lista2[1:]),"*")

modificar()


