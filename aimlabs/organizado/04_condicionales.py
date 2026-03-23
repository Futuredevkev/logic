# ============================================================
# PRÁCTICAS DE CONDICIONALES - LÓGICA DE PROGRAMACIÓN
# ============================================================
# Ejercicios de if/elif/else y lógica de comparación básica.
# También incluye el uso de input() y max() built-in.


# ─── EJERCICIO 1: Par o impar (con input) ─────────────────────
# input() siempre devuelve un STRING, por eso lo convertimos con int().
# % es el operador módulo: devuelve el resto de la división.
# Si el resto de dividir por 2 es 0 → par, si no → impar.

numero = int(input('Hola usuario, ¿me decís un número? '))

if numero % 2 == 0:
    print("Este número es par.")
else:
    print("Este número es impar.")


# ─── EJERCICIO 2: Máximo de una lista con max() ──────────────
# max() es una función built-in de Python que encuentra el valor más alto.
# También existe min() para el más bajo.

numerosMayor = [30, 40, 60]

mayor = max(numerosMayor)
print("El mayor es:", mayor)


# ─── EJERCICIO 3: Máximo de 3 variables SIN usar max() ───────
# Comparamos manualmente usando if.
# Útil para entender la lógica antes de depender de las funciones built-in.
# Empezamos asumiendo que 'a' es el mayor, y lo vamos corrigiendo.

a = 5
b = 8
c = 3

mayor = a           # asumimos que a es el mayor

if b > mayor:       # ¿b supera al actual mayor?
    mayor = b       # si sí, actualizar

if c > mayor:       # ¿c supera al actual mayor?
    mayor = c

print("El mayor es:", mayor)


# ─── EJERCICIO 4: Contar pares en una lista ──────────────────
# Recorremos la lista e incrementamos un contador cada vez que encontramos un par.

numerosPares = [3, 8, 15, 22, 7, 10]
contador = 0

for valor in numerosPares:
    if valor % 2 == 0:
        contador += 1

print("Cantidad de pares:", contador)
