#
 #3 EJERCICIO:
 #- Muestra ejemplos de creación de todas las estructuras soportadas por defecto
 #   en tu lenguaje.
# - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 #
# DIFICULTAD EXTRA (opcional):
 # Crea una agenda de contactos por terminal.
 # - Debes implementar funcionalidades de búsqueda, inserción, actualización
 #   y eliminación de contactos.
 # - Cada contacto debe tener un nombre y un número de teléfono.
 # - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
 #   y a continuación los datos necesarios para llevarla a cabo.
 # - El programa no puede dejar introducir números de teléfono no numéricos y con más
 #   de 11 dígitos (o el número de dígitos que quieras).
 # - También se debe proponer una operación de finalización del programa.
 #/
 
agenda = {}

def addContactAgenda(nombre, telefono):
  telefono_str = str(telefono)
  
  if not telefono_str.isdigit() or len(telefono_str) > 11:
    print('el telefono tiene que ser entero y ser mas de 11 digitos')
  else:
    agenda[nombre] = telefono
    print(f'Contacto {nombre} agregado correctamente')
  
  
def searchContacts(nombre):
  if nombre in agenda:
    print(f'Contacto {nombre} tiene el teléfono {agenda[nombre]}')
  else: 
    print(f'No se encontró el contacto "{nombre}".')
  
def deleteContacts(nombre):
  if nombre in agenda:
    agenda.pop(nombre)
    print(f'Se eliminó el contacto "{nombre}".')
  else:
    print(f'No se encontró el contacto "{nombre}".')

def updateContact(nombre, telefono):
  if nombre in agenda:
    telefono_str = str(telefono)
    if not telefono_str.isdigit() or len(telefono_str) > 11:
      print('El teléfono debe ser numérico y tener como máximo 11 dígitos.')
    else:
            agenda[nombre] = telefono
            print(f'Contacto "{nombre}" actualizado con teléfono {telefono}.')
  else: 
    print(f'No se encontró el contacto "{nombre}".')
    
    
while True:
  opcion = input("Elige: agregar, buscar, actualizar, eliminar, salir: ").lower()
  if opcion == "agregar":
    nombre = input('Nombre: ')
    telefono = input("Teléfono: ")
    addContactAgenda(nombre, telefono)
  if opcion == "eliminar":
    nombre = input('Nombre: ')
    deleteContacts(nombre)
  if opcion == "actualizar":
    nombre = input('Nombre: ')
    telefono = input("Teléfono: ")
    updateContact(nombre, telefono)
  if opcion == "buscar":
    nombre = input('Nombre: ')
    searchContacts(nombre)
  if opcion == "salir":
    break

 
# =========================================
# EJERCICIO 3 - ESTRUCTURAS DE DATOS EN PYTHON
# =========================================

# ----------- LISTA (list) -----------
print("=== LISTA ===")

lista = [3, 1, 2]
print("Inicial:", lista)

# Inserción
lista.append(4)
print("Después de insertar:", lista)

# Borrado
lista.remove(1)
print("Después de borrar:", lista)

# Actualización
lista[0] = 10
print("Después de actualizar:", lista)

# Ordenación
lista.sort()
print("Después de ordenar:", lista)


# ----------- TUPLA (tuple) -----------
print("\n=== TUPLA ===")

tupla = (3, 1, 2)
print("Inicial:", tupla)

# Las tuplas no se pueden modificar directamente,
# pero podemos convertirla a lista para trabajarla
temp = list(tupla)

# Inserción
temp.append(4)

# Borrado
temp.remove(1)

# Actualización
temp[0] = 10

# Ordenación
temp.sort()

tupla = tuple(temp)
print("Después de operaciones:", tupla)


# ----------- DICCIONARIO (dict) -----------
print("\n=== DICCIONARIO ===")

dic = {"nombre": "Juan", "edad": 20}
print("Inicial:", dic)

# Inserción
dic["ciudad"] = "Montevideo"
print("Después de insertar:", dic)

# Borrado
del dic["edad"]
print("Después de borrar:", dic)

# Actualización
dic["nombre"] = "Pedro"
print("Después de actualizar:", dic)

# Ordenación (por clave)
dic_ordenado = dict(sorted(dic.items()))
print("Ordenado:", dic_ordenado)


# ----------- SET (set) -----------
print("\n=== SET ===")

conjunto = {3, 1, 2}
print("Inicial:", conjunto)

# Inserción
conjunto.add(4)
print("Después de insertar:", conjunto)

# Borrado
conjunto.remove(1)
print("Después de borrar:", conjunto)

# Actualización
# (no hay actualización directa, se elimina y se agrega)
conjunto.remove(2)
conjunto.add(20)
print("Después de actualizar:", conjunto)

# Ordenación (convertir a lista)
conjunto_ordenado = sorted(conjunto)
print("Ordenado:", conjunto_ordenado)



 