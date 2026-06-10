###########################
#?????????????????????????#
###########################
frutas = {
    1:{"nombre:": "🍎 - Manzana", "precio:": 1000},
    2:{"nombre:": "🍐 - Pera", "precio:": 1200},
    3:{"nombre:": "🍑 - Durazno", "precio:": 2000},
    # 4:{"nombre:": "🍇 - Uva", "precio": 500},
    # 5:{"nombre:": "🍊 - Naranja", "precio": 1250},
    # 6:{"nombre:": "🥭 - Mango", "precio": 1750},
    # 7:{"nombre:": "🍋 - Limon", "precio": 250}
}

print(frutas)
#print(frutas.keys())
#print(frutas.values())
print()


#print(list(frutas.keys())[-1]+1)

def AgregarFrutas():
    o_Nombre=input("Ingrese el nombre del producto: ")
    o_Precio=input("Ingrese el precio del producto: ")
    frutas[list(frutas.key()[-1]+1)] = {"nombre:":o_Nombre, "precio:":o_Precio}
    
def EliminarFrutas():
    pass

def ActualizarFrutas():
    pass

def MostrarFrutas():
    for i,k in list(frutas.items()):
        print(k)
    

def BaseDeDatos():
    while True:
        try:
            print("-"*20)    
            print("1.- Agregar fruta")
            print("2.- Eliminar fruta")
            print("3.- Actualizar fruta")
            print("4.- Mostrar fruta")
            print("5.- Salir")
            op=int(input("Seleccione una opcion: \n"))
            match op:
                case 1:
                    AgregarFrutas()
                case 2:
                    EliminarFrutas()
                case 3:
                    ActualizarFrutas()
                case 4:
                    MostrarFrutas()
                case 5:
                    break
                case _:
                    print("-.-")
        except:
            pass
BaseDeDatos()