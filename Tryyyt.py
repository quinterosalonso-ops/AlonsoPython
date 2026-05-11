while True:
    try:
        edad=int(input("Ingrese su edad: "))
        break
    except ValueError as e:
        print("Ingrese una edad valida: ")
        print(e)
print(f"su edad es: {edad}")
