# while True:
#     try:
#         edad=int(input("Ingrese su edad: "))
#         break
#     except ValueError as e:
#         print("Ingrese una edad valida: ")
#         print(e)
# print(f"su edad es: {edad}")

# for i in range(10):
#     n1=int(input("Ingrese un numero: "))
#     if n1%2!=0:
#         break

# sum=0
# while True:
#     try:
#         num = int(input("Ingrese un numero: "))
#         sum+=num
#         if num==0:
#             break
#     except:
#         print("Solo numeros enteros")
# print(sum)

#ejemplo y ecplicacion de match
op=0
total=0
while op!=4:
    try:
        print("1.- Radio sterero Sony $70.000")
        print("2.- LGTV 55 pulgadas Super gamer $500.000 ")
        print("3.- PS5 $580.000")
        print("4.- Salir")
        print("Seleccione una opcion")
        op=int(input())
        match op:
            case 1:
                print("El precio a pagar es ", 70000*1.19)
                total+=70000*1.19
            case 2:
                print("El precio a pagar es ", 500000*1.19)
                total+=500000*1.19
            case 3:
                print("El precio a pagar es ", 580000*1.19)
                total+=580000*1.19
            case 4:
                print(f"Su total a pagar es {total}")
            case _:
                print("Opcion Inválida")  # opcion por defecto
    except ValueError as e:
        print("Ingrese un numero entero: ")