inventario = [
    {"nombre": "FIFA 24", "precio": 35000, "stock": 12, "promocion": "2x1"},
    {"nombre": "Call of Duty MW2", "precio": 42000, "stock": 5, "promocion": "Descuento 10%"},
    {"nombre": "Zelda: Breath of the Wild", "precio": 50000, "stock": 3, "promocion": None}
]

# TODO: Crear una función para mostrar el inventario
def mostrar_inventario():
    print("===== Inventario =====")
    for i in inventario:
        #print(i)
        print(f'Nombre: {i["nombre"]} - Precio: {i["precio"]} - Stock: {i["stock"]} - Promocion: {i["promocion"]}')

# TODO: Crear una función para agregar un nuevo producto
def agregar_producto(nombre, precio,stock,promocion=None): #Parametros (nombre, precio, stock, promocion=None):
    nuevo_juego = {
        "nombre":nombre,
        "precio":precio,
        "stock":stock,
        "promocion":promocion
    }
    inventario.append(nuevo_juego)
    mostrar_inventario()


# TODO: Crear una función para vender un producto
def vender_producto(nombre): # Parametros(nombre):
    for p in inventario:
        if p["nombre"] == nombre:
            if p["stock"] > 0:
                p["stock"] -=1
                print(f'Producto {nombre} vendido, Stock disponible: {p["stock"]}')
            else:
                print("Producto agotado")
            return
    print("Producto no encontrado")


# TODO: Crear una función para aplicar un descuento
def aplicar_descuento(nombre, porcentaje):#Parametros(nombre, porcentaje):
    for p in inventario:
        if p["nombre"] == nombre:
            descuento = p["precio"] * (porcentaje/100)
            p["precio"] -= int(descuento)
            print(f'Se aplico un {porcentaje}% de descuento a {nombre}, Nuevo precio: {p["precio"]}')
            return
    print("Producto no encontrado")

# TODO: Crear el menú principal con bucle while
def menu():
    # Aquí va tu código...
    while True:
        print("===== Menu de tienda de juegos ======")
        print("1. Mostrar Inventario")
        print("2. Agregar producto")
        print("3. Vender producto")
        print("4. aplicar descuento")
        print("5. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            mostrar_inventario()
        elif opcion == "2":
            nombre = input("Ingrese nombre de producto: ")
            precio = int(input("Ingrese precio: "))
            stock = int(input("Ingrese stock: "))
            agregar_producto(nombre,precio,stock)
        elif opcion == "3":
            nombre_venta = input("Ingrese nombre de producto: ")
            vender_producto(nombre_venta)
        elif opcion == "4":
            nombre_des = input("Ingrese nombre de producto: ")
            porcentaje = int(input("Ingrese porcentaje de descuento: "))
            aplicar_descuento(nombre_des, porcentaje)
        elif opcion == "5":
            print("Saliendo del sistema")
            break
        else:
            print("Opcion no valida")
