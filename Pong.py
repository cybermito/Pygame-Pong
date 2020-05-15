#pygame.org
import pygame
from pygame.locals import *

pygame.init()

size = 800, 600
ventana = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")
ancho, alto = pygame.display.get_surface().get_size()

colorfondo = 255, 255, 255 #valores RGB
colortextoJugador = 0, 0, 255

pelota = pygame.image.load("imagenes/ball.png")
pelotaXY = pelota.get_rect()
pelotaXY.move_ip(400-16, 300-16)
jugador1 = pygame.image.load("imagenes/bate.png")
jugador1XY = jugador1.get_rect()
jugador1XY.move_ip(50, alto/2)
jugador2 = pygame.image.load("imagenes/palazul.png")
jugador2XY = jugador2.get_rect()
jugador2XY.move_ip(ancho-50, alto/2)

#Cargamos un sonido con la librería pygame
choqueSonido = pygame.mixer.Sound("sonidos/sfx_zap.ogg")

puntosJugador1 = 0
puntosJugador2 = 0

tipoletra = pygame.font.Font("fuentes/mifuente.ttf", 30)
textojugador1 = tipoletra.render("Jugador 1: " + str(puntosJugador1), 0, colortextoJugador)
textojugador2 = tipoletra.render("Jugador 2: " + str(puntosJugador2), 0, colortextoJugador)

velocidad_pelota = [5, 5] #primer elemento posX y segundo posY

run = True
while run:
    
    pelotaXY = pelotaXY.move(velocidad_pelota)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            run = False
    
    if pelotaXY.left < 0 or pelotaXY.right > ancho:
        if pelotaXY.left < 0:
            puntosJugador2 += 1
        if pelotaXY.right > ancho:
            puntosJugador1 += 1
        velocidad_pelota[0] = -velocidad_pelota[0]
        textojugador1 = tipoletra.render("Jugador 1: " + str(puntosJugador1), 0, colortextoJugador)
        textojugador2 = tipoletra.render("Jugador 2: " + str(puntosJugador2), 0, colortextoJugador)
        
        
    if pelotaXY.top < 0 or pelotaXY.bottom > alto:
        velocidad_pelota[1] = -velocidad_pelota[1]
        
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        if jugador1XY[1] < 0:
            jugador1XY = jugador1XY.move(0, 5)
        else:
            jugador1XY = jugador1XY.move(0, -5)            
            
    if keys[pygame.K_DOWN]:
        if jugador1XY[1] > alto-96:
            jugador1XY = jugador1XY.move(0, -5)
        else:
            jugador1XY = jugador1XY.move(0, 5)
            
    if keys[pygame.K_w]:
        if jugador2XY[1] < 0:
            jugador2XY = jugador2XY.move(0, 5)
        else:
            jugador2XY = jugador2XY.move(0, -5)            
            
    if keys[pygame.K_s]:
        if jugador2XY[1] > alto-96:
            jugador2XY = jugador2XY.move(0, -5)
        else:
            jugador2XY = jugador2XY.move(0, 5)
            
    if jugador1XY.colliderect(pelotaXY):
        choqueSonido.play()
        velocidad_pelota[0] = -velocidad_pelota[0]
    if jugador2XY.colliderect(pelotaXY):
        choqueSonido.play()
        velocidad_pelota[0] = -velocidad_pelota[0]
            
    ventana.fill(colorfondo)
    ventana.blit(textojugador1, (20,20))
    ventana.blit(textojugador2, ((ancho/2)+20, 20))
    ventana.blit(pelota, (pelotaXY))
    ventana.blit(jugador1, (jugador1XY))
    ventana.blit(jugador2, (jugador2XY))
    pygame.display.update()
    pygame.display.flip()


pygame.quit()
