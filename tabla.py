import pygame

def crear_tabla(ancho_pantalla, alto_pantalla, columnas, alto_tabla = 20, color_tabla = (198, 172, 143), contorno_tabla = (100, 100, 100), velocidad = 10):
    tabla = {}

    # Dimensiones
    tabla["ancho"] = ancho_pantalla // columnas 
    tabla["alto"] = alto_tabla
    #posicion desde donde quiero que arranque (centro)
    tabla["x"] = ancho_pantalla // 2 - tabla["ancho"] // 2 #para que arranque centrado
    tabla["y"] = alto_pantalla - (alto_tabla * 2) #para que arranque en la parte inf de la pantalla
    tabla["velocidad"] = velocidad #velocidad en la que se mueve la tabla
    #rastrea la direccion en la que se mueve la tabla
    tabla["direccion"] = 0
    #creo el rectangulo
    tabla["rect"] = pygame.Rect(tabla["x"], tabla["y"], tabla["ancho"], tabla["alto"])
    tabla["color"] = color_tabla
    tabla["contorno"] = contorno_tabla

    return tabla

def mover_tabla(tabla, ancho_pantalla):
    # Restablecer dirección cada vez que se mueve la tabla
    tabla["direccion"] = 0

    # Manejar movimiento
    tecla = pygame.key.get_pressed() #obtengo estado de todas las taclas presionadas
    if tecla[pygame.K_LEFT] and tabla["rect"].left > 0: #si presiono la tecla izq y si mi tabla no sale de la pantalla
        tabla["rect"].x -= tabla["velocidad"] #muevo la tabla hacia izq
        tabla["direccion"] = -1 #indica que se mueve a la izq
    if tecla[pygame.K_RIGHT] and tabla["rect"].right < ancho_pantalla:
        tabla["rect"].x += tabla["velocidad"]
        tabla["direccion"] = 1

def dibujar_tabla(pantalla, objeto):
    pygame.draw.rect(pantalla, objeto["color"], objeto["rect"])
    pygame.draw.rect(pantalla, objeto["contorno"], objeto["rect"], 2)

def resetear_tabla(objeto, ancho_pantalla, alto_pantalla, columnas, alto_objeto = 20, color_objeto =(198, 172, 143), contorno_obejto = (100, 100, 100), velocidad = 10):
    nuevo_obejeto = crear_tabla(ancho_pantalla, alto_pantalla, columnas, alto_objeto, color_objeto, contorno_obejto, velocidad)
    #actualizo
    objeto.update(nuevo_obejeto)