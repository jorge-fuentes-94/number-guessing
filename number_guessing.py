import random

def seleccionar_dificultad():
    rango_máximo = input("Por favor, selecciona el número máximo sobre el que tiene que elegir el ordenador: ")
    return rango_máximo 
 
def dar_pistas(pistas):
    if intento== 5:
        if solución //2 == 0:
            print ("Primera pista: el número es par.")
        else:
            print ("Primera Pista: el número es impar.")
    elif intento== 4:
        if solución //5 == 0:
            print ("Segunda pista: el número es divisible por 5.")
        else:
            print ("Segunda pista: el número no es divisible por 5.")
    elif intento== 3:
        mitad = rango_máximo/2
        if solución > mitad:
            print("Tercera pista: el número es superior a {}.".format(mitad))
        else:
            print("Tercera pista: el número es inferior a {}.".format(mitad))
    elif intento== 2:
        if solución //3 == 0:
            print ("cuarta pista: el número es divisible entre 3.")
        else:
            print ("Cuarta pista: el número no es divisible entre 3.")
    elif intento== 1:
        print ("el número al cuadrado es {}.".format(solución*solución))
        
                       
print ("Bienvenido al number_guessing. En este juego tendrás que adivinar el número que ha elegido el ordenador.")
print ("Tienes cinco intentos. En cada fallo se te dará una pista.")

rango_máximo = int(seleccionar_dificultad())
solución = random.randint(1,rango_máximo)
input_jugador = 0
intento = 5

print("El ordenador ha elegido el número. ¡Empezamos con la primera pista!")

for i in range(5):
    dar_pistas(intento)
    input_jugador = (input("Introduce tu respuesta: "))
    if input_jugador == solución:
       print ("¡Felicidades! Has conseguido superar el juego.")
       print ("El número a adivinar era {}.".format(solución))
       print ("Tu puntuación final es {}".format(5-intento))
       break
    elif intento == 1 and input_jugador != solución:
        print ("Lo siento. Has agotado el número de intentos. Tendrás que empezar de nuevo.")
        break
    elif intento == 2:
        intento -= 1
        print ("Has fallado. Te quedan {} intento. Añadimos otra pista.".format(intento))
    else:
        intento -= 1
        print ("Has fallado. Te quedan {} intentos. Añadimos otra pista.".format(intento))
        
        
        
    


