# ============================================================
# PRÁCTICAS DE TUPLAS - LÓGICA DE PROGRAMACIÓN
# ============================================================
# Las tuplas son como listas pero INMUTABLES: una vez creadas
# no se pueden modificar directamente.
# Se definen con paréntesis: (1, 2, 3)
# Se usan cuando los datos no deben cambiar (coordenadas, operaciones, etc.)
# max(), min(), sum(), len() funcionan igual con tuplas y listas.


# ─── EJERCICIO 1: Convertir tupla a lista y sumar 10 ─────────
# Como la tupla no se puede modificar, la convertimos a lista,
# operamos sobre ella y guardamos el resultado en otra variable.

my_tuple = (35, 105, 120, 130, 140)

numerosRandomList = list(my_tuple)   # list() convierte la tupla en lista modificable
valores = []

for valor in numerosRandomList:
    valores.append(valor + 10)

print("Tupla original:", my_tuple)
print("Lista con +10:", valores)


# ─── EJERCICIO 2: Máximo, mínimo y promedio de tupla ─────────
# max() y min() funcionan directo sobre la tupla.
# Para el promedio: sum() divide la suma total entre len() (cantidad de elementos).

my_tuple = (35, 105, 120, 130, 140)

maximoTuple = max(my_tuple)                       # el valor más alto
minimoTuple = min(my_tuple)                       # el valor más bajo
tuplePromedio = sum(my_tuple) / len(my_tuple)     # FIX: era max()/len(), ahora sum()/len() para el promedio real

print("Máximo:", maximoTuple)
print("Mínimo:", minimoTuple)
print("Promedio:", tuplePromedio)


# ─── EJERCICIO 3: Verificar si un número está en la tupla ────
# El operador 'in' devuelve True si el elemento existe en la colección.
# Usamos try/except para manejar el caso en que el usuario escriba algo que
# no sea un número (ValueError al intentar int()).

try:
    my_tuple = (35, 105, 120, 130, 140)
    estaTupla = input('Ingresá un número y te digo si está en la tupla: ')
    estaTupla = int(estaTupla)          # convertimos el input (string) a entero
    yesornot = estaTupla in my_tuple    # True si está, False si no
    print("¿Está en la tupla?", yesornot)
except ValueError:
    print('Ingresá un número válido.')


# ─── EJERCICIO 4: Invertir una tupla ─────────────────────────
# Con slicing [::-1] invertimos cualquier secuencia (lista, tupla, string).
# Sintaxis: [inicio:fin:paso] → con paso -1 recorremos al revés.
# Empezar y terminar vacíos significa "desde el principio hasta el final".

my_tuple = (35, 1.77, "brais")
invertida = my_tuple[::-1]

print("Tupla original:", my_tuple)
print("Tupla invertida:", invertida)


# ─── EJERCICIO 5: Filtrar tupla con comprehension ────────────
# No podemos modificar una tupla, pero podemos crear una nueva filtrada.
# Usamos una expresión generadora dentro de tuple() para construirla.
# Sintaxis: tuple(expresión for variable in iterable if condición)

original = (2, 5, 7, 1, 9)

filtrada = tuple(x for x in original if x > 5)   # solo los mayores a 5

print("Tupla original:", original)
print("Tupla filtrada (> 5):", filtrada)
