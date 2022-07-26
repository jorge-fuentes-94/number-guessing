import random

def control_input(mensaje):
    i = 0
    while i == 0:
        input_simple = input(mensaje)
        if input_simple.isdigit() == False:
           print ("Eso no es un número o el número es negativo. Inténtalo de nuevo.")
        elif int(input_simple) <=0:
            print ("El número es demasiado pequeño. Prueba con un número mayor de cero.")
        else:
            i = 1
    return int(input_simple)

def dar_pistas(intento,rango_máximo,solución):
    pista_a_modificar = ""
    if intento== 5:
        if solución //2 == 0:
            pista_a_modificar = "par"
        else:
            pista_a_modificar = "impar"
        print ("Primera Pista: el número es {}.".format(pista_a_modificar))
    elif intento== 4:
        if solución //5 == 0:
            pista_a_modificar = " "
        else:
            pista_a_modificar = "no "
        print ("Segunda pista: el número {}es divisible por 5.".format(pista_a_modificar))
    elif intento== 3:
        mitad = rango_máximo/2
        if solución > mitad:
            pista_a_modificar = "superior"
        else:
            pista_a_modificar = "inferior"
        print ("Tercera pista: el número es {} a {}.".format(pista_a_modificar, round(mitad)))
    elif intento== 2:
        if solución //3 == 0:
            pista_a_modificar = " "
        else:
            pista_a_modificar = "no "
        print ("Cuarta pista: el número {} divisible entre 3.".format(pista_a_modificar))
    elif intento== 1:
        print ("el número al cuadrado es {}.".format(solución*solución))
 
mensaje_inicial = "Por favor, selecciona el número máximo sobre el que tiene que elegir el ordenador: "
mensaje_standard = "Introduce tu respuesta: "
rango_máximo = (control_input(mensaje_inicial))
solución = random.randint(1,rango_máximo)
input_jugador = 0
intento = 5   
                   
print ("Bienvenido al number_guessing. En este juego tendrás que adivinar el número que ha elegido el ordenador.")
print ("Tienes cinco intentos. En cada fallo se te dará una pista.")
print("El ordenador ha elegido el número. ¡Empezamos con la primera pista!")

while intento > 0:
    dar_pistas(intento,rango_máximo,solución)
    input_jugador = control_input(mensaje_standard)
    if input_jugador == solución:
       print ("¡Felicidades! Has conseguido superar el juego.")
       print ("El número a adivinar era {}.".format(solución))
       print ("Tu puntuación final es {}".format(intento))
       exit()
    elif intento == 1 and input_jugador != solución:
        print ("Lo siento. Has agotado el número de intentos. Tendrás que empezar de nuevo.")
        exit()
    elif intento == 2:
        intento -= 1
        print ("Has fallado. Te quedan {} intento. Añadimos otra pista.".format(intento))
    else:
        intento -= 1
        print ("Has fallado. Te quedan {} intentos. Añadimos otra pista.".format(intento))
        
        
        
        
    


