import pygame
import personaje
import math
import constantes
import random



class Weapon():
    def __init__(self, image, image_bullet):
        self.image_bullet = image_bullet
        self.imagen_original = image
        self.angulo = 0
        self.image = pygame.transform.rotate(self.imagen_original, self.angulo)
        self.shape = self.image.get_rect()
        self.dispara = False 
        self.ultimo_disparo = pygame.time.get_ticks()
    
    def  update (self, personaje):
        disparo_cooldow = constantes.COOLDOWN_BALA
        bala = None 
        self.shape.center = personaje.shape.center
        if personaje.flip == False:
            self.shape.x += personaje.shape.width/2
            self.rotar_arma(False)
        else:
           self.shape.x -= personaje.shape.width/2
           self.rotar_arma(True)
        
        #Mover la pistola con el mouse
        mouse_pos = pygame.mouse.get_pos()
        distancia_x = mouse_pos[0] - self.shape.centerx     #El eje x es el elemento CERO
        distancia_y = -(mouse_pos[1] - self.shape.centery)
        self.angulo = math.degrees(math.atan2(distancia_y, distancia_x))   

        #Detectar los click del mouse
        if pygame.mouse.get_pressed()[0] and self.dispara == False and (pygame.time.get_ticks()- self.ultimo_disparo >= disparo_cooldow):  #El cero es el izquierdo, el 1 la rueda y el 2 el derecho
            bala = Bullet(self.image_bullet, self.shape.centerx, self.shape.centery, self.angulo)
            self.dispara = True
            self.ultimo_disparo = pygame.time.get_ticks()
        #Resetear el click del mouse 
        if pygame.mouse.get_pressed()[0] == False:
            self.dispara = False 
        return bala

    def rotar_arma(self, rotar):
        if rotar == True:
            image_flip = pygame.transform.flip(self.imagen_original, True, False)
            self.image = pygame.transform.rotate(image_flip, self.angulo)
        else:
            image_flip = pygame.transform.flip(self.imagen_original, False, False)
            self.image = pygame.transform.rotate(image_flip, self.angulo)

    def dibujar (self, interfaz):
        self.image = pygame.transform.rotate(self.image, self.angulo)
        interfaz.blit(self.image, self.shape)
        #pygame.draw.rect(interfaz, constantes.COLOR_ARMA, rect=self.shape, width=1)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, image, x, y, angle):
        pygame.sprite.Sprite.__init__(self)
        self.image_original = image 
        self.angulo = angle
        self.image = pygame.transform.rotate(self.image_original, self.angulo)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        #Calculo de la velocidad de la bala 
        self.delta_x = math.cos(math.radians(self.angulo)) * constantes.VELOCIDAD_BALA
        self.delta_y = -math.sin(math.radians(self.angulo)) * constantes.VELOCIDAD_BALA
    
    def update(self, lista_enemigos, obstaculos_tiles):
        daño = 0
        pos_daño = None
        self.rect.x += self.delta_x
        self.rect.y += self.delta_y

        #Ver si las balas salieron de pantalla 
        if self.rect.right < 0 or self.rect.left > constantes.ANCHO_VENTANA or self.rect.bottom < 0 or self.rect.top > constantes.ALTO_VENTANA:
            self.kill()

        #Verificar si hay colision con enemigos
        for enemigo in lista_enemigos:
            if enemigo.shape.colliderect(self.rect):
                daño = 15 + random.randint(-7, 7)
                pos_daño = enemigo.shape
                enemigo.energia -= daño
                self.kill()
                break
        
        #Verificar si hay colision con obstaculos
        for obs in obstaculos_tiles:
            if obs[1].colliderect(self.rect):
                self.kill()
                break

        return daño, pos_daño


    def dibujar(self, interfaz):
        interfaz.blit(self.image, (self.rect.centerx, self.rect.centery-int(self.image.get_height()/2)))