import pygame, constantes, variables
from pygame.locals import *
from botones import *
from pelota import *
from ladrillos import *
from tabla import *

pantalla = pygame.display.set_mode((constantes.ANCHO_PANTALLA, constantes.ALTO_PANTALLA))


#Funcion para mostrar texto en la pantalla
def dibujar_texto(texto, fuente, color_texto, x, y):
    #Convertir el texto en imagen
    imagen = fuente.render(texto, True, color_texto)
    pantalla.blit(imagen, (x, y))


sonido_activado = True
def manejar_altavoces():
    
    global sonido_activado

    if sonido_activado:
        pygame.mixer.music.pause() # Reanuda la música 
        boton_altavoces.imagen = pygame.transform.scale(sin_sonido, (boton_altavoces.rect.width, boton_altavoces.rect.height))

    else:
        pygame.mixer.music.unpause() # Pausa la música 
        boton_altavoces.imagen = pygame.transform.scale(con_sonido, (boton_altavoces.rect.width, boton_altavoces.rect.height))

    sonido_activado = not sonido_activado #invertimos para que se pueda alternar el sonido las veces que se quiera


tabla = crear_tabla(constantes.ANCHO_PANTALLA, constantes.ALTO_PANTALLA, columnas)

def resetear_objetos():
    # Restablecer la pelota
    pelota = resetear_pelota(tabla["x"] + (tabla["ancho"] // 2), tabla["y"] - tabla["alto"])
    
    # Restablecer la tabla
    resetear_tabla(tabla, constantes.ANCHO_PANTALLA, constantes.ALTO_PANTALLA, columnas)
    
    # Crear un nuevo muro
    muro = crear_muro(columnas, filas, constantes.ANCHO_PANTALLA)
    
    return pelota, tabla, muro
