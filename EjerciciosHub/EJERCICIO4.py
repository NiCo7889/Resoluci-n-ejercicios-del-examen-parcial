"""
Durante la planificación de un proyecto se han acordado una lista de tareas. 
Para cada una de estas tareas se ha asignado un orden de prioridad (cuanto menor es el número de orden, más prioridad).
¿Eres capaz de crear una estructura del tipo cola con todas las tareas ordenadas pero sin los números de orden?

Sugerencia:
Para ordenar automáticamente una lista es posible utilizar el método .sort(), deberias probarlo.
"""
def ordenar(c):
    return c['prioridad']

cola = [
    {'tarea2' : 'comprar', 'prioridad' : '2'},
    {'tarea1' : 'Python', 'prioridad' : '1'},
    {'tarea4' : 'comer', 'prioridad' : '4'},
    {'tarea3' : 'jugar', 'prioridad' : '3'},
]

cola.sort(key=ordenar)
print(cola[0]['tarea1'], cola[1]['tarea2'], cola[2]['tarea3'],cola[3]['tarea4'])

cola=["tarea4", "tarea2","tarea5","tarea3","tarea1"]

cola.sort()