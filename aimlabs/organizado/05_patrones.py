# ============================================================
# PRÁCTICAS DE PATRONES CON ASTERISCOS - LÓGICA DE PROGRAMACIÓN
# ============================================================
# Ejercicios para imprimir formas usando bucles.
# La clave es controlar la cantidad de espacios y asteriscos por fila.
# Usamos multiplicación de strings: '*' * 3 → '***'


n = 5   # cantidad de filas (cambiar este número cambia el tamaño de todos los patrones)


# ─── EJERCICIO 1: Pirámide centrada ──────────────────────────
# Fila 1: 4 espacios + 1 asterisco
# Fila 2: 3 espacios + 3 asteriscos
# Fila 3: 2 espacios + 5 asteriscos
# ...
# Fórmula: espacios = n - i, asteriscos = 2*i - 1

print("--- Pirámide ---")
for i in range(1, n + 1):
    espacios = n - i        # los espacios disminuyen una unidad por fila
    asteriscos = 2 * i - 1  # los asteriscos crecen: 1, 3, 5, 7, 9...
    print(' ' * espacios + '*' * asteriscos)


# ─── EJERCICIO 2: Rectángulo de asteriscos ───────────────────
# Imprime n filas, cada una con exactamente n asteriscos.
# FIX: este bloque estaba dentro del for de la pirámide (indentado mal),
#      ahora está correctamente afuera como un loop independiente.

print("--- Rectángulo ---")
for i in range(n):
    print('*' * n)


# ─── EJERCICIO 3: Triángulo invertido ────────────────────────
# Primera fila: n asteriscos, segunda: n-1, ..., última: 1.
# FIX: igual que el rectángulo, estaba anidado dentro del for de la pirámide.

print("--- Triángulo invertido ---")
for i in range(n):
    asteriscos = n - i   # empieza en n y va bajando hasta 1
    print('*' * asteriscos)
