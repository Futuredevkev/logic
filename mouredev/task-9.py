 #
 # EJERCICIO:
 # Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
 # atributos y una función que los imprima (teniendo en cuenta las posibilidades
 # de tu lenguaje).
 # Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
 # utilizando su función.
 #
 # DIFICULTAD EXTRA (opcional):
 # Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
 # en el ejercicio número 7 de la ruta de estudio)
 # - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
 #   retornar el número de elementos e imprimir todo su contenido.
 #/
 

class Pila:
  def __init__(self): 
    self.elements = []
    
  def push(self, number):
    
    self.elements.append(number)
  
  def pop(self):
    if len(self.elements) > 0:
      self.elements.pop()
    
  def printElements(self):
    elementsNumber = len(self.elements)
    return f'numeros de elementos {elementsNumber}, contenido {self.elements}'
  
  
class Person:
  def __init__(self, name: str, surname: str, age: int, height: float):
    self.full_name = f"{name} {surname}"
    self.age = age 
    self.height = height
     
  def dates(self):
    print(f'{self.full_name} con la edad de {self.age} y la altura de {self.height}')
    
my_person_date = Person("Kevin", "Moreira", 23, 1.60)
my_person_date.age = 24
    
    
