# ============================================================
# PRÁCTICAS DE LISTAS - LÓGICA DE PROGRAMACIÓN
# ============================================================
# Este archivo agrupa todos los ejercicios sobre listas:
# recorridos, filtros, sumas acumuladas, enumerate y más.


# ─── EJERCICIO 1: Suma de números pares ──────────────────────
# Recorremos la lista y sumamos solo los números pares.
# % es el operador módulo: devuelve el RESTO de la división.
# Si valor % 2 == 0 → es divisible por 2 → es par.

numeros = [2, 4, 8, 10, 334, 30, 25, 32, 24, 88, 84, 85]
suma = 0

for valor in numeros:
    if valor % 2 == 0:
        suma += valor   # suma += valor es lo mismo que suma = suma + valor

print("Suma de pares:", suma)


# ─── EJERCICIO 2: Nombres - reverse, filtro, set, swap ───────
# Varias operaciones sobre una lista de nombres:
# invertir, filtrar por longitud, eliminar duplicados y swap.

listaNombres = ['juan', 'jose', 'pedrito', 'transana', 'luana', 'juan', 'luana']

# .reverse() invierte la lista EN EL LUGAR (modifica la original, no devuelve nada)
listaNombres.reverse()
print("Lista invertida:", listaNombres)

# Filtrar nombres con 5 o más letras usando len()
contador = 0
listasNombre5omas = []

for valor in listaNombres:
    if len(valor) >= 5:   # len() devuelve la cantidad de caracteres de un string
        contador += 1
        listasNombre5omas.append(valor)

print("Cantidad de nombres con 5+ letras:", contador)
print("Nombres con 5+ letras:", listasNombre5omas)

# Eliminar duplicados con set():
# set() convierte la lista en un conjunto → los duplicados desaparecen automáticamente.
# Luego lo convertimos de vuelta a list().
setSinRepetidos = set(listaNombres)
listSinRepeticiones = list(setSinRepetidos)
print("Lista sin repeticiones:", listSinRepeticiones)

# Swap: intercambiar primer y último elemento usando asignación simultánea.
# Python evalúa el lado derecho PRIMERO, luego asigna, así no necesitamos variable temporal.
listSinRepeticiones[0], listSinRepeticiones[-1] = listSinRepeticiones[-1], listSinRepeticiones[0]
print("Lista tras swap primero/último:", listSinRepeticiones)


# ─── EJERCICIO 3: Máximo divisible por 3 ─────────────────────
# Filtramos los divisibles por 3 y encontramos el mayor con max().

numerosMaximos = [3, 9, 12, 312, 324, 555, 534, 524, 1024]
numerosMaximosDivisible3 = []

for valor in numerosMaximos:
    if valor % 3 == 0:
        numerosMaximosDivisible3.append(valor)

maximo = max(numerosMaximosDivisible3)   # max() devuelve el valor más alto de la lista
print("Máximo divisible por 3:", maximo)


# ─── EJERCICIO 4: Suma acumulada (running sum) ───────────────
# Creamos una nueva lista donde cada elemento es la suma de todos
# los anteriores MÁS el actual.
# Ejemplo: [3, 9, 12] → [3, 12, 24]
#
# No usamos max() porque ese devuelve un único valor.
# Acá acumulamos progresivamente con cada iteración.

numerosRandom = [3, 9, 12, 312, 324, 555, 534, 524, 1024, 333, 3493843, 343]
numerosSumadosTotal = []
suma_total = 0

for valor in numerosRandom:
    suma_total += valor                    # sumamos el valor al acumulador
    numerosSumadosTotal.append(suma_total) # guardamos el estado actual del acumulador

print("Suma acumulada:", numerosSumadosTotal)


# ─── EJERCICIO 5: Separar positivos y negativos ──────────────
# Recorremos y enviamos cada número a su lista correspondiente.
# El 0 no entra en ninguna (no es positivo ni negativo).

numerosRandom = [3, 9, 12, 312, 324, 555, 534, 524, 1024, 333, 3493843, 343, -23, -55, -60, -40]
listaNegativosFiltrados = []
listaPositivosFiltrados = []

for valor in numerosRandom:
    if valor < 0:
        listaNegativosFiltrados.append(valor)
    elif valor > 0:
        listaPositivosFiltrados.append(valor)

print("Negativos:", listaNegativosFiltrados)
print("Positivos:", listaPositivosFiltrados)


# ─── EJERCICIO 6: Repetir palabras según su longitud ─────────
# Cada palabra se repite tantas veces como letras tiene.
# Ejemplo: 'juan' (4 letras) → ['juan', 'juan', 'juan', 'juan']
#
# [valor] crea una lista de un elemento.
# * len(valor) la repite N veces.
# += concatena esa lista repetida a listaRepetida.

listaNombres = ['juan', 'jose', 'pedrito', 'transana', 'luana']
listaRepetida = []

for valor in listaNombres:
    listaRepetida += [valor] * len(valor)

print("Lista repetida:", listaRepetida)


# ─── EJERCICIO 7: Enumerate - modificar lista según condición ─
# enumerate() nos da el ÍNDICE y el VALOR al mismo tiempo.
# Lo usamos para modificar la lista en el lugar (numbers[i] = ...).
# Si par → multiplicar x3, si impar → restar 5.

numbers = [24, 42, 32, 55]

for i, valor in enumerate(numbers):   # i = índice (0,1,2...), valor = elemento
    if valor % 2 == 0:
        numbers[i] = valor * 3
    else:
        numbers[i] = valor - 5

print("Lista modificada (par*3, impar-5):", numbers)

# Duplicar todos los elementos con enumerate
for i, valor in enumerate(numbers):
    numbers[i] = valor * 2

print("Lista duplicada:", numbers)

# Lo mismo con list comprehension (forma más corta y pythónica)
# [expresión for variable in iterable]
doubled = [x * 2 for x in numbers]
print("Duplicada con comprehension:", doubled)

# Restar 3 a cada elemento
for i, valor in enumerate(numbers):
    numbers[i] = valor - 3

print("Lista tras restar 3:", numbers)


# ─── EJERCICIO 8: Otra lista con enumerate + comprehension ───
# Si divisible por 3 → sumar 10, si no → restar 2.
# Luego elevamos al cuadrado con comprehension.

numbers2 = [3, 8, 15, 40, 70, 12]

for i, valor in enumerate(numbers2):
    if valor % 3 == 0:
        numbers2[i] = valor + 10
    else:
        numbers2[i] = valor - 2

# x**2 = x elevado al cuadrado (potencia)
numbersNew = [x**2 for x in numbers2]
print("Lista al cuadrado:", numbersNew)


# ─── EJERCICIO 9: Pares positivos - contador, suma, índices ──
# Tenemos negativos, positivos y ceros mezclados.
# Solo nos interesan los pares positivos.

numerosRandom = [3, -2, 8, 15, -7, 22, 0, 10, -5]
contador = 0
suma = 0

for valor in numerosRandom:
    if valor > 0:           # primero filtramos positivos
        if valor % 2 == 0:  # de esos, solo los pares
            contador += 1
            suma += valor

print("Cantidad pares positivos:", contador)
print("Suma pares positivos:", suma)

# Lo mismo pero también guardando los índices donde aparecen con enumerate
numerosPares = [3, 8, 15, 22, 7, 10]
contador = 0
suma = 0
indices_pares_positivos = []

for i, valor in enumerate(numerosPares):
    if valor > 0 and valor % 2 == 0:   # condición combinada con 'and'
        contador += 1
        suma += valor
        indices_pares_positivos.append(i)   # guardamos la posición en la lista

print("Cantidad pares positivos:", contador)
print("Suma pares positivos:", suma)
print("Índices de pares positivos:", indices_pares_positivos)


# ─── EJERCICIO 10: Múltiplos negativos de 3 → promedio ───────
# Buscamos números que sean múltiplos de 3 Y negativos.
# Guardamos de una posible división por cero con una condición.

numerosxD = [3, -6, 8, -9, 15, -12, 0, 10, -5]
contador = 0
suma = 0

for valor in numerosxD:
    if valor % 3 == 0 and valor < 0:   # múltiplo de 3 Y negativo
        contador += 1
        suma += valor

if contador > 0:   # siempre verificar antes de dividir para evitar ZeroDivisionError
    promedio = suma / contador
    print("Promedio de múltiplos negativos de 3:", promedio)
else:
    print("No hay múltiplos negativos de 3.")


# ─── EJERCICIO 11: Separar por condición + promedios ─────────
# De una lista mixta:
#   positivos pares → list1
#   negativos múltiplos de 5 → list2
#
# Tres versiones progresivas del mismo ejercicio:

# Versión 1: con contadores y sumas manuales
numerosRevueltos = [10, -5, 3, 8, -15, 0, -20, 7, 12]
list1 = []
list2 = []
contadorPositivo = 0
contadorNegativo = 0
sumaPositivo = 0
sumaNegativo = 0

for valor in numerosRevueltos:
    if valor > 0:
        if valor % 2 == 0:
            list1.append(valor)
            contadorPositivo += 1
            sumaPositivo += valor
    elif valor < 0:
        if valor % 5 == 0:
            list2.append(valor)
            contadorNegativo += 1
            sumaNegativo += valor

promedioPositivo = sumaPositivo / contadorPositivo
promedioNegativo = sumaNegativo / contadorNegativo

print("Promedio positivos pares (v1):", promedioPositivo)
print("Promedio negativos múlt.5 (v1):", promedioNegativo)

# Versión 2: más limpia usando sum() y len() sobre las listas resultantes
numerosRevueltos = [10, -5, 3, 8, -15, 0, -20, 7, 12]
list1 = []
list2 = []

for valor in numerosRevueltos:
    if valor > 0:
        if valor % 2 == 0:
            list1.append(valor)
    elif valor < 0:
        if valor % 5 == 0:
            list2.append(valor)

promedioPositivo = sum(list1) / len(list1)   # sum() suma todo, len() cuenta cuántos hay
promedioNegativo = sum(list2) / len(list2)

print("Promedio positivos pares (v2):", promedioPositivo)
print("Promedio negativos múlt.5 (v2):", promedioNegativo)

# Versión 3: con índices y f-string para mostrar todo junto
numerosRevueltos = [10, -5, 3, 8, -15, 0, -20, 7, 12]
list1 = []
list2 = []
indices1 = []
indices2 = []

for i, valor in enumerate(numerosRevueltos):
    if valor > 0:
        if valor % 2 == 0:
            list1.append(valor)
            indices1.append(i)
    elif valor < 0:
        if valor % 5 == 0:
            list2.append(valor)
            indices2.append(i)

positivoPromedio = sum(list1) / len(list1)
negativoPromedio = sum(list2) / len(list2)

# f-string: permite insertar variables dentro del texto usando {}
print(f'Positivos encontrados: {list1}, negativos: {list2}')
print(f'Índices positivos: {indices1}, índices negativos: {indices2}')
print(f'Promedio positivo: {positivoPromedio}, promedio negativo: {negativoPromedio}')


# ─── EJERCICIO 12: Condicionales múltiples sobre lista ───────
# Positivos condicionales: valor > 5 Y par
# Negativos condicionales: valor < 0 Y impar Y múltiplo de 5

positivosCondicionales = []
negativosCondicionales = []
indicesPositivosCondicionales = []
indicesNegativosCondicionales = []

lgbtDiversidad = [4, -10, 15, -3, 20, -25, 8, -30, 7, 2]

for i, valor in enumerate(lgbtDiversidad):
    if valor > 5 and valor % 2 == 0:                       # mayor a 5 Y par
        positivosCondicionales.append(valor)
        indicesPositivosCondicionales.append(i)
    elif valor < 0 and valor % 2 != 0 and valor % 5 == 0:  # negativo, impar Y múlt. de 5
        negativosCondicionales.append(valor)
        indicesNegativosCondicionales.append(i)

promedioPositivosCondicionales = sum(positivosCondicionales) / len(positivosCondicionales)
promedioNegativosCondicionales = sum(negativosCondicionales) / len(negativosCondicionales)

print(f'Positivos condicionales: {positivosCondicionales}')
print(f'Negativos condicionales: {negativosCondicionales}')
print(f'Índices positivos: {indicesPositivosCondicionales}')
print(f'Índices negativos: {indicesNegativosCondicionales}')

maximosPositivosCondicionales = max(positivosCondicionales)
minimosNegativosCondicionales = min(negativosCondicionales)   # FIX: era max(), ahora min() porque la variable se llama "minimos"

print(f'Máximo positivo: {maximosPositivosCondicionales}')
print(f'Mínimo negativo: {minimosNegativosCondicionales}')


# ─── EJERCICIO 13: Contador de elementos mayores al promedio ──
# Por cada elemento, comparamos si supera el promedio de los anteriores.
# Empezamos el loop desde el índice 1 (el segundo elemento).

listaNumeros = [100, 200, 150, 300]
suma = listaNumeros[0]   # iniciamos la suma con el primer elemento
contador = 0

for i in range(1, len(listaNumeros)):  # range(1, len) arranca desde el índice 1
    promedio = suma / i                 # promedio de los elementos que vimos hasta ahora

    if listaNumeros[i] > promedio:     # ¿el actual supera el promedio previo?
        contador += 1

    suma += listaNumeros[i]            # agregamos el actual a la suma para la próxima vuelta

print("Elementos que superan el promedio previo:", contador)
