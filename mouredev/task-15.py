from datetime import datetime
 
 #
 # EJERCICIO:
 # Crea dos variables utilizando los objetos fecha (date, o semejante) de tu lenguaje:
 # - Una primera que represente la fecha (día, mes, año, hora, minuto, segundo) actual.
 # - Una segunda que represente tu fecha de nacimiento (te puedes inventar la hora).
 # Calcula cuántos años han transcurrido entre ambas fechas.
 #
 # DIFICULTAD EXTRA (opcional):
 # Utilizando la fecha de tu cumpleaños, formatéala y muestra su resultado de
 # 10 maneras diferentes. Por ejemplo:
 # - Día, mes y año.
 # - Hora, minuto y segundo.
 # - Día de año.
 # - Día de la semana.
 # - Nombre del mes.
 # (lo que se te ocurra...)
 #/
 
 
myBirthday = datetime(2002, 10, 3, 12, 30, 5)
now = datetime.now()

days = (now - myBirthday).days
anios = days / 365
anios_int = int(anios)

print(f'han pasado {anios_int} anios')



# EXTRA 

# 1. Día / Mes / Año
print(myBirthday.strftime('%d/%m/%Y'))  # 03/10/2002

# 2. Año-Mes-Día (formato ISO)
print(myBirthday.strftime('%Y-%m-%d'))  # 2002-10-03

# 3. Hora completa
print(myBirthday.strftime('%H:%M:%S'))  # 12:30:05

# 4. Día de la semana (nombre)
print(myBirthday.strftime('%A'))  # Thursday

# 5. Día de la semana (abreviado)
print(myBirthday.strftime('%a'))  # Thu

# 6. Nombre del mes
print(myBirthday.strftime('%B'))  # October

# 7. Mes abreviado
print(myBirthday.strftime('%b'))  # Oct

# 8. Día del año (1-366)
print(myBirthday.strftime('%j'))  # 276

# 9. Semana del año
print(myBirthday.strftime('%U'))  # semana número

# 10. Formato completo “humano”
print(myBirthday.strftime('%A, %d de %B de %Y - %H:%M:%S'))




