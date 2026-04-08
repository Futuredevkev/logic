 #
 # EJERCICIO:
 # Utilizando tu lenguaje, emplea 3 mecanismos diferentes para imprimir
 # números del 1 al 10 mediante iteración.
 #
 # DIFICULTAD EXTRA (opcional):
 # Escribe el mayor número de mecanismos que posea tu lenguaje
 # para iterar valores. ¿Eres capaz de utilizar 5? ¿Y 10?
 #/
 
# For 

for i in range(0, 11):
  print(i)

# While
  
i = 1
while i <= 10:
  print(i)
  i += 1
  

# List Comprenshion

[print(i) for i in range(1, 11)]  

# Map

list(map(print, range(1, 11)))

# For enumerate

for i, _ in enumerate(range(1, 11), start=1):
    print(i)

# Recursividad

def oneTen(n):
  if n > 10:
    return
  
  print(n)
  
  oneTen(n + 1)

oneTen(0)