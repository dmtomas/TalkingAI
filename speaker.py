import numpy as np
import csv
import tensorflow as tf

def encontrar(lista, a):
    mindif = np.inf
    ans = 0
    for i in range(0, len(a)):
        dif = 0
        for j in range(1, len(a[i])):
            dif += (lista[j-1] - a[i][j]) ** 2
        if dif < mindif:
            mindif = dif
            ans = i
        if mindif == 0:
            return a[ans][0]
    return a[ans][0]


a = []
rows = 10
with open('Diccionario de palabras.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    j = 0
    for row in plots:
        a.append([row[0]])
        for i in range(1, len(row)):
            a[j].append(float(row[i]))
        j += 1
model = tf.keras.models.load_model('SpeakingAI')
texto = input("ingresar lo que le dijeron: ").split(" ")
pregunta1 = input("fue una pregunta? s/n ")
escribir = []
maxpalabras = 15
for i in range(len(texto), maxpalabras):
    texto.append("#")
texto = texto[:maxpalabras]
for palabra in texto:
    conocida = "no"
    for i in range(0, len(a)):
        if palabra.lower() == a[i][0]:
            conocida = "yes"
            for j in range(1, len(a[i])):
                escribir.append(float(a[i][j]))
            break
    if conocida == "no":
        for i in range(1, len(a[0])):
            escribir.append(a[0][i])
escribir.append(1 if pregunta1.lower() == "s" else 0)
respuesta = model.predict(np.array(escribir).reshape((1, 151)))

promedio = []
print("La computadora ", end="")
print("pregunta: " if respuesta[0][-1] > 0.5 else "responde: ")
traducido = []
ans = ""
for i in range(0, 15):
    traducido.append([])
    for j in range(0, 10):
        traducido[i].append(respuesta[0][i*10+j])

for i in range(0, len(traducido)):
    ans += encontrar(traducido[i], a) + " "
print(ans)

