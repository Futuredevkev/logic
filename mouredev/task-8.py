#
# EJERCICIO:
# Implementa los mecanismos de introducción y recuperación de elementos propios de las
# pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
# o lista (dependiendo de las posibilidades de tu lenguaje).
#
# DIFICULTAD EXTRA (opcional):
# - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
#   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
#   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
#   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
#   el nombre de una nueva web.
# - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
#  impresora compartida que recibe documentos y los imprime cuando así se le indica.
#   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
#   interpretan como nombres de documentos.
#/

# Pila

stack = []

# Push - Pila
stack.append(1)
stack.append(2)
stack.append(3)

#Pop

stackItem = stack[len(stack) - 1]
del stack[len(stack) - 1]
print(stackItem)

print(stack.pop())

print(stack)


# Cola

queue = []

queue.append(1)
queue.append(2)
queue.append(3)

stackItem = stack[0]
del queue[0]



def webNavigation():
  
  while True:
    action = input('usa adelante, atras, o aniadi una url para navegar')
    if action == 'salir':
      print('saliendo del navegador')
      break
    elif action == 'adelante':
      pass 
    elif action == 'atras':
      if len(stack) > 0:
        stack.pop() 
    else:
      stack.append(action)
  
    if len(stack > 0):
      print(f'has navegado a la web: {stack[len(stack) - 1]}')
    else: 
      print('estas en la pagina de inicio')
      

def imprimirElementosDeLaCola():
  queue = []
  
  while True:
    
    action = input('aniade un documento o selecciona Imprimir/Salir:')
  
    if action == 'salir':
      break
    elif action == 'imprimir':
      if len(queue) > 0:
        print(f'toma el documento {queue.pop[0]}')
    else:
      queue.append(action)
      
    print(f'cola de impresion: {queue}')
 
imprimirElementosDeLaCola()     