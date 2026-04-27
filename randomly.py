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

# dos peleadores se piden al inicio de la pelea
# cada peleador inicia con 100 de hp
# se debe hacer una pelea por turnos
# y cada golpe varia entre 7 y 18
# se termina el match cuando uno de los 2 tiene su hp menor o igual a 0
# se debe mostrar el ganador al final

player1name=input("Selecciona tu jugador player 1: ")
player2name=input("Selecciona tu jugador player 2: ")

print(f"Inicia el combate entre {player1name} y {player2name}.")
player1hp=100
player2hp=100
turno=rd.randint(1,2)

while player1hp > 0 and player2hp > 0:
    if turno % 2 == 0:
        golpe=rd.randint(7,18)
        print(f"{player1name} golpea haciendo {golpe} puntos de hp")
        player2hp-=golpe
    else:
        golpe=rd.randint(7,18)
        print(f"{player2name} golpea haciendo {golpe} puntos de hp")
        player1hp-=golpe
    turno+=1
    player1hptext=("█")*(player1hp)
    player2hptext=("█")*(player2hp)
    print(f'''{player1name} {player1hptext}
{player2name} {player2hptext}''')
    time.sleep(1)

if player1hp>player2hp:
    print(f"{player1name} wins.")
else:
    print(f"{player2name} wins.")










