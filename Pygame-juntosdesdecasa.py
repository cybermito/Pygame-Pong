import pygame
from pygame.locals import *

pygame.init()

size = 800, 600
ventana = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")

ancho, alto = pygame.display.get_surface().get_size()

blanco = 255, 255, 255
colortextoJugador = 0, 0, 0
colorGanador = 255, 0, 0

pelota = pygame.image.load("imagenes/ball.png")
jugador1 = pygame.image.load("imagenes/bate.png")
jugador2 = pygame.image.load("imagenes/palazul.png")
pelotaXY = pelota.get_rect()
jugador1XY = jugador1.get_rect()
jugador1XY.move_ip(50, alto/2)
jugador2XY = jugador2.get_rect()
jugador2XY.move_ip(750, alto/2)
puntosJugador1 = 0
puntosJugador2 = 0
ganador = False

tipoletra = pygame.font.Font("fuentes/mifuente.ttf", 40)
textoJugador1 = tipoletra.render("Jugador 1: " + str(puntosJugador1), 0, colortextoJugador)
textoJugador2 = tipoletra.render("Jugador 2: " + str(puntosJugador2), 0, colortextoJugador)
textoGanador = tipoletra.render("", 0, colorGanador)

velocidad_pelota = [1, 1]
velocidad_jugador = [1, 1]

run = True
while run:

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        if jugador1XY[1] < 0:
            jugador1XY = jugador1XY.move(0, 1)
        else:
            jugador1XY = jugador1XY.move(0, -1)
            
    if keys[pygame.K_DOWN]:
        if jugador1XY[1] > alto-96:
            jugador1XY = jugador1XY.move(0, -1)
        else:
            jugador1XY = jugador1XY.move(0, 1)
            
    if keys[pygame.K_w]:
        if jugador2XY[1] < 0:
            jugador2XY = jugador2XY.move(0, 1)
        else:
            jugador2XY = jugador2XY.move(0, -1)
            
    if keys[pygame.K_s]:
        if jugador2XY[1] > alto-96:
            jugador2XY = jugador2XY.move(0, -1)
        else:
            jugador2XY = jugador2XY.move(0, 1)
        
    if jugador1XY.colliderect(pelotaXY):
        velocidad_pelota[0] = -velocidad_pelota[0]
        
    if jugador2XY.colliderect(pelotaXY):
        velocidad_pelota[0] = -velocidad_pelota[0]
        
    pelotaXY = pelotaXY.move(velocidad_pelota)
                
    if pelotaXY.left < 0 or pelotaXY.right > ancho:
        if pelotaXY.left < 0:
            puntosJugador2 += 1
            
            if puntosJugador2 == 1 and ganador == False:
                print("Ganador Jugador 2")
                textoGanador = tipoletra.render("Jugador 2 es el Ganador", 0, colorGanador)
                ganador = True
                
        if pelotaXY.right > ancho:
            puntosJugador1 += 1
            
            if puntosJugador1 == 1 and ganador == False:
                print("Ganador Jugador 1")
                textoGanador = tipoletra.render("Jugador 1 es el Ganador", 0, colorGanador)
                ganador = True
                
        textoJugador1 = tipoletra.render("Jugador 1: " + str(puntosJugador1), 0, colortextoJugador)
        textoJugador2 = tipoletra.render("Jugador 2: " + str(puntosJugador2), 0, colortextoJugador)
        velocidad_pelota[0] = -velocidad_pelota[0]
    
    if pelotaXY.top < 0 or pelotaXY.bottom > alto:
        velocidad_pelota[1] = -velocidad_pelota[1]

    if ganador:
        ventana.fill(blanco)
        ventana.blit(textoGanador, (150, 200))
        pygame.display.update()
        pygame.display.flip()
    else:        
        ventana.fill(blanco)
        ventana.blit(pelota, pelotaXY)
        ventana.blit(textoJugador1, (20, 20))
        ventana.blit(textoJugador2, ((ancho/2)+20, 20))
        ventana.blit(textoGanador, (150, 200))
        ventana.blit(jugador1, jugador1XY)
        ventana.blit(jugador2, jugador2XY)
        pygame.display.update()
        pygame.display.flip()

pygame.quit()