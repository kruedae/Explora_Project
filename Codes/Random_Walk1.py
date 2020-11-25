#Programa para simular una caminata aleatoria
import random

def randomwalk(n):
    #Devuelve las coordenadas despues de 'n' bloques de caminata random
    x=0
    y=0
    for i in range(n):
        step = random.choice(['N','S','E','W'])
        if step == 'N':
            y = y + 1
        elif step == 'S':
            y = y - 1
        elif step == 'E':
            x = x + 1
        else:
            x = x - 1
    return (x,y)
N=2500 #Numero de simulaciones
np = 10 #Numero de pasos aleatorios
contador=0
for i in range(N):
    walk = randomwalk(np)
#    print(walk,"Distancia desde el punto inicial = ",
#            abs(walk[0])+abs(walk[1]))
    contador += abs(walk[0])+abs(walk[1])
print("Promedio= ",contador/N)

