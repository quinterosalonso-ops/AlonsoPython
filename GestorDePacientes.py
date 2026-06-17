## Crear un gestor de pacientes
pacientes=[{"nombre":"Aquiles Baeza",   "prevision":"Fonasa",   "temperatura":34.6, "grave": False}]
'''
crear al gestor de pacientes en un centro medico
Para poner el nombre se debe validar que no este vacio 
y ademas tenga mas de 8 caracteres
Para la prevision de salud solo exiten 3 posibles valores
Fonasa, Isapre, o Fodesa
Al ingresar un paciente, se debe poner la temperatura
Crear una funcion que valide si esta grave o no
Para que este grave debe tener mas de 39°
Cada atencion vale $25.000
Los despcuentos corresponden a 
Fonasa 54%
Isapre 27%
Fodesa 12,5%
'''
def validarestado(temp):
    if temp >= 37:
        return True
    return False

def IngresarPaciente():
    print(
'''----------------------
Ingresar Paciente
----------------------'''
)    
    try:
        nombre=input("Ingresar nombre: ")
        while len(nombre) < 8:
            nombre=input("El nombre debe tener al menos 8 caracteres: ")
    except:
        pass
    prevision=input("Ingresar prevision: ")
    temp=int(input("Ingresar temperatura: "))
    pacientes.append({"nombre":nombre,   "prevision":prevision,   "temperatura":temp, "grave": validarestado(temp)})

def MostrarPacientes():
    for p in pacientes:
        print(p["nombre"])

def RevisarPaciente():
    nombre=input("Ingresar nombre de paciente a revisar: ")
    for p in pacientes:
        if p["nombre"] == nombre:
            print("El paciente tiene",p["temperatura"],"°C de temperatura")
    

def menu():
    while True:
        try:
            print(
        '''----------------------------
        Bienvenido al sistema
        1-. Ingresar paciente
        2-. Revisar paciente
        3-. Salir
        ----------------------------'''
        )
            op=int(input("Ingrese la opcion deseada: "))
            match op:
                case 1:
                    IngresarPaciente()
                case 2:
                    MostrarPacientes()
                    RevisarPaciente()
                case _:
                    pass
        except:
            pass

menu()