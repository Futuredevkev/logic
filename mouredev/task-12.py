 #
 # IMPORTANTE: Sólo debes subir el fichero de código como parte del ejercicio.
 #
 # EJERCICIO:
 # Desarrolla un programa capaz de crear un archivo que se llame como
 # tu usuario de GitHub y tenga la extensión .txt.
 # Añade varias líneas en ese fichero:
 # - Tu nombre.
 # - Edad.
 # - Lenguaje de programación favorito.
 # Imprime el contenido.
 # Borra el fichero.
 #
 # DIFICULTAD EXTRA (opcional):
 # Desarrolla un programa de gestión de ventas que almacena sus datos en un 
 # archivo .txt.
 # - Cada producto se guarda en una línea del archivo de la siguiente manera:
 #   [nombre_producto], [cantidad_vendida], [precio].
 # - Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar,
 #   actualizar, eliminar productos y salir.
 # - También debe poseer opciones para calcular la venta total y por producto.
 # - La opción salir borra el .txt.
 #/
 

def read_products():
    with open("./productos.txt", "r") as f:
        lineas = f.readlines() 
    
    productos = []
    for linea in lineas:
        nombre, precio, cantidad = linea.strip().split(",")
        productos.append([nombre, float(precio), int(cantidad)])
      
    return productos


def shop():  
    while True:
        action = input('Que accion quieres realizar? aniadir, eliminar, actualizar, venta total, venta producto, salir\n').lower()
        
        if action == 'salir':
            print('saliendo del programa....')
            break 
        
        elif action == 'aniadir':
            nombre = input('Nombre? ').capitalize()
            precio = float(input('Precio? '))
            cantidad = int(input('Cantidad? '))
            
            if precio > 0 and cantidad > 0:
                with open("productos.txt", "a") as f:
                    f.write(f'{nombre},{precio},{cantidad}\n')
            else:
                print('Datos invalidos') 
        
        elif action == 'eliminar':
            nombre = input('Que producto queres eliminar? ').capitalize()
            productos = read_products()
            productos = [p for p in productos if p[0] != nombre]
            
            with open("productos.txt", "w") as f:
                for p in productos:
                    f.write(f"{p[0]},{p[1]},{p[2]}\n")
        
        elif action == 'actualizar':
            nombre = input('Que producto queres actualizar? ').capitalize()
            productos = read_products()
            
            for p in productos:
                if p[0] == nombre:
                    p[1] = float(input('Nuevo precio: '))
                    p[2] = int(input('Nueva cantidad: '))
            
            with open("productos.txt", "w") as f:
                for p in productos:
                    f.write(f"{p[0]},{p[1]},{p[2]}\n")
        
        elif action == 'venta total':
            productos = read_products()
            total = sum(p[1] * p[2] for p in productos)
            print(f"Venta total: {total}")
        
        elif action == 'venta producto':
            nombre = input("Producto? ").capitalize()
            productos = read_products()
            
            for p in productos:
                if p[0] == nombre:
                    print(f"Total de {nombre}: {p[1] * p[2]}")
        
        else:
            print('esa opcion no existe')
 
#Exampless

import os
 
f = open("./github.txt", "w+")

writeTXT = "Hello There\nMy name Is Kevin\nMy GitHub is FutureDevKev\nMy age 23\nMy favorite languague is Python"

f.write(writeTXT)

f.close()

os.remove("./github.txt")

