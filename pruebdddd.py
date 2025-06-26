turistas = {"001": ["John Doe", "Estados Unidos", "12-01-2024"],
            "002": ["Emily Smith", "Estados Unidos", "23-03-2024"],
            "012": ["Julian Martinez", "Argentina", "19-09-2023"],
            "014": ["Agustin Morales", "Argentina", "28-03-2024"],
            "005": ["Carlos Garcia", "Mexico", "10-05-2024"],
            "006": ["Maria Lopez", "Mexico", "08-12-2023"],
            "007": ["Joao Silva", "Brasil", "20-06-2024"],
	        "003": ["Michael Brown", "Estados Unidos", "05-07-2023"],
	        "004": ["Jessica Davis", "Estados Unidos", "15-11-2024"],
            "008": ["Ana Santos", "Brasil", "03-10-2023"],
            "010": ["Martin Fernandez", "Argentina", "13-02-2023"],
            "011": ["Sofia Gomez", "Argentina", "07-04-2024"],
           }

""" 
1.- Agregar
2.- Buscar por pais
3.- Eliminar por nombre
4.- Salir
"""

def agregar(id,nombre,pais,fecha):
    buscado = False
    for item in turistas.keys():
        if(item==id):
            buscado = True
            break
    if(buscado):
        return False
    else:
        turista = {id:[nombre,pais,fecha]}
        turistas.update(turista)
        return True

def buscarPorPais(pais):
    for item in turistas.values():
        if(item[1].lower()==pais.lower()):
            print(f"El turista {item[0]} viajo a {item[1]} el {item[2]}")
            
def eliminar():
    nombre = input("Ingrese nombre del turista: ")
    for item in turistas.items():
        """ item[1][0] = nombre
            item[0] = llave
        """
        if(item[1][0]==nombre):
            turistas.pop(item[0])
            break
        

opcion = 0 

while opcion!=4:
    print("Bienvenido")
    print("1.- Agregar Turista")
    print("2.- Buscar Turista")
    print("3.- Eliminar Turista")
    print("4.- Salir")
    opcion=int(input("Ingrese la opcion que desea: "))
    match opcion:
        case 1:
            id = input("Ingrese ID del turista: ")
            if(len(id)>0):
                nombre = input("Ingrese nombre del turista: ")
                if(len(nombre)>0):
                    pais = input("Ingrese Pais a visitar")
                    if(len(pais)>0):
                        fecha = input("Ingrese fecha del viaje: ")
                        if(len(fecha)>0):
                            if(agregar(id,nombre,pais,fecha)):
                                print("Agregado con exito")
                            else:
                                print("Registro ya existe")
                        else:
                            print("Fecha no puede estar vacia")
                    else:
                        print("Pais no puede estar vacio")
                else:
                    print("Nombre no puede estar vacio")
            else:
                print("ID no puede estar vacio")
        case 2:
            pais = input("Ingrese pais que desea buscar: ")
            buscarPorPais(pais)
        case 3:
            eliminar()
        case 4:
            print("Cerrando programa...")
        case _:
            print("Opcion fuera de rango")
