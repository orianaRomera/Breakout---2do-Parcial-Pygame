import pygame
from variables import *

def crear_muro(columnas, filas, ancho_pantalla, alto_bloque=50):
    muro = {}
    ancho_bloque = ancho_pantalla // columnas  # Ancho del ladrillo, para que se distribuyan de manera uniforme
    muro["bloques"] = []  # Lista para almacenar todas las filas de bloques, obtendra todos los bloques que voy a hacer
    
    for fila in range(filas): #itero sobre las filas
        fila_bloques = [] #obtiene todos los bloques de una fila
        for columna in range(columnas): #itero sobre las columnas
            #genero posiciones para cada bloque
            bloque_x = columna * ancho_bloque
            bloque_y = fila * alto_bloque
            #creo el rectangulo
            rectangulo = pygame.Rect(bloque_x, bloque_y, ancho_bloque, alto_bloque)

            # Determinar la fuerza del bloque según la fila
            if fila < 2:
                fuerza = 3
            elif fila < 4:
                fuerza = 2
            elif fila < 6:
                fuerza = 1

            bloque_individual = [rectangulo, fuerza] #cada bloque lo represento como una lista, donde tengo el rectangulo del bloque y la fuerza de este

            #agrego a mi fila de bloques cada bloque individual creado
            fila_bloques.append(bloque_individual)

        #agrego la fila al muro
        muro["bloques"].append(fila_bloques)

    return muro


def dibujar_muro(pantalla, muro):

    for fila in muro["bloques"]: #itero sobre cada fila del muro
        for bloque in fila: #itero sobre cada bloque dentro de la fila
            # Asignar el color del bloque según su nombre
            if bloque[1] == 3: #posicion 1 de mi lista de bloques individual es la fuerza
                bloque_color = bloque_azul
            elif bloque[1] == 2:
                bloque_color = bloque_rojo
            elif bloque[1] == 1:
                bloque_color = bloque_celeste

            # Dibujar el bloque
            pygame.draw.rect(pantalla, bloque_color, bloque[0]) #posicion 0 de mi lista de bloque individual que es donde tengo guardado las dimensiones de mi bloque
            # Dibujar borde del bloque
            pygame.draw.rect(pantalla, color_fondo, bloque[0], 2)