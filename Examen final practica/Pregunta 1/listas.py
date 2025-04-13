""" 1. Utilizar el concepto de módulo necesariamente. Escribir un programa para
el manejo de listas el cuál cumplirá los siguientes requerimientos (4 ptos):
Reglas: - Crear una función que le permitirá almacenar 10 números
 aleatorios en unalista y finalmente los imprimirá por consola
 al llamar la función.
- Crear una función que le permita almacenar los números no repetidos de la
lista anterior, retornar este valor e imprimirlo por consola.
- Crear una función donde se creará una lista para ordenar de mayor a menor
la lista que se creó en el ítem anterior (número no repetidos) y otra lista
para ordenarlas de menor a mayor, retornar este valor e imprimirlos por
consola.  - Crear una función para indicar cuál es mayor número par de la lista
(lista del ítem 2), retornar este valor e imprimirlo por consola.
- Crear el archivo principal.py, donde solo llamarás las anteriores funciones
que se encontrarán alojadas en un módulo"""

import random


def generar_lista_aleatoria():
    lista = []
    for _ in range(10):
        numero = random.randint(1, 10)
        lista.append(numero)
    print("Lista aleatoria: {}".format(lista))
    return lista


def obtener_no_repetidos(lista):
    lista_sin_repetidos = list(set(lista))
    print("Lista sin repetidos: {}".format(lista_sin_repetidos))
    return lista_sin_repetidos


def ordenar_listas(lista):
    mayor_a_menor = sorted(lista, reverse=True)
    menor_a_mayor = sorted(lista)
    print("Orden mayor a menor: {}".format(mayor_a_menor))
    print("Orden menor a mayor: {}".format(menor_a_mayor))
    return mayor_a_menor, menor_a_mayor


def obtener_mayor_par(lista):
    pares = [n for n in lista if n % 2 == 0]
    if pares:
        mayor_par = max(pares)
        print("El mayor número par es: {}".format(mayor_par))
        return mayor_par
    else:
        print("No hay números pares en la lista.")
        return None
