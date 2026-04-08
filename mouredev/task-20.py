# =========================================
# IMPORTS
# =========================================

# Enum permite crear tipos con valores constantes (como estados)
from enum import Enum

# uuid sirve para generar IDs únicos (como identificadores de pedidos)
import uuid


# =========================================
# ENUM DE ESTADOS DEL PEDIDO
# =========================================

# Definimos los posibles estados que puede tener un pedido
class Status(Enum):
    PENDING = "PENDING"       # Pedido creado pero no enviado
    SEND = "SEND"             # Pedido enviado
    DELIVERED = "DELIVERED"   # Pedido entregado
    CANCELLED = "CANCELLED"   # Pedido cancelado


# =========================================
# CLASE PEDIDO
# =========================================

class Pedido:
    def __init__(self):
        # Genera un ID único automáticamente
        self.id = uuid.uuid4()
        
        # Estado inicial del pedido
        self.status = Status.PENDING

    # Método que define cómo se imprime el objeto
    def __str__(self):
        return f"ID: {self.id} - Estado: {self.status.value}"

    # -------------------------------------
    # CAMBIOS DE ESTADO
    # -------------------------------------

    def send(self):
        # Solo se puede enviar si está pendiente
        if self.status == Status.PENDING:
            self.status = Status.SEND
            print("El pedido fue enviado.")
        else:
            print(f"No se puede enviar un pedido en estado {self.status.value}.")

    def deliver(self):
        # Solo se puede entregar si ya fue enviado
        if self.status == Status.SEND:
            self.status = Status.DELIVERED
            print("El pedido fue entregado.")
        else:
            print(f"No se puede entregar un pedido en estado {self.status.value}.")

    def cancel(self):
        # Se puede cancelar si está pendiente o enviado
        if self.status in [Status.PENDING, Status.SEND]:
            self.status = Status.CANCELLED
            print("El pedido fue cancelado.")
        else:
            print(f"No se puede cancelar un pedido en estado {self.status.value}.")

    # -------------------------------------
    # DESCRIPCIÓN DEL ESTADO
    # -------------------------------------

    def description(self):
        # Devuelve un texto según el estado actual
        if self.status == Status.PENDING:
            return "El pedido está pendiente."
        elif self.status == Status.SEND:
            return "El pedido fue enviado."
        elif self.status == Status.DELIVERED:
            return "El pedido ya fue entregado."
        elif self.status == Status.CANCELLED:
            return "El pedido fue cancelado."


# =========================================
# FUNCIONES DEL SISTEMA
# =========================================

def makePedido():
    """
    Permite crear pedidos de forma interactiva.
    Devuelve una lista de pedidos creados.
    """
    pedidos = []

    while True:
        user = input("Si quieres crear un pedido escribe 'si', si no escribe 'salir': ").lower()

        if user == "salir":
            break
        elif user == "si":
            pedido = Pedido()
            pedidos.append(pedido)
            print(f"Pedido creado con ID: {pedido.id}")
        else:
            print("Opción no válida.")

    return pedidos


def showListPedidos(pedidos):
    """
    Muestra todos los pedidos con su índice.
    """
    if not pedidos:
        print("No hay pedidos creados.")
        return

    # enumerate permite recorrer lista con índice
    for i, pedido in enumerate(pedidos, start=1):
        print(f"{i}. {pedido}")


def selectPedido(pedidos):
    """
    Permite seleccionar un pedido de la lista.
    Devuelve el pedido elegido o None si hay error.
    """
    if not pedidos:
        print("No hay pedidos para seleccionar.")
        return None

    showListPedidos(pedidos)

    try:
        option = int(input("Elige el número del pedido: "))

        # Validamos rango
        if option >= 1 and option <= len(pedidos):
            return pedidos[option - 1]  # Ajuste de índice (lista empieza en 0)
        else:
            print("Número fuera de rango.")
            return None

    except ValueError:
        print("Debes ingresar un número válido.")
        return None


# =========================================
# MENÚ PRINCIPAL
# =========================================

def menu():
    """
    Sistema principal interactivo.
    """
    pedidos = makePedido()

    while True:
        print("\n--- MENÚ ---")
        print("1. Mostrar pedidos")
        print("2. Enviar pedido")
        print("3. Entregar pedido")
        print("4. Cancelar pedido")
        print("5. Mostrar descripción de un pedido")
        print("6. Salir")

        option = input("Elige una opción: ")

        if option == "1":
            showListPedidos(pedidos)

        elif option == "2":
            pedido = selectPedido(pedidos)
            if pedido:
                pedido.send()

        elif option == "3":
            pedido = selectPedido(pedidos)
            if pedido:
                pedido.deliver()

        elif option == "4":
            pedido = selectPedido(pedidos)
            if pedido:
                pedido.cancel()

        elif option == "5":
            pedido = selectPedido(pedidos)
            if pedido:
                print(pedido.description())

        elif option == "6":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida.")


# Ejecutamos el sistema
menu()


# =========================================
# EJEMPLO SIMPLE: ENUM DE DÍAS
# =========================================

class WeekDays(Enum):
    Monday = 1
    Tuesday = 2
    Wednesday = 3
    Thursday = 4 
    Friday = 5 
    Saturday = 6
    Sunday = 7


def dayOfWeek():
    """
    Recibe un número del 1 al 7 y devuelve el día correspondiente.
    """
    try:
        day = int(input("Consulta los días de la semana (1 al 7): "))
        
        # Convertimos el número al Enum
        day_enum = WeekDays(day)

        # .name devuelve el nombre (Monday, Tuesday...)
        print(f"El día es: {day_enum.name}")

    except ValueError:
        print("Número inválido")