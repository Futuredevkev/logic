# ============================================================
# PRÁCTICAS DE SIMULACIONES - LÓGICA DE PROGRAMACIÓN
# ============================================================
# Ejercicios que simulan situaciones reales con while y diccionarios:
# - Recolección de números con validación
# - Simulador de banco (operaciones fijas e interactivo)
# - Historial de temperaturas con clasificación


# ─── EJERCICIO 1: Recolectar números positivos con while ─────
# El usuario ingresa números uno por uno.
# Cuando escribe 'fin' o deja vacío, terminamos.
# Guardamos solo los mayores a 0 y calculamos su promedio.
# try/except captura el error si el usuario escribe algo que no es número.

numerosMayor0 = []

while True:
    entrada = input('Dame un número (o "fin" para terminar): ')
    if entrada == 'fin' or entrada == '':
        break
    try:
        numero = int(entrada)
        if numero > 0:
            numerosMayor0.append(numero)
    except ValueError:
        print("Eso no es un número válido, intentá de nuevo.")

if numerosMayor0:   # si la lista no está vacía
    promedioNumerosMayor0 = sum(numerosMayor0) / len(numerosMayor0)
    print("Promedio de números mayores a 0:", promedioNumerosMayor0)
else:
    print("No ingresaste números mayores a 0.")


# ─── EJERCICIO 2: Simulador de banco con operaciones fijas ───
# Tenemos una lista de operaciones (tuplas) y las procesamos en orden.
# Cada tupla es (tipo, monto).
# Si el tipo es 'retiro' y no hay fondos suficientes, avisamos sin procesar.
# Guardamos cada movimiento exitoso como diccionario en el historial.

saldo = 500
operaciones = [
    ("deposito", 50),
    ("deposito", 200),
    ("retiro", 300),
    ("retiro", 200),
    ("retiro", 70),
]
historial = []
depositos = 0
retiros = 0

for i, operacion in enumerate(operaciones):
    tipo = operacion[0]    # primer elemento de la tupla: 'deposito' o 'retiro'
    monto = operacion[1]   # segundo elemento: el importe

    if tipo == 'deposito':
        saldo += monto
        depositos += 1
        # guardamos el registro completo como diccionario
        registro = {'tipo': tipo, 'monto': monto, 'saldo': saldo, 'indice': i}
        historial.append(registro)

    elif tipo == 'retiro':
        if saldo >= monto:   # solo retiramos si hay saldo suficiente
            saldo -= monto
            retiros += 1
            registro = {'tipo': tipo, 'monto': monto, 'saldo': saldo, 'indice': i}
            historial.append(registro)
        else:
            print(f'Saldo insuficiente para retirar {monto}. Saldo actual: {saldo}')

print("\nHistorial de operaciones fijas:", historial)
print(f'Depósitos: {depositos} | Retiros: {retiros} | Saldo final: {saldo}')


# ─── EJERCICIO 3: Simulador de banco interactivo ─────────────
# El usuario ingresa operaciones hasta escribir 'exit'.
# Misma lógica que arriba, pero con input().
# FIX: el original usaba 'i' del for anterior para contar → confuso.
#      Ahora usamos 'contador_operaciones' propio del while.
# FIX: agregado try/except para el monto, por si el usuario escribe texto.

print("\n--- Banco interactivo ---")
contador_operaciones = 0   # contador independiente para este while

while True:
    tipo = input('¿Depósito o retiro? (o "exit" para salir): ')

    if tipo.lower() == 'exit':
        break

    try:
        monto = int(input('Ingresá el monto: '))
    except ValueError:
        print("Monto inválido, ingresá un número.")
        continue   # 'continue' salta al inicio del while sin ejecutar el resto

    if tipo == 'deposito':
        saldo += monto
        depositos += 1
        registro = {'tipo': tipo, 'monto': monto, 'saldo': saldo, 'indice': contador_operaciones}
        historial.append(registro)

    elif tipo == 'retiro':
        if saldo >= monto:
            saldo -= monto
            retiros += 1
            registro = {'tipo': tipo, 'monto': monto, 'saldo': saldo, 'indice': contador_operaciones}
            historial.append(registro)
        else:
            print(f'Saldo insuficiente. Saldo actual: {saldo}')
    else:
        print("Tipo no reconocido. Escribí 'deposito' o 'retiro'.")

    contador_operaciones += 1

print("Historial completo:", historial)
print(f'Saldo final: {saldo}')


# ─── EJERCICIO 4: Historial de temperaturas ──────────────────
# El usuario ingresa temperaturas día por día.
# Cada temperatura se clasifica en: frío, templado o caliente.
# Al final se muestra el historial completo y el promedio.
# FIX: el promedio se calculaba pero nunca se imprimía → agregado print().
# FIX: guardamos de ZeroDivisionError si el usuario no ingresa nada.

print("\n--- Historial de temperaturas ---")
historialTemperaturas = []
dia = 0
frio = 0
templado = 0
caliente = 0

while True:
    entrada = input('Temperatura del día (o "fin" para terminar): ')
    if entrada.lower() == 'fin':
        break

    try:
        temperatura = int(entrada)
    except ValueError:
        print("Ingresá un número válido.")
        continue

    # Clasificamos por rangos
    if temperatura < 15:
        clasificacion = 'frio'
        frio += 1
    elif 15 <= temperatura <= 25:
        clasificacion = 'templado'
        templado += 1
    else:
        clasificacion = 'caliente'
        caliente += 1

    # Guardamos el día como diccionario
    registro = {"dia": dia, "temperatura": temperatura, "clasificacion": clasificacion}
    historialTemperaturas.append(registro)
    dia += 1

print("Historial:", historialTemperaturas)

# Calculamos el promedio solo si se ingresaron datos (evita ZeroDivisionError)
if historialTemperaturas:
    # list comprehension para extraer solo las temperaturas del historial
    solo_temperaturas = [r["temperatura"] for r in historialTemperaturas]
    historialTemperaturasPromedio = sum(solo_temperaturas) / len(solo_temperaturas)
    print(f"Temperatura promedio: {historialTemperaturasPromedio}")     # FIX: faltaba este print
    print(f"Días fríos: {frio} | Templados: {templado} | Calientes: {caliente}")
else:
    print("No ingresaste ninguna temperatura.")
