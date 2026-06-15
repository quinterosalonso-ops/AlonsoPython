#Crear un gestor de estacionamiento
#El estacionamiento tiene 4 pisos
#Cada pso tiene 10 espacios
#Preguntar cuando entra un vehiculo, que tipo de vehiculo es
#Vehiculo ligero 2000
#Vehiculo mediano 3000
#Vehiculo pesado 3500

estacionamiento = {
    1:[2000,3000,3500,3000,3000,3000,3000],
    2:[2000,3500],
    3:[3500,3000,2000],
    4:[2000,2000,2000,2000],
}




# Ingresar
def ingresar():
    print('''
-------------------------------------------------------
Ingrese su tipo de vehiculo
-------------------------------------------------------
1.- Ligero 2000
2.- mediano 3000
3.- pesado 3500
4.- Salir
''')
    op=int(input("Ingrese su opcion: "))
    valor=0
    match op:
        case 1:
            valor=2000
        case 2:
            valor=3000
        case 3:
            valor=3500
        case _:
            return
    for i in estacionamiento:
        if len(estacionamiento[i]) < 10:
            print(f"hay espacio en el piso {i}")
            print(f"estacionando en el piso {i}")
            estacionamiento[i].append(valor)
            break
        print(f"no hay espacio disponible, en el piso {i}")


# Contar
def contar():
    cont=0
    total=0
    for i in estacionamiento:
        for j in range(len(estacionamiento[i])):
            cont+=1
            total+=estacionamiento[i][j]
            #print(estacionamiento[i][j])
        print(f"En el piso {i} hay {len(estacionamiento[i])} autos estacionados")
    print(f"Hay {cont} vehiculos estacionados.")
    

# Ganancia
def ganancia():
    total=0
    for i in estacionamiento:
        for j in range(len(estacionamiento[i])):
            total+=estacionamiento[i][j]
    print(f"la ganancia promedio es de {total}")
    pass


# Verificacion de datos
def verificacion():
    for i in estacionamiento:
        print(estacionamiento[i])

while True:
    try:
        print('''
-------------------------------------------------------
Bienvenido al sistema de ingreso al estacionamiento
-------------------------------------------------------            
1.- ingresar vehiculo
2.- contar vehiculos
3.- ganancia promedio
-------------------------------------------------------
''')
        op=int(input("Seleccione una opcion: "))
        match op:
            case 1:
                ingresar()
                verificacion()
            case 2:
                contar()
                verificacion()
            case 3:
                ganancia()
                verificacion()
    except:
        pass