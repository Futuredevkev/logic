 #
 # EJERCICIO:
 # Utilizando tu lenguaje crea un conjunto de datos y realiza las siguientes
 # operaciones (debes utilizar una estructura que las soporte):
 # - Añade un elemento al final.
 # - Añade un elemento al principio.
 # - Añade varios elementos en bloque al final.
 # - Añade varios elementos en bloque en una posición concreta.
 # - Elimina un elemento en una posición concreta.
 # - Actualiza el valor de un elemento en una posición concreta.
 # - Comprueba si un elemento está en un conjunto.
 # - Elimina todo el contenido del conjunto.
 #
 # DIFICULTAD EXTRA (opcional):
 # Muestra ejemplos de las siguientes operaciones con conjuntos:
 # - Unión.
 # - Intersección.
 # - Diferencia.
 # - Diferencia simétrica.
 #/
 
 
## EXTRA

# Une uno con el otro excluyendo los repetidos
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

zUnion = x.union(y)
print(zUnion)

# Devuelve los repetidos
zInterseccion = x.intersection(y)
print(zInterseccion)


# Lo que esta en x pero no en y
xNoRepeatY = x.difference(y)
# Lo que esta en y pero no en x
yNoRepeatX = y.difference(x)
# Todo lo que no se repite de los dos
allNoRepeat = x.symmetric_difference(y)

print(xNoRepeatY)
print(yNoRepeatX)
print(allNoRepeat)
 

### S1MPLE EXCERCISE 
 
# aniadir un elemento al final de una lista
 
nombres = ["Ana", "Luis", "Carlos", "María", "Sofía"]

nombres.append("Joselito")

print(nombres)


#aniadir un elemento en una posicion concreta

nombres.insert(0, "Juanita")

print(nombres)

#aniadir varios elementos al final de una lista

nombres.extend(["panchito", "culiadito"])

print(nombres)

###### aniadir varios elementos en posiciones concretas

# con un for poco eficiente insertar elementos en sus posiciones concretas

nuevos = ['b', 'c']
posicion = 2

for elemento in reversed(nuevos):
  nombres.insert(posicion, elemento)
  
print(nombres)

#Slicing la mejor forma, aniadir elementos en la posicion 2:2
nombres[posicion:posicion] = nuevos

print(nombres)


# Eliminar un elemento en una posicion concreta
nombres.pop(2)
print(nombres)

# Cambiar un valor concreto en un indice concreto
nombres[2] = "Caca"
print(nombres)

# Buscar un elemento en la lista y ver el indice
IndexPositionIsTrue = nombres.index("Caca")
print(IndexPositionIsTrue)

#Eliminar todos los elementos de la lista.
nombres.clear()
print(nombres)


