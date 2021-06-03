import csv
import tensorflow as tf
import os
import numpy as np
from sklearn.model_selection import train_test_split


def train_Neural():
    # Train with the data given by the previous games.
    name = "Training_Data.csv"
    with open(name) as csvfile:
        reader = csv.reader(csvfile)
        next(reader)

        data = []
        for row in reader:
            data.append({
                "evidence": [float(cell) for cell in row[:151]],
                "label": [float(cell) for cell in row[151:]]
            })

    # Separate data into training and testing groups
    evidence = [row["evidence"] for row in data]
    labels = [row["label"] for row in data]
    X_training, X_testing, y_training, y_testing = train_test_split(
        evidence, labels, test_size=0.01
    )
    try:
        model = tf.keras.models.load_model('SpeakingAI')
    except:
        # Create a neural network
        model = tf.keras.models.Sequential()

        # Add two hidden layers with 4 units, with ReLU activation
        model.add(tf.keras.layers.Dense(150, input_shape=(151,), activation="relu"))

        # Add output layer with 1 unit, with sigmoid activation
        model.add(tf.keras.layers.Dense(151, activation="sigmoid"))

        # Train neural network
        model.compile(
            optimizer="adam",
            loss="binary_crossentropy",
            metrics=["accuracy"]
        )

    # How many times it has to go throw the data.
    model.fit(X_training, y_training, epochs=750)

    # Evaluate how well model performs
    model.evaluate(X_testing, y_testing, verbose=0)

    model.save('SpeakingAI')

def generador():
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

    texto = input("ingresar lo le dijeron: ").split(" ")
    pregunta1 = input("fue una pregunta? s/n ")
    respuesta = input("ingresar la respuesta: ").split(" ")
    pregunta2 = input("Fue una pregunta? s/n ")
    escribir = []
    maxpalabras = 15
    for i in range(len(texto), maxpalabras):
        texto.append("#")
    for i in range(len(respuesta), maxpalabras):
        respuesta.append("#")
    texto = texto[:maxpalabras]
    respuesta = respuesta[:maxpalabras]
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
    for palabra in respuesta:
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
    escribir.append(1 if pregunta2.lower() == "s" else 0)

    with open("Training_Data.csv", "a") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(escribir)
train_Neural()