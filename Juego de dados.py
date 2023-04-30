import random
import os
numr1=[]
numr2=[]
fondos1=4000
fondos2=4000
respuesta=0
os.system("cls")
print ("JUEGO DE DADOS")
print ("")
print ("Ambos jugadores cuentan con 4000 monedas para apostar.")
print ("El jugador con la suma de dados mas alta gana.")
print ("El juego acaba cuando uno de los jugadores se queda sin monedas.")
print ("")
print ("")
def ronda():
    sum1=0
    sum2=0
    for x in range(0,3):
        os.system("cls")
        print ("-----------------------------------")
        print ("Jugador 1 tira el dado")
        aux= str(input("Presiona enter para continuar "))
        numr1.insert(x,random.randint(1,6))
        print ("Su numero es ",numr1[x])
        print ("-----------------------------------")
        aux= str(input("Presiona enter para continuar "))
        sum1=sum1+numr1[x]
    for x in range(0,3):
        os.system("cls")
        print ("-----------------------------------")
        print ("Jugador 2 tira el dado")
        aux= str(input("Presiona enter para continuar "))
        numr2.insert(x,random.randint(1,6))
        print ("Su numero es ",numr2[x])
        print ("-----------------------------------")
        aux= str(input("Presiona enter para continuar "))
        sum2=sum2+numr2[x]
    return [sum1,sum2,numr1,numr2]
while fondos1>0 and fondos2>0:
    respuesta=0
    os.system("cls")
    print ("Los fondos del jugador 1 son: ",fondos1)
    print ("Los fondos del jugador 2 son: ",fondos2)
    apuesta1=int(input("Jugador 1 introduzca su apuesta "))
    apuesta2=int(input("Jugador 2 introduzca su apuesta "))
    if apuesta1==apuesta2 and apuesta1<=fondos1 and apuesta1>0:
        fondos1=fondos1-apuesta1
        fondos2=fondos2-apuesta2
        respuesta=1
    elif apuesta1!=apuesta2:
        print ("No hubo acuerdo vuelvan a acordar")
        aux= str(input("Presiona enter para continuar "))
        respuesta=0
    elif apuesta1<=0:
        print ("No se pueden apostar numeros negativos o 0.")
        aux= str(input("Presiona enter para continuar "))
    else:
        print ("No pueden apostar un número superior a sus fondos")
        aux= str(input("Presiona enter para continuar "))
        respuesta=0
    if respuesta==1:
        rondas=ronda()
        if rondas[2][0]==rondas[2][1] and rondas[2][0]==rondas[2][2] and rondas[3][0]==rondas[3][1] and rondas[3][0]==rondas[3][2]:
            if rondas[3][0]==rondas[2][0] and rondas[3][1]==rondas[2][1] and rondas[3][2]==rondas[2][2]:
                print ("AMBOS JUGADORES SACARON TRIPLE DADO!! Esta ronda se repetirá")
                aux= str(input("Presiona enter para continuar "))
                fondos1=fondos1+apuesta1
                fondos2=fondos2+apuesta2
            elif rondas[3][0]>rondas[2][0] and rondas[3][1]>rondas[2][1] and rondas[3][2]>rondas[2][2]:
                print ("El jugador Nº2 sacó una combinacion de triple dado mucho mayor.")
                aux= str(input("Presiona enter para continuar "))
                fondos2=fondos2+apuesta1+apuesta2
            else:
                print ("El jugador Nº1 sacó una combinacion de triple dado mucho mayor.")
                aux= str(input("Presiona enter para continuar "))
                fondos1=fondos1+apuesta1+apuesta2
        elif rondas[3][0]==rondas[3][1] and rondas[3][0]==rondas[3][2]:
            print ("TRIPLE DADO!! El jugador Nº2 gana!")
            aux= str(input("Presiona enter para continuar "))
            fondos2=fondos2+apuesta1+apuesta2
        elif rondas[0]>rondas[1]:
            print ("El jugador 1 gana!! Ganó por una diferencia de: ",rondas[0]-rondas[1])
            aux= str(input("Presiona enter para continuar "))
            fondos1=fondos1+apuesta1+apuesta2
        elif rondas[1]>rondas[0]:
            print ("El jugador 2 gana!! Ganó por una diferencia de: ",rondas[1]-rondas[0])
            aux= str(input("Presiona enter para continuar "))
            fondos2=fondos2+apuesta1+apuesta2
        elif rondas[0]==rondas[1]:
            print ("Se ha empatado, esta ronda se repetirá")
            fondos1=fondos1+apuesta1
            fondos2=fondos2+apuesta2
        else:
            print ("")
if fondos1==0 or fondos2==0:
    if fondos1==0:
        print ("Ganó el jugador 2. Felicitaciones!")
    if fondos2==0:
        print ("Ganó el jugador 1. Felicitaciones!")
