import pygame, constantes, variables
from pygame.locals import *
import pygame.mixer as mixer
from pelota import *
from tabla import *
from ladrillos import *
from funciones import *
from clasepuntaje import Puntaje
from botones import *

#Inicializo pygame y mixer
pygame.init()
mixer.init()

#creo pantalla
pantalla = pygame.display.set_mode((constantes.ANCHO_PANTALLA, constantes.ALTO_PANTALLA))

#Titulo ventana
pygame.display.set_caption("Breakout")
#Icono ventana
icono = pygame.image.load("Imagenes/icono.png")
pygame.display.set_icon(icono)

clock = pygame.time.Clock()
fps = 60

#cargar musica
pygame.mixer.music.load("breakout.mpeg")
#ajustar el volumen
pygame.mixer.music.set_volume(0.5)

#fuentes del juego
fuente = pygame.font.SysFont("Constantia", 25)
fuente2 = pygame.font.SysFont("Constantia", 15)
fuente3 = pygame.font.SysFont("Constantia", 30)

#creo instancia de ladrillo
muro = crear_muro(columnas, filas, constantes.ANCHO_PANTALLA)

#creo instancia de tabla
tabla = crear_tabla(constantes.ANCHO_PANTALLA, constantes.ALTO_PANTALLA, columnas)

#creo instancia de pelota
pelota = crear_pelota(tabla["x"] + (tabla["ancho"] // 2), tabla["y"] - tabla["alto"])

#creo instancia de puntaje
puntaje = Puntaje()

flag_correr = True

while flag_correr:

    #Velocidad del juego
    clock.tick(fps)

    if iniciar == False: #significa que el juego no empezo y estoy en mi menu
        #dibujo menu
        pantalla.fill(color_fondo)
        #agrego los botones
        if boton_iniciar.dibujar(pantalla):
            iniciar = True #cambia a verdadero por lo tanto inicia el juego
            puntaje.resetear_puntos()
        if boton_salir.dibujar(pantalla):
            flag_correr = False #salgo de mi bucle por lo tanto salgo del juego
        if boton_puntuaciones.dibujar(pantalla):
            puntaje.mostrar_listado_puntajes()
        if boton_altavoces.dibujar(pantalla): 
            manejar_altavoces()
                
    else:
        if juego_en_pausa: #significa que pongo pausa
            pantalla.fill(color_fondo)
            #dibujo los botones de mi menu secundario
            if boton_reanudar.dibujar(pantalla):
                juego_en_pausa = False #vuelvo al juego
            if boton_puntuaciones.dibujar(pantalla):
                puntaje.mostrar_listado_puntajes()
            if boton_salir_escritorio.dibujar(pantalla):
                flag_correr = False #salgo de mi bucle por lo tanto salgo del juego
            if boton_altavoces.dibujar(pantalla):
                manejar_altavoces()
            if boton_home.dibujar(pantalla):
                iniciar = False
                pelota, tabla, muro = resetear_objetos() #busque otras maneras de hacerlo para no poner tres variables juntas asi pero no supe como y preferia dejarlo asi antes que repetir dos veces 3 lineas de codigo (que es la funcion que se encuentra en el modulo de funciones)

        else:
            pantalla.fill(color_fondo)
            #dibujo texto de poner pausa
            dibujar_texto("PRESIONA BARRA ESPACIADORA PARA PAUSAR", fuente2, color_pausa, 140, 652)
            #dibujo mis objetos
            dibujar_muro(pantalla, muro)
            dibujar_tabla(pantalla, tabla)
            dibujar_pelota(pantalla, pelota)
            dibujar_texto(f"Score {puntaje.obtener_puntos()}", fuente3, color_pausa, 10, 10)
            
            if pelota_en_vivo == True: #mientras la pelota sea verdadera voy a poder mover
                #Muevo tabla y pelota
                mover_tabla(tabla, constantes.ANCHO_PANTALLA)
                game_over = mover_pelota(pelota, muro, tabla,puntaje)
                if game_over != 0: #si el juego termino, cambio el estado de la pelota
                    pelota_en_vivo = False
                    puntaje.guardar_puntaje()
                    puntaje.resetear_puntos()
            
            #Instrucciones al jugador
            if not pelota_en_vivo:
                if game_over == 1: 
                    dibujar_texto("HAS GANADO", fuente, color_texto, 215, constantes.ALTO_PANTALLA // 2 + 50)
                    dibujar_texto(f"Tu puntaje fue de {puntaje.obtener_ultimo_puntaje()} puntos", fuente, color_texto, 150, constantes.ALTO_PANTALLA // 2 + 80)
                    dibujar_texto("Haz click en cualquier lugar para comenzar", fuente, color_texto, 70, constantes.ALTO_PANTALLA // 2 + 100)

                elif game_over == -1:
                    dibujar_texto("HAS PERDIDO", fuente, color_texto, 215, constantes.ALTO_PANTALLA // 2 + 50)
                    dibujar_texto(f"Tu puntaje fue de {puntaje.obtener_ultimo_puntaje()} puntos", fuente, color_texto, 150, constantes.ALTO_PANTALLA // 2 + 80)
                    dibujar_texto("Haz click en cualquier lugar para comenzar", fuente, color_texto, 70, constantes.ALTO_PANTALLA // 2 + 110)

    for event in pygame.event.get():
        #Cerrar ventana
        if event.type == QUIT:
            pygame.quit()
            quit()

        #Cuando aprieto un boton del mouse el juego comienza
        if event.type == pygame.MOUSEBUTTONDOWN and pelota_en_vivo == False:
            pelota_en_vivo = True
            pelota, tabla, muro = resetear_objetos()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                juego_en_pausa = True #pongo el juego en pausa si aprieto space

    if not esta_reproduciendo_musica:
        mixer.music.play(-1) #el -1 es para que se reproduzca en bucle la cancion sin que se corte 
        esta_reproduciendo_musica = True

    #Actualizo la pantalla
    pygame.display.flip()

mixer.music.stop()