import pygame

class Boton():
    def __init__(self, x, y, imagen, escala):
        #par escalar necesito saber que tan grande es la imagen, alto y ancho original para poder escalar y obtener una imagen de tamaño ajustado segun la escala que uno le indique
        ancho = imagen.get_width()
        alto = imagen.get_height()
        self.imagen = pygame.transform.scale(imagen, (int(ancho * escala), int(alto * escala)))
        #obtener un rectangulo a partir de la imagen
        self.rect = self.imagen.get_rect()
        #posicion del rectangulo en la esquina superrior izquierda
        self.rect.topleft = (x, y)
        #para utilizar si el boton se presiona una sola vez
        self.click = False

    def dibujar(self, imagen): #recibe la imagen sobre la que se dibuja el boton
        accion = False #para indicar si el boton fue presionado 
        #obtener la posicion del mouse para saber donde esta el cursor
        posicion = pygame.mouse.get_pos()
        #saber si el mouse esta sobre uno de los botones
        #si el mouse colisiona con el rectangulo del boton
        if self.rect.collidepoint(posicion):
            #verifico que clik del mouse estoy presionando, el 0 significa la posicion del click izq y que no estaba previamente clickeado 
            if pygame.mouse.get_pressed()[0] == 1 and self.click == False:
                self.click = True #para que solo reconozca que presiono un solo click en el boton
                accion = True #inidica que el boton ha sido presionado
            elif pygame.mouse.get_pressed()[0] == 0: #osea que no se presiono ningun click o se suelta el boton del mouse
                self.click = False 

        #dibujar boton en la pantalla
        imagen.blit(self.imagen, (self.rect.x, self.rect.y))

        return accion #devuelve true si el boton fue presionado o false si no 