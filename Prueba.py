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

print("Calculadora de puntaje de credito")
_uingresos=int(input("Ingresar Cantidad de ingresos: "))
_ueducacion=input("Ingresar Nivel Educacional: basico/medio/superior ")
_unacionalidad=input("Ingresar Nacionalidad: chilena/extranjera ")

_nacionalidad=0
if _unacionalidad == "chilena":
    _nacionalidad=300000

_educacion=1
if _ueducacion == "medio":
    _educacion=1.3
if _ueducacion == "superior":
    _educacion=1.5

_ingresos=0
if _uingresos >= 1500001:
    _ingresos=1000000
elif _uingresos <= 1500000 and _uingresos > 1000000:
    _ingresos=650000
elif _uingresos <= 1000000 and _uingresos >= 500000:
    _ingresos=300000

print("Su puntaje de credito es de: ",(_ingresos*_educacion)+_nacionalidad)
    


