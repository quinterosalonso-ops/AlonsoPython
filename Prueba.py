# print("ola")

# #Creando Variables

# titulo="Clima de hoy" #String
# diaDelMes=13 #Int
# mes=4 #Int

# temperature=22.3 #Float
# llueve=False #Bolean

# print(titulo)
# print("Temperatura actual:", temperature, "grados")
# print(diaDelMes, "-", mes)

# if llueve:
#     print("Ta lloviendo, lleva paraguas")
# else:
#     print("No ta lloviendo, lleva parasol")

# precios de tickets
# Pedir password Temu y pin 3435


# _pass="temu"
# _pin=3435

# _Upass=input("Ingresar Password: ")
# _Upin=int(input("Ingresar Pin: "))

# if _pass == _Upass and _pin == _Upin:
#     print("Ingreso exitoso")
# else:
#     print("Ingreso incorrecto")

# print("Calculadora de puntaje de credito")
# _uingresos=int(input("Ingresar Cantidad de ingresos: "))
# _ueducacion=input("Ingresar Nivel Educacional: basico/medio/superior ")
# _unacionalidad=input("Ingresar Nacionalidad: chilena/extranjera ")

# _nacionalidad=0
# if _unacionalidad == "chilena":
#     _nacionalidad=300000

# _educacion=1
# if _ueducacion == "medio":
#     _educacion=1.3
# if _ueducacion == "superior":
#     _educacion=1.5

# _ingresos=0
# if _uingresos >= 1500001:
#     _ingresos=1000000
# elif _uingresos <= 1500000 and _uingresos > 1000000:
#     _ingresos=650000
# elif _uingresos <= 1000000 and _uingresos >= 500000:
#     _ingresos=300000

# print("Su puntaje de credito es de: ",(_ingresos*_educacion)+_nacionalidad)
    
#ejemplo y explicacion de match

# # Precios
# prod1 = 70000
# prod2 = 500000
# prod3 = 580000
# iva= 1.19
# op=0
# Total=0
# while op !=4:
#     print(f"1. Radio estereo Sony ${prod1}")
#     print(f"""2. LGTV 55" Super gamer ${prod2} """)
#     print(f"3. PS5 ${prod3}")
#     print(f"4. Salir")
#     print("Seleccione una opcion")
#     op=int(input())
#     match op:
#         case 1:
#             print(f"El valor del producto con iva incluido es de ${prod1*iva}")
#             Total+=prod1
#         case 2:
#             print(f"El valor del producto con iva incluido es de ${prod2*iva}")
#             Total+=prod2
#         case 3:
#             print(f"El valor del producto con iva incluido es de ${prod3*iva}")
#             Total+=prod3
#         case 4:
#             print("Saliendo del sistema")
#         case _:
#             print("Opcion invalida")
#     print(f"su total es de {Total}")

# cont=1
# num=9
# while cont<=num:
#     print(f"{cont} x {num} = {cont*num}")
#     cont+=1

var1=0
var2=0
op=int(input('''Ingrse una operacion
            1.- Suma
            2.- Resta
            3.- Multiplicacion
            4.- Sivision
            5.- Salir
            '''))

def PedirNum():
    global var1
    global var2
    var1=int(input("ingresar primer numero de la operacion"))
    var2=int(input("ingresar segundo numero de la operacion"))

while op!=5:
    op=int(input('''Ingrse una operacion
            1.- Suma
            2.- Resta
            3.- Multiplicacion
            4.- Sivision
            5.- Salir
            '''))
    match op:
        case 1:
            PedirNum()
            print("el resultado de la operacion es", var1+var2)
        case 2:
            PedirNum()
            print("el resultado de la operacion es", var1-var2)
        case 3:
            PedirNum()
            print("el resultado de la operacion es", var1*var2)
        case 4:
            PedirNum()
            print("el resultado de la operacion es", var1/var2)
        case 5:
            print("Saliendo del sistema")
        case _:
            print("opcion invalida")
    