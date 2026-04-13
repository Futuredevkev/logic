 #
 # EJERCICIO:
 # Explora el concepto de callback en tu lenguaje creando un ejemplo
 # simple (a tu elección) que muestre su funcionamiento.
 #
 # DIFICULTAD EXTRA (opcional):
 # Crea un simulador de pedidos de un restaurante utilizando callbacks.
 # Estará formado por una función que procesa pedidos.
 # Debe aceptar el nombre del plato, una callback de confirmación, una
 #3 de listo y otra de entrega.
 ##- Debe imprimir un confirmación cuando empiece el procesamiento.
 # - Debe simular un tiempo aleatorio entre 1 a 10 segundos entre
 #   procesos.
 # - Debe invocar a cada callback siguiendo un orden de procesado.
 # - Debe notificar que el plato está listo o ha sido entregado.
 #/
 
import random
import time
 
def mostrar_resultados(resultado):
  print(f'Resultado: {resultado}')
  

def suma(a, b, callback):
  resultado = a + b 
  callback(resultado)
  

suma(5, 3, mostrar_resultados)
  
  
## EXTRA 

def confirmationFood(plato):
  print(f'{plato} esta confirmado, sale a cocina!')

def finishedFood(plato):
  print(f'{plato} esta terminado!! pasa a delivery') 

def deliveredFood(plato):
  print(f'{plato} esta en la calle, pronto sera entregado') 
  
def randomTime():
  return random.randint(1, 20)

def procesar_pedido(callback_confirmation, callback_finishedFood, callback_delivered):
  platos = ['arroz', 'pancho', 'hamburguesa con papas', 'ensalada']
  
  for i, p in enumerate(platos, start=1):
    print(f'{i}. {p}')
    
  usuario = input(f'que plato queres pedir hermano?, decime el indice del plato que queres.')
  
  if not usuario.isdigit():
    print('Tenes que ingresar un numero')
    return 
  
  usuario = int(usuario)
  
  if usuario < 1 or usuario > len(platos):
    print('ese numero no esta en el menu')
    return 
  
  
  plato_elegido = platos[usuario - 1]
  
  print(f'\nElegiste: {plato_elegido}')
  
  callback_confirmation(plato_elegido)
  time.sleep(randomTime())
  callback_finishedFood(plato_elegido)
  time.sleep(randomTime())
  callback_delivered(plato_elegido)
  
  
  
  
procesar_pedido(confirmationFood, finishedFood, deliveredFood)