  #
 # EJERCICIO:
 # - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 #   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 #   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 # - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 #   que representen todos los tipos de estructuras de control que existan
 #   en tu lenguaje:
 #   Condicionales, iterativas, excepciones...
 # - Debes hacer print por consola del resultado de todos los ejemplos.
 #
 # DIFICULTAD EXTRA (opcional):
 # Crea un programa que imprima por consola todos los números comprendidos
 # entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 #
 # Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 #/
 
 
# Arimetricos
suma = 10 + 3
resta = 10 - 3
division = 10/3
divisionEntera = 10 // 3
multiplicacion = 10 * 3
modulo = 10 % 5 
potencia = 10 ** 10

print(suma)
print(resta)
print(multiplicacion)
print(modulo)
print(potencia)

# Comparacion

comparacion = 10 == 10
diferente = 10 != 5 
mayor = 10 > 5
menor = 10 < 20
mayorIgual = 10 >= 5
menorIgual = 10 <= 20

print(comparacion)
print(diferente)
print(mayor)
print(menor)
print(mayorIgual)
print(menorIgual)

#Logicos 

x = True 
y = False 
print(x and y) # False 
print(x or y) # True 
print(not x) # False 

# Asignacion 

c = 5 
c += 2 # c + 2
c -= 3 # c - 3
c *= 2 # c * 2
c /= 4 # c / 4
c //= 2 # c // 2
c %= 2 # c % 2 
c **= 3 # c ** 3


# De Identidad

lista1 = [1, 2]
lista2 = lista1 
lista3 = [1, 2]

print(lista1 is lista2) # True / Mismo objeto
print(lista1 is lista3) # False / mismo contenido, diferente objeto
print(lista1 is not lista3) # True


# De Pertenencia

print(1 in lista1) # True
print(3 not in lista1) # True

# Bit a bit

x = 5
y = 3

print(x & y) # AND 
print(x | y) # OR 
print(x ^ y)  # XOR → 6 (0b0110)
print(~x)     # NOT → -6
print(x << 1) # shift left → 10
print(x >> 1) # shift right → 2

# Condicionales 

edad = 20
acumulacion = 0

if edad >= 20:
  acumulacion += 2
else:
  print('burrito')
  
print(acumulacion)
  
  
  
# Iterativas 

#While Loop

i = 0

while i <= 3:
  print(i)
  i += 1
  

# For Loop

for i in range(3):
  print(i)
  

# For Lista 
frutas = ["manzana", "banana", "cereza"]

for fruta in frutas:
  print(fruta)
  

# For dic 

frutas = {"verde": "manzana", "verde": "manzana", "verde": "manzana", "verde": "manzana", "verde": "manzana"}

for clave, valor in frutas.items():
  print(clave, valor)
  
# Comprehensions 
cuadrados = [x**2 for x in range(5)]
print(cuadrados)

# Excepciones 
try:
  x = 10/0
except ZeroDivisionError:
  print("No se puede dividir entre cero")
finally:
    print("Esto se ejecuta siempre")
    


NumerosParesMultiplos3 = []
otherNumbers = []
maxRange = 55

for i in range(10, maxRange + 1):
  if i % 2 == 0 or i % 3 == 0: # con el or nos trae los numeros de cualquiera de las dos condiciones, si tuvieramos and tiene q cumplir las dos condiciones para traer x numeros
    NumerosParesMultiplos3.append(i)
  else:
    otherNumbers.append(i)

# Comprenshion same task
    
NumerosParesMultiplos3 = [i for i in range(10, 56) if i % 2 == 0 or i % 3 == 0]
otherNumbers = [i for i in range(10, 56) if not (i % 2 == 0 or i % 3 == 0)]

print(f'numeros pares y multiplos 3 {NumerosParesMultiplos3}')
print(f'Otros numeros {otherNumbers}')