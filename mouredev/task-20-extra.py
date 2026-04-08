from enum import Enum
import uuid


class TaskStatus(Enum):
    TODO = 'TODO'
    IN_PROGRESS = 'IN_PROGRESS'
    DONE = 'DONE'
    CANCELLED = 'CANCELLED'


class Task:
    def __init__(self, description: str):
        self.id = uuid.uuid4()
        self.description = description
        self.status = TaskStatus.TODO

    def __str__(self):
        return f"ID: {self.id} - Estado: {self.status.value} - Descripcion: {self.description}"

    def start(self):
        if self.status == TaskStatus.TODO:
          self.status = TaskStatus.IN_PROGRESS
          print('la tarea esta en progreso')
        else: 
          print('no se ha podido iniciar la tarea')

    def complete(self):
        if self.status == TaskStatus.IN_PROGRESS:
          self.status = TaskStatus.DONE
          print('Ha salido todo bien, task completada')
        else: 
          print('No ha podido completarse la tarea')

    def cancel(self):
        if self.status in [TaskStatus.IN_PROGRESS, TaskStatus.TODO]:
          self.status = TaskStatus.CANCELLED
        else:
          print('No se ha podido cancelar la tarea')
    
    def get_description_status(self):
      if self.status == TaskStatus.IN_PROGRESS:
        return 'El task esta en progreso'
      elif self.status == TaskStatus.DONE:
        return 'el task esta terminado'
      elif self.status == TaskStatus.TODO:
        return 'el task no empezo'
      elif self.status == TaskStatus.CANCELLED:
        return 'el task esta cancelado'
        


# ---------------- FUNCIONES ----------------

def makeTasks():
    tasks = []

    while True:
        user = input("Si quieres crear una tarea escribe 'si', si no escribe 'salir': ").lower()

        if user == 'salir':
            break
        elif user == 'si':
            description = input("Escribe la descripción de la tarea: ")
            task = Task(description)
            tasks.append(task)
            print(f'Tarea creada con ID: {task.id}')
        else:
            print("Opción no válida.")

    return tasks


def showListTasks(tasks):
    if not tasks:
        print("No hay tareas creadas.")
        return

    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")


def selectTask(tasks):
    if not tasks:
        print("No hay tareas para seleccionar.")
        return None

    showListTasks(tasks)

    try:
        option = int(input("Elige el número de la tarea: "))
        if option >= 1 and option <= len(tasks):
            return tasks[option - 1]
        else:
            print("Número fuera de rango.")
            return None
    except ValueError:
        print("Debes ingresar un número válido.")
        return None


def menu():
    tasks = makeTasks()

    while True:
        print("\n--- MENÚ ---")
        print("1. Mostrar tareas")
        print("2. Iniciar tarea")
        print("3. Completar tarea")
        print("4. Cancelar tarea")
        print("5. Mostrar descripcion del estado")
        print("6. Salir")

        option = input("Elige una opción: ")

        if option == "1":
            showListTasks(tasks)

        elif option == "2":
            task = selectTask(tasks)
            if task:
                task.start()

        elif option == "3":
            task = selectTask(tasks)
            if task:
                task.complete()

        elif option == "4":
            task = selectTask(tasks)
            if task:
                task.cancel()

        elif option == "5":
          task = selectTask(tasks)
          if task:
               print(task.get_description_status())

        elif option == "6":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida.")


menu()