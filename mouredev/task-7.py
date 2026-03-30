 #
 # EJERCICIO:
 # Entiende el concepto de recursividad creando una función recursiva que imprima
 # números del 100 al 0.
 #
 # DIFICULTAD EXTRA (opcional):
 # Utiliza el concepto de recursividad para:
 # - Calcular el factorial de un número concreto (la función recibe ese número).
 # - Calcular el valor de un elemento concreto (según su posición) en la 
 #   sucesión de Fibonacci (la función recibe la posición).
 #
 
 
def a100(n):
  if n > 100:
    return
  
  print(n)
  
  a100(n + 1)
  
a100(0)

def menos100(n):
  if n >= 0:
    return 
  
  print(n)
  
  menos100(n - 100)
  
menos100(100)

def factorial(number):
  if number < 0:
    return 0
  elif number == 0:
    return 1

  return number * factorial(number - 1)

print(factorial(5))  
  
  
def fibonacci(position):
  if position <= 0:
    print('La posicion tiene q ser mayor a 0')
    return 0
  elif position == 1:
    return 0
  elif position == 2:
    return 1
  else:
    return fibonacci(position - 1) + fibonacci(position - 2)
    
  
print(fibonacci(10))