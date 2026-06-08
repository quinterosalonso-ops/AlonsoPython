# alumno={
#     "nombre":"Shinji Ikari",
#     "edad": 14,
#     "carrera":"piloto"
# }

# for key , value in alumno.items():
#     print(key,value)

# alumno["Email"]="s.ikari@nerv.gob"
# print()
# for key , value in alumno.items():
#     print(key,value)



# productos={
#     1:{"nombre":"Control Inalambrico", "Categoria": "Electronica", "precio": 45000},
#     2:{"nombre":"Pilas Recargables", "Categoria": "Insumos", "precio": 5000},
#     3:{"nombre":"Pasta Termica", "Categoria": "Computacion", "precio": 10000}
# }


# print(productos[2]["Categoria"])
# print(productos[3]["precio"])
# print(productos[1]["nombre"])


frutas = {
    1:{"nombre:": "🍎 - Manzana", "precio": 1500},
    2:{"nombre:": "🍐 - Pera", "precio": 1500},
    3:{"nombre:": "🍑 - Durazno", "precio": 1500},
    4:{"nombre:": "🍇 - Uva", "precio": 1500},
    5:{"nombre:": "🍊 - Naranja", "precio": 1500},
    6:{"nombre:": "🥭 - Mango", "precio": 1500},
    7:{"nombre:": "🍋 - Limon", "precio": 1500}
}

def mostrarFrutas():
    for num, nombre in frutas.items():
        print(f"{num}.- {nombre}")

def agregarFrutas():
    agregar=input("Ingrese un vegetal")
    nuevoKey=list(frutas.keys()[-1])
    frutas[nuevoKey+1]=agregar

def EliminarFrutas():
    borrar=int(input("Cual vegetal borrará?: "))
    del frutas[borrar]

def ActualizarFrutas():
    actualizar=int(input("Cual desea actualizar?"))
    nuevoveg=input("Cual es el nuevo nombre")
    frutas[actualizar]=nuevoveg
    

def VegetablesMenu():
    while True:
        try:
            print("-"*20)    
            print("1.- Agregar vegetal")
            print("2.- Eliminar vegetal")
            print("3.- Actualizar vegetal")
            print("4.- Mostrar vegetal")
            print("5.- Salir")
            op=int(input("Seleccione una opcion: \n"))
            match op:
                case 1:
                    agregarFrutas()
                case 2:
                    EliminarFrutas()
                case 3:
                    ActualizarFrutas()
                case 4:
                    mostrarFrutas()
                case 5:
                    pass
                case _:
                    print("-.-")

                
        except:
            pass
    


VegetablesMenu()
