#Explicacion uso listas

# lista=[8, 20, 12, 87, 1024]
# #      0   1   2   3     4

# print(lista)

# for elemento in lista:
#     print(f"numero {elemento}")

#Crear una lista de 3, no 4 frutas,
#mostrar cada elemento individualmente

# frutas=["Manzana", "Peras", "Frutillas", "Platanos", "Uva", "Iphone"]
# for fruta in frutas:
#     if fruta[0] in "aeiouAEIOU":
#         print(fruta)

#Hacer una lista de nombres y otra de apellidos
#Mostrar las listas como si fueran nombres
#Vale decir, Diego Robles, 


''' 
modificar carrito de compras para poder utilizarlo con listas

agregar producto
mostrar productos
eliminar productos
actualizar productos
salir

'''



nombres=["Astolfo", "Belle", "Mia", "Sasha"]
apellidos=["Guzman", "Delphine", "Khalifa", "Gray"]

for i in range(len(nombres)):
    print(nombres[i],apellidos[i])