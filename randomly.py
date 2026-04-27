# uso y explicacion de random
import random as rd
import time
# print(rd.randint(1, 10))


# num = rd.randint(1,10)

# for i in range(num):
#     print("hola random")

# strike=rd.randint(10,70)

# if strike >= 50:
#     print(f"its a critical hit. Damage: {strike}")
# else:
#     print(f"its no very effective. Damage: {strike}")


# # 3 personas juegan golf
# # cada persona tiene la posibilidad de golpear 3 veces
# # y la distancia varia entre 60 y 190 metros
# # mostrar al final el golpe mas fuerte

# cantidad_jugadores=3

# print("Cada jugador de prepara para golpear")

# def tirojugador():
#     TiroMasAlto=0
#     for i in range(3):
#         dist=rd.randint(60,190)
#         if TiroMasAlto<dist:
#             TiroMasAlto=dist
#     return TiroMasAlto

# for i in range(cantidad_jugadores):
#     print(f"jugador {i+1} lanza la pelota {tirojugador()} metros en su tiro mas alto")
#     time.sleep(2)

# # dos peleadores se piden al inicio de la pelea
# # cada peleador inicia con 100 de hp
# # se debe hacer una pelea por turnos
# # y cada golpe varia entre 7 y 18
# # se termina el match cuando uno de los 2 tiene su hp menor o igual a 0
# # se debe mostrar el ganador al final

# player1name=input("Selecciona tu jugador player 1: ")
# player2name=input("Selecciona tu jugador player 2: ")

# print(f"Inicia el combate entre {player1name} y {player2name}.")
# player1hp=100
# player2hp=100
# turno=rd.randint(1,2)

# while player1hp > 0 and player2hp > 0:
#     if turno % 2 == 0:
#         golpe=rd.randint(7,18)
#         print(f"{player1name} golpea haciendo {golpe} puntos de hp")
#         player2hp-=golpe
#     else:
#         golpe=rd.randint(7,18)
#         print(f"{player2name} golpea haciendo {golpe} puntos de hp")
#         player1hp-=golpe
#     turno+=1
#     player1hptext=("█")*(player1hp)
#     player2hptext=("█")*(player2hp)
#     print(f'''{player1name} {player1hptext}
# {player2name} {player2hptext}''')
#     time.sleep(1)

# if player1hp>player2hp:
#     print(f"{player1name} wins.")
# else:
#     print(f"{player2name} wins.")

# Crea un numero random entre 1 y 100
# Pide al usuario que adivine el numero
# si el usuario pone un numero mayor al generado
# debe decir "te pasaste", en caso contrario
# "El numero a adivinar es mayor"
# solo hay 5 oportunidades de adivinar

numrandom= rd.randint(1,100)
oportunidad=0
correcto=False
while oportunidad<5:
    numsel=int(input("Ingresa un numero entre 0-100: "))
    while numsel >100 or numsel<0:
        numsel=int(input("Numero fuera de rango, intente nuevamente: "))
    if (numsel) > numrandom:
        print("Te pasaste")
    elif numsel < numrandom:
        print("El numero a adivinar es mayor")
    elif numsel==numrandom:
        print("Has adivinado el numero")
        correcto=True
    oportunidad+=1

if correcto==False:
    print("Se acabaron las oportunidades")
    print(f"el numero era secreto era {numrandom}.")

        








