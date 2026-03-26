 # 
 # EJERCICIO:
 # Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 # en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 # - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición,
 #   recorrido, conversión a mayúsculas y minúsculas, reemplazo, división, unión,
 #   interpolación, verificación...
 #
 # DIFICULTAD EXTRA (opcional):
 # Crea un programa que analice dos palabras diferentes y realice comprobaciones
 # para descubrir si son:
 # - Palíndromos
 # - Anagramas
 # - Isogramas
 #
 
def main():
  palabra1 = input('dame la primera palabra').lower()
  palabra2 = input('dame la segunda palabra').lower()
  
  if es_palindromo(palabra1):
      print(f"{palabra1} es un palíndromo")
  else:
      print(f"{palabra1} NO es un palíndromo")

  if es_palindromo(palabra2):
      print(f"{palabra2} es un palíndromo")
  else:
      print(f"{palabra2} NO es un palíndromo")

  if es_anagrama(palabra1, palabra2):
      print(f"{palabra1} y {palabra2} son anagramas")
  else:
      print(f"{palabra1} y {palabra2} NO son anagramas")

  if es_isograma(palabra1):
      print(f"{palabra1} es un isograma")
  else:
      print(f"{palabra1} NO es un isograma")

  if es_isograma(palabra2):
      print(f"{palabra2} es un isograma")
  else:
      print(f"{palabra2} NO es un isograma")



#Polindromo la palabra alrevez tiene q ser igual 
def es_palindromo(palabra):
    return palabra == palabra[::-1] # Cuando escribes [::-1]: inicio = nada → empieza desde el inicio fin = nada → termina al final paso = -1 → recorre hacia atrás, es decir, invierte la cadena

# Anagrama (La palabra tiene exactamente las mismas letras pero en distinto orden, ejemplo listen:silent)  
def es_anagrama(p1, p2):
    return sorted(p1) == sorted(p2)

# Isograma en las dos palabras no se tiene q repetir ninguna letra, todas las letras aparecen una sola vez. por eso usamos len y set, set se encarga que no haya repetidos y len todas las letras unicas
def es_isograma(palabra):
    return len(set(palabra)) == len(palabra)
  
if __name__ == "__main__":
  main()
  
 
 
# Cadena de ejemplo
texto = "Hola Mundo"

# 1️⃣ Acceso a caracteres específicos
print(texto[0])   # 'H' -> primer carácter
print(texto[-1])  # 'o' -> último carácter

# 2️⃣ Subcadenas (slicing)
print(texto[0:4])   # 'Hola' -> del índice 0 al 3
print(texto[5:])    # 'Mundo' -> desde el índice 5 hasta el final
print(texto[:4])    # 'Hola' -> desde el inicio hasta el índice 3

# 3️⃣ Longitud de la cadena
print(len(texto))   # 10

# 4️⃣ Concatenación
texto2 = texto + "!!!"
print(texto2)       # 'Hola Mundo!!!'

# 5️⃣ Repetición
print(texto * 3)    # 'Hola MundoHola MundoHola Mundo'

# 6️⃣ Recorrido (loop)
for char in texto:
    print(char, end=' ')
print()

# 7️⃣ Conversión a mayúsculas y minúsculas
print(texto.upper())  # 'HOLA MUNDO'
print(texto.lower())  # 'hola mundo'
print(texto.title())  # 'Hola Mundo' -> mayúscula inicial en cada palabra

# 8️⃣ Reemplazo
print(texto.replace("Mundo", "Python"))  # 'Hola Python'

# 9️⃣ División (split)
palabras = texto.split()  # divide por espacios
print(palabras)           # ['Hola', 'Mundo']

#  🔟 Unión (join)
print("-".join(palabras))  # 'Hola-Mundo'

# 1️⃣1️⃣ Interpolación / Formateo
nombre = "Kevin"
saludo = f"Hola {nombre}, bienvenido!"  # f-string
print(saludo)
print("Hola {}, bienvenido!".format(nombre))
print("Hola %s, bienvenido!" % nombre)

# 1️⃣2️⃣ Verificación / Checks
print(texto.startswith("Hola"))  # True
print(texto.endswith("Mundo"))   # True
print("Mundo" in texto)          # True
print("Python" not in texto)     # True
print(texto.isalpha())           # False (porque hay espacio)
print("Hola".isalpha())          # True
print("123".isdigit())           # True

# 1️⃣3️⃣ Eliminación de espacios (strip)
texto_con_espacios = "   Hola Mundo   "
print(texto_con_espacios.strip())   # 'Hola Mundo'
print(texto_con_espacios.lstrip())  # 'Hola Mundo   '
print(texto_con_espacios.rstrip())  # '   Hola Mundo'

# 1️⃣4️⃣ Buscar posición
print(texto.find("Mundo"))   # 5
print(texto.index("Mundo"))  # 5 -> similar a find pero da error si no existe

# 1️⃣5️⃣ Contar ocurrencias
print(texto.count("o"))  # 2

# 1️⃣6️⃣ Invertir cadena
print(texto[::-1])  # 'odnuM aloH'

