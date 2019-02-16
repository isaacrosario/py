import random
continuar =1
while continuar ==1:
    print("Bienvenido a YourMasterMind")
    print("eliga la dificultad del juego <1=Easy, 2=Hard 3=Nightmare")
    dificultad= int(input("Digite el numero de la dfificulad: "))

#asiganacion el niuvel de deificiulata
    if dificultad ==1:
        cant_digitos= 3
    elif dificultad ==2:
        cant_digitos=4
    elif dificultad==3:
        cant_digitos =5

    digitos = ('0','1','2','3','4','5','7','8','9')
    codigo = ''


#serlccion los simbolos

    for i in range(cant_digitos):
        elegido = random.choice(digitos)
        while elegido in codigo:
            elegido = random.choice(digitos)
        codigo  = codigo + elegido

    print("Tienes que adivinar un codigo de ",cant_digitos, " digitos distintos")
    propuesta = input("Que codigo propones?")
    

    intentos = 1

    while propuesta  !=  codigo:
        intentos = intentos  + 1 
        aciertos = 0 
        coincidencia= 0 
        for i in range(cant_digitos):
            if propuesta[i] == codigo[i]:
                aciertos = aciertos  + 1 
            elif propuesta[i] in codigo:
                coincidencia = coincidencia + 1
        print("Tu propuesta (",propuesta,") tienes ", aciertos ,"aciertos y ",coincidencia, "coicidencia")
        propuesta = input("Propon otro codigo: ")

    print("FELICIDES ! Adivinaste el codigo en ", intentos,"intentos,"," el codigo es: " ,codigo)
    continuar = int(input("Desea seguir jugando?: <1=si, 0=no>: "))
            



 