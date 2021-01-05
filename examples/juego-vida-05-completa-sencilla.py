#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Solución para el Ejercicio 3 "juego de la vida (parte 1)" del Módulo 9 (esqueleto inicial)
# Más sencilla de entender, más parecida a las vistas en clase...

import time


# Función auxiliar usada desde leer_tablero_fich(), para que quede todo más claro...
def convertir_cadena_linea_en_lista(cad):
    """Para una cadena bien formada como "000101010101010101111", devuelve [0, 0, 0, 1, ...]"""
    l = []
    for caracter in cad:
        if caracter in ".0-·":  # Opc.: permitir "0"s y más, por comodidad
            l.append(0)
        elif caracter == "1":
            l.append(1)
        # NOTA: al no hacer nada más, ya ignoramos los \n, espacios, líneas vacías...
    return l


def leer_tablero_fich(nombre_fich):
    """Lee un fichero de texto con un contenido adecuado (...) y lo convierte
    en una matriz que representa el tablero de juego (0's y 1's numéricos)"""
    # Recordar que se debe cumplir que:
    # - Comprobar que todas tengan la misma logitud
    # - Permitir cualquier número de líneas de entrada
    # - Ignorar las líneas completamente vacías
    m = []  # La matriz resultado
    try:
        with open(nombre_fich) as f:
            for line in f:
                # Por claridad, "extraemos" la lógica para cada línea a otra función
                l = convertir_cadena_linea_en_lista(line)
                if len(l) > 0:
                    m.append(l)
    except FileNotFoundError:
        print(f"Error en la lectura del archivo '{nombre_fich}'', no existe o no se puede abrir!")
        m = []  # en  caso de error, mejor esto (por si estaba "a medias")
    return m


# Nota: en esta versión ya no se utiliza (al menos por ahora) esta función
def leer_tablero(tablero_cadena):
    """Convierte una cadena adecuada en una matriz, para operar mejor con ella"""
    i = 0
    l = []  # Una lista para ir generando una fila
    m = []  # La matriz resultado
    columnas = 0
    for celda in tablero_cadena:
        if celda == '\n':
            if columnas == 0:
                columnas = len(l)
            elif columnas != len(l):
                print(f"Error en la fila {i}, faltan o sobran datos!")
                exit(1)
            i = i + 1
            m.append(l)
            l = []
        elif celda != " ":  # ignoramos los espacios para escribirlo más claramente
            # Aceptamos varias cosas como "vacío", y cualquier otra implica "lleno"
            if celda in ".0-·":
                l.append(0)
            else:
                l.append(1)

    return m


def print_tablero(m, vacio="0", lleno="1", sep=""):
    """Escribe por pantalla la matriz m con formato de tablero de 0's y 1's"""
    cad = str(m).replace(",", "").replace(" ", "").replace("[", "").replace("]","\n")
    cad = cad.replace("0", vacio + sep).replace("1", lleno + sep)
    print(cad, end="")


def clear_screen():
    """Limpia la pantalla (en consola). Válido en Linux, Mac y Windows"""
    # NOTA: no sirve en modo interactivo, IPython, Jupyter notebook, etc.
    import os
    os.system('cls' if os.name=='nt' else 'clear')


def num_vecinos(m, x, y):
    """Devuelve el número de vecinos de la celda m[y][x], como un valor de 0 a 8"""
    result = 0
    FILAS = len(m)
    COLUMNAS = len(m[0]) if len(m) else 0
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i != 0 or j != 0:  # no contar la celda en sí!
                if (x + i >= 0) and (x + i < COLUMNAS) and (y + j >= 0) and (y + j < FILAS):
                    result += m[y+j][x+i]

    return result


def sig_generacion(m):
    """Devuelve la matriz resultante de aplicar las reglas del juego a cada celda"""
    FILAS = len(m)
    COLUMNAS = len(m[0]) if len(m) else 0
    new_m = []  # matriz resultado
    for i in range(FILAS):
        l = []  # Una lista para ir generando una fila
        for j in range(COLUMNAS):
            vec = num_vecinos(m, j, i)
            if vec < 2 or vec > 3:
                l.append(0)  # muere
            elif vec == 3:
                l.append(1)  # nace
            else:
                l.append(m[i][j])  # sobrevive si estaba viva
        new_m.append(l)

    return new_m


# Comienzo del programa

# NOTA: posible mejora opcional: recibir un argumento de línea de comandos opcional, con el
# nombre del fichero de tablero que se debe leer (si no se recibe, se usa el de por defecto)

# NOTA: dependiendo de cómo/dónde lo ejecutemos, puede hacer falta ajustar la ruta!
# FICH_TABL = "examples/juego-vida.txt"
FICH_TABL = "examples/juego-vida-spc.txt"

# m = leer_tablero(tablero_texto)
m = leer_tablero_fich(FICH_TABL)
FILAS = len(m)
COLUMNAS = len(m[0]) if len(m) else 0

clear_screen()
print(f"Tablero inicial ({FILAS} filas, {COLUMNAS} columnas):")
print_tablero(m, vacio="-", sep=" ")

if FILAS and COLUMNAS:
    input("Pulsa enter para comenzar")

# Pruebas y comprobaciones
# print(num_vecinos(m, 0, 0))
# print(num_vecinos(m, 1, 0))
# print(num_vecinos(m, 2, 0))
# print(num_vecinos(m, 0, 1))
# print(num_vecinos(m, 1, 1))
# print(num_vecinos(m, 2, 1))

# Ir evolucionando y mostrando el estado del juego
gen = 2
while len(m) > 0:
    clear_screen()
    print(f"Tablero siguiente (generación {gen}):")
    m = sig_generacion(m)
    print_tablero(m, vacio="-", sep=" ")
    time.sleep(0.3)
    gen = gen + 1
