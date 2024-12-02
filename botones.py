import pygame, constantes
from claseboton import Boton

#Cargo imagenes de botones
iniciar_juego = pygame.image.load('Imagenes/iniciar_juego.png')
salir_juego = pygame.image.load('Imagenes/salir.png')
reanudar = pygame.image.load('Imagenes/reanudar.png')
salir_escritorio = pygame.image.load('Imagenes/salirescritorio.png')
puntuaciones = pygame.image.load('Imagenes/puntuaciones.png')
con_sonido = pygame.image.load('Imagenes/convolumen.png')
sin_sonido = pygame.image.load('Imagenes/sinvolumen.png')
home = pygame.image.load('Imagenes/casa.png')

#Instancias de botones menu principal
boton_iniciar = Boton(constantes.ANCHO_PANTALLA // 2 - 150, 150, iniciar_juego, 1)
boton_salir = Boton(constantes.ANCHO_PANTALLA // 2 - 150, 450, salir_juego, 1)
boton_puntuaciones = Boton(constantes.ANCHO_PANTALLA // 2 - 150, 300, puntuaciones, 1)
boton_sin_volumen = Boton(520, 610, sin_sonido, 2)
boton_con_volumen = Boton(520, 610, con_sonido, 0.09)
boton_altavoces = Boton(520, 610, con_sonido, 0.09)


#instancias de botones menu en pausa
boton_reanudar = Boton(constantes.ANCHO_PANTALLA // 2 - 150, 150, reanudar, 1)
boton_salir_escritorio = Boton(constantes.ANCHO_PANTALLA // 2 - 150, 450, salir_escritorio, 1)
boton_home = Boton(30, 610, home, 0.3)