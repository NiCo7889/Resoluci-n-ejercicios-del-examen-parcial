"""
Ejercicio 5
Crea un script llamado descomposicion.py que realice las siguientes tareas:
Debe tomar 1 argumento que será un número entero positivo.
En caso de no recibir un argumento, debe mostrar información acerca de cómo utilizar el script.
El objetivo del script es descomponer el número en unidades, decenas, centenas, miles... tal que por ejemplo si se introduce el número 3647:
python descomposicion.py 3647
 
El programa deberá devolver una descomposición línea a línea como la siguiente utilizando las técnicas de formateo:
0007
0040
0600
3000
Pista
Que el valor sea un número no significa necesariamente que deba serlo para formatearlo. 
Necesitarás jugar muy bien con los índices y realizar muchas conversiones entre tipos cadenas, números y viceversa
"""

print("Introduce un número entero positivo de 4 cifras para que sea descompuesto")

num = input("Tu número: ")
if len(num) != 4:
    print("Tu número no es válido")
else:
    for c in range(3, -1, -1):
        res = num[c]
        if c == 0:
            n ="1000"
            m = n.replace("1", res)
            print(m)
        elif c == 1:
            n ="0100"
            m = n.replace("1", res)
            print(m)
        elif c == 2:
            n ="0010"
            m = n.replace("1", res)
            print(m)
        elif c == 3:
            n ="0001"
            m = n.replace("1", res)
            print(m)

# No está resuelto de forma completamente correcta pero cumple con su función