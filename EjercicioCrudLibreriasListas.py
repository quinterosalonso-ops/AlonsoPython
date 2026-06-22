inventario = [
    {"id": 1, "nombre": "Teclado", "precio": 80000,"cantidad":2},
    {"id": 2, "nombre": "Mouse", "precio": 40000,"cantidad":4},
    {"id": 3, "nombre": "Audifonos", "precio": 60000,"cantidad":5}
    ]

def mostrar_inventario():
    for i in inventario:
        print(i["id"], i["nombre"])    

def buscar_producto(id):
    for i in inventario:
        if i["id"] == id:
            print("El",i["nombre"],"Cuesta",i["precio"],"pesos")
    pass

def actualizar_stock(id, nueva_cantidad):
    
    pass

def eliminar_producto(id):
    pass


mostrar_inventario()
buscar_producto(1)