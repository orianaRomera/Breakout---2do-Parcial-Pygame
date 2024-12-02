import pygame, constantes
from variables import *


def crear_pelota(x, y, radio = 10, velocidad_x = 4, velocidad_y = -4, velocidad_max = 5):

    pelota = {}
    pelota["radio"] = radio
    pelota["x"] = x - radio #para que la pelota este centrada
    pelota["y"] = y
    #el ancho y el alto es igual al diametro de la pelota por eso se multiplica por 2
    pelota["rect"] = pygame.Rect(pelota["x"], pelota["y"], radio * 2, radio * 2)
    pelota["speed_x"] = velocidad_x
    pelota["speed_y"] = -velocidad_y
    #para evitar que la pelota se mueva mas rapido de lo permitido
    pelota["velocidad_maxima"] = velocidad_max
    pelota["game_over"] = 0 #en 0 el juego aun no termino

    return pelota

def dibujar_pelota(pantalla, pelota):
    #las coordenadas son las del centro del circulo por eso en cada posicion se le suma el radio
    pygame.draw.circle(pantalla, color_pelota, (pelota["rect"].x + pelota["radio"], pelota["rect"].y + pelota["radio"]), pelota["radio"])

def mover_pelota(pelota, muro, tabla_jugador, puntaje, umbral_colision = 5):
   
    #COLISIONES CON LOS BLOQUES
    for fila in muro["bloques"]: #se recorre todas las filas de bloques y dentro de cada una cada bloque individual
        for bloque in fila:
            if pelota["rect"].colliderect(bloque[0]):  #si el rectangulo de la pelota colisiona con el rectangulo del bloque, que en mi lista el rectangulo esta en la posicion 0
                # Colisiones con los bordes de los bloques
                #compruebo si la colision vino de arriba (la pelota se mueve hacia abajo)y colisiona con la parte superior del bloque, si es asi invierto el sentido de la pelota
                if pelota["rect"].bottom <= bloque[0].top + umbral_colision and pelota["speed_y"] > 0:
                    pelota["speed_y"] *= -1 #la velocidad se invierte para simular el rebote hacia arriba
                #compruebo si la colision vino de abajo (la pelota se mueve hacia arriba) y colisiona con la parte inf del bloque, si es asi invierto el sentido de la pelota
                if pelota["rect"].top >= bloque[0].bottom - umbral_colision and pelota["speed_y"] < 0:
                    pelota["speed_y"] *= -1 #iinvierto velocidad para que rebote hacia abajo
                #compruebo si la colision vino del lado izquierdo
                if pelota["rect"].right >= bloque[0].left - umbral_colision and pelota["speed_x"] > 0:
                    pelota["speed_x"] *= -1
                #compruebo si la colision vino del lado derecho
                if pelota["rect"].left <= bloque[0].right + umbral_colision and pelota["speed_x"] < 0:
                    pelota["speed_x"] *= -1

                # Reducir la fuerza del bloque, los contadores nos indican en que fila y bloque estamos, el inidice 1 es la fuerza que esta en mi lista de bloques individuales
                #verificamos que si mi fuerza del bloque es mayor a 1 siginifica que aun no esta destruido
                if bloque[1] > 1:
                    #si se cumple, la fuerza disminuye en 1 
                    bloque[1] -= 1
                    puntaje.agregar_puntos(10)
                else: #si la fuerza es igual a 1 significa que ya no le queda mas vidas
                    bloque[0] = (0, 0, 0, 0) #los 0 hacen al bloque invisible simulando que no existe
                    puntaje.agregar_puntos(20)

            if bloque[0] != (0,0,0,0):
                pared_destruida = 0 #el bloque no ha sido destruido 
        
    # Si la pared está destruida, fin del juego
    if pared_destruida == 1:
        pelota["game_over"] = 1

    # COLISIONES CON LAS PAREDES
    #si salio de los limites de la pantalla del lado izquierdo o si salio de los limites del lado derecho
    if pelota["rect"].left < 0 or pelota["rect"].right > constantes.ANCHO_PANTALLA:
        pelota["speed_x"] *= -1 #invierto velocidad horizontal
    if pelota["rect"].top < 0: #si la parte superior de la pelota supera el borde sup de la pantalla
        pelota["speed_y"] *= -1 #invierto velocidad, rebota hacia abajo
    if pelota["rect"].bottom > constantes.ALTO_PANTALLA: #si salio hacia abajo de la pantalla
        pelota["game_over"] = -1 #el juego termino, perdio

    # COLISIONES CON LA TABLA
    if pelota["rect"].colliderect(tabla_jugador["rect"]): #si colisiona la pelota con la tabla
    # Comprobar si la pelota colisiona con la parte superior de la tabla (cuando la pelota se esta moviendo hacia abajo)
        if pelota["rect"].bottom <= tabla_jugador["rect"].top + umbral_colision and pelota["speed_y"] > 0:
            pelota["speed_y"] *= -1  # Invertir la velocidad vertical (rebote)
            pelota["speed_x"] += tabla_jugador["direccion"]  # Ajustar la velocidad horizontal según la dirección de la tabla, si la direccion es -1 la pelota va hacia la izq y si la direccion es 1 la pelota va hacia la derecha

            # Limitar la velocidad máxima de la pelota
            if pelota["speed_x"] > pelota["velocidad_maxima"]:
                pelota["speed_x"] = pelota["velocidad_maxima"] 
            elif pelota["speed_x"] < -pelota["velocidad_maxima"]:
                pelota["speed_x"] = -pelota["velocidad_maxima"]
        else: #si la pelota colisiona de una manera diferente, la hace rebotar
            pelota["speed_x"] *= -1  # Invertir la velocidad horizontal (rebote lateral)

    #muevo la pelota hacia arriba o hacia abajo
    pelota["rect"].x += pelota["speed_x"] 
    pelota["rect"].y += pelota["speed_y"]

    return pelota["game_over"] #retorno el el estado del juego en base a la pelota

def resetear_pelota(x, y, radio = 10, velocidad_x = 4, velocidad_y = -4, velocidad_max = 5):
    return crear_pelota(x, y, radio, velocidad_x, velocidad_y, velocidad_max)