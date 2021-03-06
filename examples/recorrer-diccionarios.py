#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Solución para el Ejercicio / demo "recorrer diccionarios" del Módulo 4 (esqueleto inicial)

dicc1 = {
    "Naranjas": 25,
    "Manzanas": 0,
    "Fresas": 240,
    "Kiwis": 15.33333,
    "Plátanos": 5.5,
}

dicc2 = {
    "Naranjas": None,
    "Manzanas": 55,
    "Fresas": 0.0,
    "Kiwis": "tres bandejas",
    "Plátanos": 5.5,
}

frutas = dicc1


# Primera forma de solucionarlo: recorriendo las claves del diccionario

for fruta in frutas.keys():  # si no indico nada, es como keys()
    # MODIFICAR para que cumpla lo que nos pedían:
    if frutas[fruta] > 0:
        print("La cantidad de:", fruta, "es", frutas[fruta])

print()


# Alternativa: recorrer los elementos o items (tuplas clave-valor)

for fruta, cantidad in frutas.items():
    # MODIFICAR para que cumpla lo que nos pedían:
    if cantidad > 0:
        print("La cantidad de:", fruta, "es", cantidad)

print()


# Alternativa 2, no recomendable para este caso: sacar los elementos con popitem()
# No es recomendable simplemente por eficiencia, tenemos que hacer primero una copia
# porque no sabemos si luego haría falta la lista original de nuevo (probable...)

copia_frutas = frutas.copy()  # hacer una copia
while len(copia_frutas) > 0:
    fruta, cantidad = copia_frutas.popitem()
    # MODIFICAR para que cumpla lo que nos pedían:
    if cantidad > 0:
        print("La cantidad de:", fruta, "es", cantidad)
