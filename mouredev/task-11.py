 #
 # EJERCICIO:
 # Explora el concepto de manejo de excepciones según tu lenguaje.
 # Fuerza un error en tu código, captura el error, imprime dicho error
 # y evita que el programa se detenga de manera inesperada.
 # Prueba a dividir "10/0" o acceder a un índice no existente
 # de un listado para intentar provocar un error.
 #
 # DIFICULTAD EXTRA (opcional):
 # Crea una función que sea capaz de procesar parámetros, pero que también
 #  pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
 # corresponderse con un tipo de excepción creada por nosotros de manera
 # personalizada, y debe ser lanzada de manera manual) en caso de error.
 # - Captura todas las excepciones desde el lugar donde llamas a la función.
 # - Imprime el tipo de error.
 # - Imprime si no se ha producido ningún error.
 # - Imprime que la ejecución ha finalizado.
 #/
 



#Examples

lista = [30, 40, 70, 60, 33]

try:
  lista[6]
except IndexError as e:
   print(f'no existe indice: error {e}')
   


class ErrorDeValidacion(Exception):
  def __init__(self, campo,  mensaje):
    self.campo = campo 
    self.mensaje = mensaje
    super().__init__(f"Error en '{campo}': {mensaje}")

def procesar():
    lista = []

    while True:
        inputUser = input('dame un numero o "salir": ')

        if inputUser == 'salir':
            break

        try:
            numero = int(inputUser)  # puede fallar (ValueError)
            
            if numero < 0:
              raise ErrorDeValidacion("numero", "No se permiten negativos")
            
            lista.append(numero)

            # Forzar error a propósito
            print(lista[10])  #  IndexError

        except ValueError:
            print("Eso no es un número")

        except IndexError:
            print("Te fuiste de rango")

        finally:
            print("Iteración terminada")
      
  
  


 
 