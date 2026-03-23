# ============================================================
# PRÁCTICAS DE DICCIONARIOS - LÓGICA DE PROGRAMACIÓN
# ============================================================
# Un diccionario es una colección de pares clave: valor.
# Se define con llaves: {'clave': valor}
# Las claves deben ser únicas. Si se repite una clave,
# el último valor sobreescribe al anterior.
#
# Métodos clave:
#   .items()  → devuelve pares (clave, valor) para recorrer
#   .values() → devuelve solo los valores
#   .keys()   → devuelve solo las claves


# ─── EJERCICIO 1: Crear diccionario desde lista (con for) ────
# Recorremos la lista y creamos un par clave:valor por cada palabra.
# La clave es la palabra, el valor es su cantidad de letras.

palabrasLista = ['perro', 'gato', 'leche', 'pan', 'pancho']
diccionario = {}

for palabra in palabrasLista:
    diccionario[palabra] = len(palabra)   # len() cuenta los caracteres

print("Diccionario (for):", diccionario)


# ─── EJERCICIO 2: Lo mismo con comprensión de diccionario ────
# Forma más corta y pythónica.
# Sintaxis: {clave: valor for variable in iterable}

palabrasLista = ['perro', 'gato', 'leche', 'pan', 'pancho']

diccionario = {palabra: len(palabra) for palabra in palabrasLista}

print("Diccionario (comprehension):", diccionario)


# ─── EJERCICIO 3: Invertir clave y valor ─────────────────────
# Queremos que lo que era valor pase a ser clave, y viceversa.
# .items() nos da cada par (clave, valor) para poder desestructurarlos.

diccionario_original = {
    'perro': 5,
    'gato': 4,
    'conejo': 6
}

# Forma con for
diccionario_invertido = {}

for clave, valor in diccionario_original.items():
    # .items() devuelve pares: ('perro', 5), ('gato', 4), etc.
    # Ahora el valor original se convierte en la nueva clave
    diccionario_invertido[valor] = clave

print("Diccionario original:", diccionario_original)
print("Diccionario invertido (for):", diccionario_invertido)

# Forma pythónica con comprensión de diccionario (mismo resultado, una sola línea)
diccionario_invertido2 = {valor: clave for clave, valor in diccionario_original.items()}
print("Diccionario invertido (comprehension):", diccionario_invertido2)


# ─── EJERCICIO 4: Filtrar productos por precio ───────────────
# Calculamos el promedio de precios y filtramos por distintos umbrales.

productos_precios = {
    'manzana': 120,
    'banana': 80,
    'naranja': 100,
    'pera': 150,
    'kiwi': 200
}

# .values() devuelve solo los valores (los precios)
promedio = sum(productos_precios.values()) / len(productos_precios)
print("Promedio de precios:", promedio)

# Filtrar los que cuestan más de 100 (con for)
diccionarioMas100 = {}
for clave, valor in productos_precios.items():
    if valor > 100:
        diccionarioMas100[clave] = valor

print("Productos > 100 (for):", diccionarioMas100)

# Filtrar los que cuestan más de 120 (con comprehension)
# La condición va al final de la comprensión con 'if'
diccionarioMas120 = {
    clave: valor
    for clave, valor in productos_precios.items()
    if valor > 120
}
print("Productos > 120 (comprehension):", diccionarioMas120)


# ─── EJERCICIO 5: Incrementar precios en un diccionario ──────
# Nota: si hay claves repetidas, Python conserva solo el ÚLTIMO valor.
# Acá 'manzana', 'banana', etc. aparecen dos veces → gana el segundo.
# Es un comportamiento a tener en cuenta cuando cargás datos.

productos_precios = {
    'manzana': 120,
    'banana': 80,
    'naranja': 100,
    'pera': 150,
    'kiwi': 200,
    'manzana': 555,    # duplicado → sobreescribe 120
    'banana': 5353,    # duplicado → sobreescribe 80
    'naranja': 53353,  # duplicado → sobreescribe 100
    'pera': 53232,     # duplicado → sobreescribe 150
}

# Forma con for: creamos un nuevo diccionario con cada precio +20
nuevoDicIncrementado = {}
for clave, valor in productos_precios.items():
    precioIncrementado = valor + 20
    nuevoDicIncrementado[clave] = precioIncrementado

print("Precios +20 (for):", nuevoDicIncrementado)

# Forma con comprehension: más concisa, mismo resultado
diccionarioMas20 = {clave: valor + 20 for clave, valor in productos_precios.items()}
print("Precios +20 (comprehension):", diccionarioMas20)

productos_precios = {
    'manzana': 120,
    'banana': 80,
    'naranja': 100,
    'pera': 150,
    'kiwi': 200,
    'manzana': 555,   
    'banana': 5353,    
    'naranja': 53353,  
    'pera': 53232, 
}

puntosTotales = 0
productosSumados = sum(productos_precios.values())
print(productosSumados)

for producto, puntos in productos_precios.items():
    puntosTotales += puntos

print(productosSumados)


jugadores_puntos = {
    "kevin": 1200,
    "ana": 950,
    "luis": 1100,
    "maria": 1300
}


pedirNombre = input('dame tu nombre')
pedirPuntuaje  = input('dame un puntuaje')

pedirPuntuaje = int(pedirPuntuaje)

if pedirNombre in jugadores_puntos:
    jugadores_puntos[pedirNombre] += pedirPuntuaje
else:
    jugadores_puntos[pedirNombre] = pedirPuntuaje

print(jugadores_puntos)

texto = "banana"

frecuencias = {}

for letra in texto:
    if letra in frecuencias:
        frecuencias[letra] += 1
    else:
        frecuencias[letra] = 1

print(frecuencias)
        


texto = "banana"

frecuencias = {}

for letra in texto:
    frecuencias[letra] = frecuencias.get(letra, 0) + 1

print(frecuencias)


listaNombres = []
listaEdades = []

personas_edades = {
    "kevin": 21,
    "ana": 25,
    "luis": 30,
    "maria": 28,
    "sofia": 22,
    "pedro": 35,
    "lucia": 19
}

for nombre, edad in personas_edades.items():
    listaNombres.append(nombre)
    listaEdades.append(edad)

print(listaNombres, listaEdades)


personas_edades = {
    "kevin": 21,
    "ana": 25,
    "luis": 30,
    "maria": 28,
    "sofia": 22
}

# Creamos la lista de tuplas
lista_tuplas = []

for nombre, edad in personas_edades.items():
    lista_tuplas.append((nombre, edad))

# Ordenamos la lista por edad (segunda posición de la tupla)
lista_ordenada = sorted(lista_tuplas, key=lambda x: x[1])

print(lista_ordenada)


clavesEncontradas = []
personas_encontradas = {}

valor_buscando = int(input('ingresa la edad a buscar'))

for nombre, edad in personas_edades.items():
     if edad == valor_buscando:
        clavesEncontradas.append((nombre, edad))
        # Si queremos hacerlo poniendo en un dic seria: personas_encontradas[nombre] = edad



diccionario_random = {
    "manzana": 5,
    "azul": 10,
    "sol": 5,
    "perro": 7,
    "luna": 10,
    "coche": 5,
    "agua": 3,
    "estrella": 7,
    "libro": 3,
    "pizza": 10
}

valoresIgualesInDic = {}


def preguntar():    
    dame_un_numero = int(input('ingresa un numero'))
    return dame_un_numero



def estaValor(numero):
    encontrados = {}

    for clave, valor in diccionario_random.items():
        if valor == numero:
            encontrados[clave] = valor
    return encontrados

print(valoresIgualesInDic)


intentos = 0
while intentos <= 5:
    numero = preguntar 
    resultados = estaValor(numero)

    if resultados:
        print("¡Encontré coincidencias!")
        #valoresIgualesInDic.update(resultados) - forma mas facil
        for clave, valor in resultados.items():
            valoresIgualesInDic[clave] = valor
        print("Resultados acumulados:", valoresIgualesInDic)
        # Si querés que siga preguntando, no ponemos break
    else:
        print("No encontré ese valor.")
        intentos += 1
        print(f"Intentos fallidos: {intentos}/5")

print("Fin del programa. Diccionario final de coincidencias:", valoresIgualesInDic)