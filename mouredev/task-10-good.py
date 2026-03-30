# =========================================================
# 🧱 BASE: EMPLOYEE
# =========================================================

class Employee:
    def __init__(self, name: str, id: int):
        self.name = name 
        self.id = id
    
    def person(self):
        return f"Soy {self.name} con ID {self.id}"


# =========================================================
# 🧠 LIST MANAGER (REUTILIZABLE)
# =========================================================

class ListManager(Employee):

    def _add_to_list(self, target_list, label):
        while True:
            input_user = input(f'Ingresa un {label} (o "salir"): ')

            if input_user.lower() == 'salir':
                break

            if input_user.strip() == '':
                print(f"{label} vacío")
                continue

            if input_user not in target_list:
                target_list.append(input_user)
                print(f"{label} agregado")
            else:
                print(f"{label} duplicado")

    def _remove_from_list(self, target_list, label):
        while True:
            input_user = input(f'Eliminar {label} (o "salir"): ')

            if input_user.lower() == 'salir':
                break

            for item in target_list:
                if item == input_user:
                    target_list.remove(item)
                    print(f"{label} eliminado")
                    break
            else:
                print("No encontrado")


# =========================================================
# 🧠 MANAGER
# =========================================================

class Manager(ListManager):
    def __init__(self, name, id, area):
        super().__init__(name, id)
        self.area = area 
        self.capacityTasks = []
        self.employers = []

    def addTaskRoles(self):
        self._add_to_list(self.capacityTasks, "task")

    def deleteTaskRole(self):
        self._remove_from_list(self.capacityTasks, "task")

    def employerAdd(self):
        self._add_to_list(self.employers, "empleado")

    def deleteEmployer(self):
        self._remove_from_list(self.employers, "empleado")


# =========================================================
# 🧑‍💼 PROJECT MANAGER
# =========================================================

class ProjectManager(ListManager):
    def __init__(self, name, id):
        super().__init__(name, id)
        self.projects = []
        self.tasks = []

    def add_project(self):
        self._add_to_list(self.projects, "proyecto")

    def delete_project(self):
        self._remove_from_list(self.projects, "proyecto")

    def add_task(self):
        self._add_to_list(self.tasks, "task")

    def delete_task(self):
        self._remove_from_list(self.tasks, "task")


# =========================================================
# 👨‍💻 PROGRAMMER
# =========================================================

class Programmer(ListManager):
    def __init__(self, name, id, stack_main, level):
        super().__init__(name, id)
        self.stack_main = stack_main
        self.level = level 
        self.bugs = []
        self.tasks = []
        self.techs = []

    def add_task(self):
        self._add_to_list(self.tasks, "task")

    def delete_task(self):
        self._remove_from_list(self.tasks, "task")

    def report_bug(self):
        bug = input("Ingresa bug: ")
        if bug.strip():
            self.bugs.append(bug)

    def add_tech(self):
        self._add_to_list(self.techs, "tech")
        
        
        
# Crear instancia y llamar a sus funciones para menus interactivos!!
manager = Manager("Kevin", 1, "IT")
pm = ProjectManager("Ana", 2)
programmer = Programmer("Luis", 3, "Python", "Junior")

manager.addTaskRoles()
manager.employerAdd()
print(manager.capacityTasks)
print(manager.employers)