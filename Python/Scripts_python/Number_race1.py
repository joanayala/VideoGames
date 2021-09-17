#Developer: jayala
#Date: 17-sep-2021
'''
    Script description:
    Cree un juego en Python que permita a un sólo jugador
    lanzar dos dados en varias oportunidades consecutivas, y
    finalice el juego cuando obtenga un par de unos [D1:1-D2:2]
'''
import os
from random import randint, uniform, random

print("::: JUEGO CARRERA NUMÉRICA :::")
status = True #Boolean
while status : # while status == True
    key = input(".::: Presiona cualquier tecla para lanzar los dados ...")
    dice1 = randint(1,6)
    dice2 = randint(1,6)
    print("Dice 1: ", dice1)
    print("Dice 2: ", dice2)

    if dice1 == 1 and dice2 == 1 :
        status = False
        print(".::: Sacaste par de unos, el juego ha terminado")
        key = input(".::: Presiona cualquier tecla para salir ...")