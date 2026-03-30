 #
 # EJERCICIO:
 # Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
 # implemente una superclase Animal y un par de subclases Perro y Gato,
 # junto con una función que sirva para imprimir el sonido que emite cada Animal.
 #
 # DIFICULTAD EXTRA (opcional):
 # Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
 # pueden ser Gerentes, Gerentes de Proyectos o Programadores.
 # Cada empleado tiene un identificador y un nombre.
 # Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
 # actividad, y almacenan los empleados a su cargo.
 #/


class Employee:
  def __init__(self, name: str, id: int):
    self.name = name 
    self.id = id
    
  def person(self):
    return f"Soy la persona con el nombre {self.name} y tengo la identificacion de {self.id}"


class Manager(Employee):
  def __init__(self, name, id, area):
    super().__init__(name, id)
    self.area = area 
    self.capacityTasks = []
    self.employers = []
    
    def addTaskRoles(self):
      while True:
        input_user = input('Ingresa una task (o "salir" para terminar): ')

        if input_user.lower() == 'salir':
            break

        if input_user.strip() != '' and input_user not in self.capacityTasks:
            self.capacityTasks.append(input_user)
            print("Task agregada")
        else:
            print("Task vacía o duplicada")
        
    def deleteTaskRole(self):
      while True:
        input_user = input('¿Qué task querés eliminar? (pon "salir" si no quieres eliminar mas)')

        if input_user.lower() == 'salir':
          break

        for task in self.capacityTasks:
          if task == input_user:
            self.capacityTasks.remove(task)
            print("Task eliminada correctamente")
            break
        else:
          print("Ese elemento no se encuentra en la lista")
    
    def employerAdd(self):
      while True:
        input_user = input('Ingresa un empleado (o "salir" para terminar): ')

        if input_user.lower() == 'salir':
            break

        if input_user.strip() != '' and input_user not in self.employers:
            self.employers.append(input_user)
            print("Task agregada")
        else:
            print("Task vacía o duplicada")
            
    def deleteEmployer(self):
      while True:
        input_user = input('¿Qué employer querés eliminar? (pon "salir" si no quieres eliminar mas)')

        if input_user.lower() == 'salir':
          break

        for task in self.employers:
          if task == input_user:
            self.employers.remove(task)
            print("Task eliminada correctamente")
            break
        else:
          print("Ese elemento no se encuentra en la lista")




class ProjectManager(Employee):
  def __init__(self, name, id):
    super().__init__(name, id)
    self.projects = []
    self.tasks = []
    
  ## Practicamente lo mismo que la otra clase hija

class Programmer(Employee):
  def __init__(self, name, id, stack_main, level):
    super().__init__(name, id)
    self.stack_main = stack_main
    self.level = level 
    self.bugs = []
    self.tasks = []
    self.techs = []
        
  ## Practicamente lo mismo que la otra clase hija
  
  

############## ExaampleS
class Animal:
    def __init__(self, especie, edad, altura, nombre):
        self.especie = especie
        self.edad = edad
        self.altura = altura
        self.nombre = nombre

    def describir(self):
        return f"Soy el animal {self.nombre}, Especie: {self.especie}, Edad: {self.edad}, Altura: {self.altura}"

class Gato(Animal):
    def __init__(self, especie, edad, altura, nombre, patitas):
        super().__init__(especie, edad, altura, nombre)  # reutiliza el constructor del padre
        self.patitas = patitas # Nueva propiedad Nombre a clase gato 

    def hacer_sonido(self):
        return "Miau 🐱"  

    def presentarse(self):
        return f"tengo las patitas como {self.patitas}"


# ---- Uso ----

gato1 = Gato("Felino", 2, 30, "Michi", 4)

print(gato1.describir())       # método heredado
print(gato1.hacer_sonido())   
print(gato1.presentarse())     # método propio de Gato