#Un día el viento soplaba con fuerza
#mira cómo se mueve aquella banderola-dijo un monje
# #lo que se mueve es el viento -respondió otromonje
# #ni las banderolas ni el viento, lo que se mueve son vuestras mentes – dijo el maestro"

texto = "Un día el viento soplaba con fuerza#mira cómo se mueve aquella banderola-dijo un monje#lo que se mueve es el viento -respondió otromonje#ni las banderolas ni el viento, lo que se mueve son vuestras mentes – dijo el maestro"
lineas = texto.split("#")
for i, linea in enumerate(lineas):
    lineas[i] = linea.capitalize()
    if i == 0:
        lineas[i] = lineas[i] + "..."
    else:
        lineas[i]="_"+lineas[i]+"."

for linea in lineas:
    print(linea)