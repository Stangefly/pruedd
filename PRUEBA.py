usuarios= [
    {"nombre": "Angel Vergara","sexo": "M", "contraseña": "migatitomiau",},

]
def ingresar_usuario(nombre,sexo,contraseña):
    nuevo_usuario= {
            "nombre":nombre,
            "sexo":sexo,
            "contraseña":contraseña
        }
    usuarios.append(nuevo_usuario)
    return
def buscar_usuario(nombre):
    for i in usuarios:
        if i[1].lower() == nombre.lower():
            print(f'El sexo del usuario es {i[1]} y la contraseña es {i[2]} ')
            return
        
def eliminar():
    
    for i in usuarios.items():
        if i[1][0]== nombrea:
            usuarios.pop(i[0])
while True:
    print("==================Menu Principal====================")
    print("1.- Ingresar usuario")
    print("2.- Buscar usuario")
    print("3.- Eliminar usuario")
    print("4.- Salir ")
    opcion= int(input("Ingrese una opcion del 1 al 4 "))

    match opcion:

        case 1:
            try:
                nombre=input("Ingrese el nombre de su nuevo usuario: ")
                sexo=input("Ingrese el sexo de su nuevo usuario solo con M o F: ")
                contraseña=float((input("Ingrese la contraseña de su nuevo usuario (Minimo 8 caracteres): ")))
                if sexo.lower() == "m" or sexo.lower() == "f":
                    if len(contraseña) >=8:
                        ingresar_usuario(nombre, sexo, contraseña)
                        print("Usuario ingresado con sumo exito")
                    else:
                        print("Ingrese una contraseña de minimo 8 caracteres")
                else:
                    print("El sexo debe ser solo F o M")
            except:
                SyntaxError
                print(f"Error {SyntaxError}")
        case 2:
            nombre= input("Porfavor ingrese usuario a buscar: ")
            buscar_usuario(nombre)
        case 3:
            nombrea= input("Ingrese el nombre de usuario a eliminar")
            eliminar()  
        case 4:
            print("Gracias por su tiempo")
        case _:
            print("Ingrese datos validos")
    


    