# #Sin argumento y sin retorno
# def saludo():
#     print("Hola sin argumento y sin retorno")

# #Sin argumento y con retorno
# def suma():
#     num1 = 3
#     num2 = 5
#     return(num1 + num2)

# def esMayor():
#     edad=24
#     if edad>=18:
#         return True
#     return False

# #Con argumento y sin retorno

# def Saludame(name):
#     print(f"Hola {name}.")

# Saludame("Alonso")


# def calculariva(neto):
#     print("el precio con iva es:",neto*1.19)

# calculariva(1000)

# #Con argumento y con retorno
# def sumaCA(n1,n2):
#     return(n1+n2)

# def calcularIVAca(neto):
#     return neto*1.19

# print("El resultado es:", sumaCA(7,10))
# print("El resultado con iva es:", calcularIVAca(10000))

# numeros = input("Ingresa una lista de numeros para saber cuales son pares y cuales son impares:")

# listanum = numeros.split(" ")

# for a in range(len(listanum)):
#     listanum[a] = int(listanum[a])

# pares = []
# impares = []

# for i in listanum:
#     if i % 2 == 0:
#         pares.append(i)
#     else:
#         impares.append(i)

# print("Los nueros pares son:",pares)
# print("Los numeros impares son:",impares)

def PedirNotas(nums):
    ListaDeNotas = nums.split(" ")
    for a in range(len(ListaDeNotas)):
        ListaDeNotas[a] = int(ListaDeNotas[a])
    return ListaDeNotas

def Sacarpromedio(num):
    Notas = PedirNotas(num)
    sum = 0
    for n in range(len(Notas)):
        sum += Notas[n]
    Promedio = sum/len(Notas)
    return Promedio

print(Sacarpromedio(input("Ingresa tus notas separadas con un espacio:")))











