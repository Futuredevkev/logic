print("--- 1. TRIÁNGULOS SIMPLES ---")

# Triángulo Invertido: Empieza en 10, baja hasta 1
for i in range(10, 0, -1):
    print('*' * i)

# Triángulo Normal: Sube de 1 a 14
for i in range(1, 15):
    print('*' * i)

# Triángulo Alineado a la Derecha
# Lógica: (Espacios = Total - actual) + (Asteriscos = actual)
filas = 4
for i in range(1, filas + 1):
    espacios = " " * (filas - i)
    asteriscos = "*" * i
    print(espacios + asteriscos)


print("\n--- 2. MATRICES Y LISTAS ANIDADAS ---")

# MATRIZ DE MULTIPLICACIÓN (3x3)
matriz = []
for i in range(1, 4):
    fila = []
    for j in range(1, 4):
        fila.append(i * j)
    matriz.append(fila)
print("Matriz 3x3:", matriz)

# TRIÁNGULO DE NÚMEROS IMPARES (Descendente)
# Crea filas con números 1, 3, 5... reduciendo la cantidad de números por fila
N = 5
for i in range(N, 0, -1):
    fila_impares = []
    num = 1 
    for _ in range(i):
        fila_impares.append(num)
        num += 2
    print(*fila_impares) # El '*' desempaqueta la lista para imprimirla bonita

print("\n--- 3. RECURSIVIDAD (Figuras) ---")

def imprimir_piramide_rec(fila_actual, total_filas):
    # CASO BASE: Si ya pasamos el total, nos detenemos
    if fila_actual > total_filas:
        return
    
    # LÓGICA: Espacios + Asteriscos
    espacios = " " * (total_filas - fila_actual)
    asteriscos = "*" * fila_actual
    print(espacios + asteriscos)
    
    # LLAMADA RECURSIVA: Siguiente fila
    imprimir_piramide_rec(fila_actual + 1, total_filas)

imprimir_piramide_rec(1, 4)

def imprimir_cuadrado_rec(fila_actual, lado):
    if fila_actual > lado:
        return
    print("*" * lado)
    imprimir_cuadrado_rec(fila_actual + 1, lado)

print("Cuadrado Recursivo:")
imprimir_cuadrado_rec(1, 3)


print("\n--- 4. ÁRBOLES Y RECURSIVIDAD ---")

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

# Construcción manual del árbol
raiz = Nodo(10)
raiz.izquierdo = Nodo(5)
raiz.derecho = Nodo(15)
raiz.izquierdo.izquierdo = Nodo(3)
raiz.izquierdo.derecho = Nodo(7)

def recorrer_in_order(nodo):
    """
    Flujo In-Order: 
    1. Ir lo más a la izquierda posible.
    2. Leer el valor actual (Raíz).
    3. Ir a la derecha.
    """
    if nodo is None:
        return

    recorrer_in_order(nodo.izquierdo) # Paso 1
    print(f"Visitando nodo: {nodo.valor}") # Paso 2
    recorrer_in_order(nodo.derecho)   # Paso 3

recorrer_in_order(raiz)