lista_1 = ["h","o","l","a","","m","u","n","d","o"]
lista_2 = ["h","o","l","a","","l","u","n","a"]

lista_3 = []

for letra in lista_1 and lista_2:
    if letra in lista_2 and letra not in lista_3:
        lista_3.append(letra)

print(lista_3)