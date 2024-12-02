import os, json, funciones, pygame, variables
from datetime import datetime, date
from pygame.locals import *

pygame.font.init()

fuente3 = pygame.font.SysFont("Constantia", 30)

class Puntaje:
    def __init__(self):
        self.puntos = 0

    def agregar_puntos(self, puntos):
        self.puntos += puntos #incremento puntuacion actual que estaba inicializada en 0
        self.ultimo_puntaje = self.puntos #reflejo la puntuacion acumulada

    def resetear_puntos(self):
        self.puntos = 0
    
    def obtener_puntos(self):
        return self.puntos #devuelvo la puntuacion actual, utilizada mientras estas jugando
    
    def obtener_ultimo_puntaje(self):
        return self.ultimo_puntaje #ultimo puntaje registrado para mostrar al final de la partida cuantos puntos se obtuvieron
        
    def leer_puntaje(self):
        if os.path.exists('puntajes.json'): #verifico si el archivo existe para evitar error en tiempo de ejecucion, lo busque porque me tiraba error y me dio esta solucion
            with open('puntajes.json', 'r') as archivo:
                retorno = json.load(archivo) #si existe, le cargo los datos 
                retorno = sorted(retorno, key=lambda x: x["puntos"], reverse = True)[:15] #ordeno de mayor a menor puntaje, x representa cada elemento de la lista y luego obtiene el valor asociado a la clave
                return retorno
        else:
            return [] #si no existe me devuele un dict vacio, sino me devuelve el contenido
        
    def mostrar_listado_puntajes(self):
        
        variables.flag_puntaje = True
        while variables.flag_puntaje:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        variables.flag_puntaje = False

            funciones.pantalla.fill(variables.color_fondo) 
            funciones.dibujar_texto("MEJORES PUNTAJES", fuente3, variables.color_pausa, 160, 100)

            diccionario = self.leer_puntaje() #obtengo la lista de puntajes del archivo
            x_inicial = 100  # Ajusta según la posición horizontal deseada
            y_inicial = 150  # Ajusta según la posición vertical inicial
            espacio_entre_lineas = 30 #distancia vertical entre cada linea de texto

            for item in diccionario:
                funciones.dibujar_texto(f"Fecha: {item['fecha']} Puntos: {item['puntos']}", fuente3, variables.color_texto, x_inicial, y_inicial)
                y_inicial += espacio_entre_lineas  # Incrementa la posición vertical para la próxima línea

            pygame.display.flip()

    def guardar_puntaje(self):

        diccionario = self.leer_puntaje() #para obtener lista de puntajes actual

        with open('puntajes.json', 'w') as archivo:

            fecha = date.today() #llamo a la fecha de ese dia

            puntaje = {
                'fecha' : fecha,
                'puntos' : self.obtener_ultimo_puntaje()
            } #creo diccionario con la fecha y los puntos 

            puntaje["fecha"] = puntaje["fecha"].strftime("%d-%m-%Y") #le asguno a la clave fecha la fecha actual
        
            diccionario.append(puntaje) #agrego al diccionario ya existente 
        
            json.dump(diccionario, archivo, indent=4) #escribo la lista de puntajes de nuevo
        
            