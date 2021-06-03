import numpy as np
import csv
f = open("Palabras.txt", "w")
k = open("texto.txt", "r")
archivos = 10
datos = k.read().lower().split("\n")
texto = [[]]
val = 0
for i in range(0, len(datos)):
    for j in range(len(datos[i].split(" "))):
        if datos[i].split(" ")[j] == "asdf":
            texto.append([])
            val += 1
        else:
            texto[val].append(datos[i].split(" ")[j])
noWord = [",", ".", ";", ":"]
value = []
f.write(",\n")
f.write(".\n")
for j in range(0, len(texto)):
    for i in range(0, len(texto[j])):
        print(texto[j][i])
        if texto[j][i][-1] == "," or texto[j][i][-1] == "." or texto[j][i][-1] == ":" or texto[j][i][-1] == ";":
            texto[j][i] = texto[j][i][:-1]
        if texto[j][i].lower() not in noWord:
            noWord.append(texto[j][i].lower())
            f.write(str(texto[j][i].lower()) + "\n")


diccionario = {}
for r in range(0, len(noWord)):
    value.append([])
    for i in range(0, len(texto)):
        puntos = 0
        N = len(texto[i])
        value[r].append([])
        for j in range(0, len(texto[i])):
            if noWord[r] == texto[i][j]:
                puntos += 1
        value[r][i] = puntos/N
maximo = 0
for i in range(0, len(value)):
    if max(value[i]) > maximo:
        print(max(value[i]))
        maximo = max(value[i])

for i in range(len(value)):
    resp = []
    resp.append(noWord[i])
    for j in range(0, len(value[i])):
        resp.append(value[i][j] / maximo)

    with open("Diccionario de palabras.csv", "a") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(resp)
