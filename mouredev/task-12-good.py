def read_products():
    try:
        with open("productos.txt", "r") as f:
            lineas = f.readlines()
    except FileNotFoundError:
        return []

    productos = []
    for linea in lineas:
        nombre, precio, cantidad = linea.strip().split(",")
        productos.append([nombre, float(precio), int(cantidad)])
    
    return productos


def write_products(productos):
    with open("productos.txt", "w") as f:
        for nombre, precio, cantidad in productos:
            f.write(f"{nombre},{precio},{cantidad}\n")


def shop():
    while True:
        action = input(
            "\nQue accion quieres realizar?\n"
            "aniadir | eliminar | actualizar | venta total | venta producto | salir\n"
        ).lower()

        # SALIR
        if action == 'salir':
            print('Saliendo del programa...')
            break

        # AÑADIR
        elif action == 'aniadir':
            nombre = input('Nombre: ').capitalize()

            try:
                precio = float(input('Precio: '))
                cantidad = int(input('Cantidad: '))
            except ValueError:
                print("Error: ingresá números válidos")
                continue

            if precio > 0 and cantidad > 0:
                with open("productos.txt", "a") as f:
                    f.write(f"{nombre},{precio},{cantidad}\n")
                print("Producto añadido")
            else:
                print("Datos inválidos")

        # ELIMINAR
        
        elif action == 'eliminar':
            nombre = input('Producto a eliminar: ').capitalize()
            productos = read_products()

            nuevos = [p for p in productos if p[0] != nombre]

            if len(nuevos) == len(productos):
                print("Producto no encontrado")
            else:
                write_products(nuevos)
                print("Producto eliminado")

        # ACTUALIZAR
        
        elif action == 'actualizar':
            nombre = input('Producto a actualizar: ').capitalize()
            productos = read_products()

            encontrado = False

            for p in productos:
                if p[0] == nombre:
                    try:
                        p[1] = float(input('Nuevo precio: '))
                        p[2] = int(input('Nueva cantidad: '))
                        encontrado = True
                    except ValueError:
                        print("Error: datos inválidos")
                        break

            if encontrado:
                write_products(productos)
                print("Producto actualizado")
            else:
                print("Producto no encontrado")

        # VENTA TOTAL
        
        elif action == 'venta total':
            productos = read_products()
            total = sum(precio * cantidad for _, precio, cantidad in productos)
            print(f"Venta total: {total}")

        # VENTA POR PRODUCTO
        
        elif action == 'venta producto':
            nombre = input("Producto: ").capitalize()
            productos = read_products()

            for prod_nombre, precio, cantidad in productos:
                if prod_nombre == nombre:
                    print(f"Total de {nombre}: {precio * cantidad}")
                    break
            else:
                print("Producto no encontrado")

        else:
            print("Opción no válida")


# Ejecutar
shop()