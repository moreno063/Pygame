import pygame 
import constantes
import math

class Personaje():
    def __init__(self, x, y, animaciones, energia, tipo):
        self.score = 0              #Para las monedas
        self.object = 0
        self.energia = energia
        self.vivo = True
        self.flip = False
        self.animaciones = animaciones
        #imagen que se muestra en pantalla actualmente
        self.frame_index = 0
        self.image = animaciones[self.frame_index]
        self.update_time = pygame.time.get_ticks() #aqui se almacena la HORA ACTUAL en milisegundos desde que se inicio 'pygame'
        self.shape = self.image.get_rect()
        self.shape.center = (x, y)
        self.tipo = tipo
        self.ultimo_golpe = pygame.time.get_ticks()
        self.golpe = False

    def enemigos(self, jugador, posicion_pantalla, obstaculos_tiles):
        clipped_line = ()
        ene_dx = 0                            #Delta x
        ene_dy = 0

        #Reposicion de enemigos en base a la camar o pantalla
        self.shape.x += posicion_pantalla[0]
        self.shape.y += posicion_pantalla[1]

        #Crear una linea de vision 
        linea_de_vision = ((self.shape.centerx, self.shape.centery ), (jugador.shape.centerx, jugador.shape.centery))

        #Chequear si hay obstaculos en la linea de vision
        for obs in obstaculos_tiles:
            if obs[1].clipline(linea_de_vision):            #Si hay colision
                clipped_line = obs[1].clipline(linea_de_vision) #entonces se guardan las coordenadas en esta variable

        #Distancia entre el jugador y el enemigo
        distancia = math.sqrt(((self.shape.centerx - jugador.shape.centerx)**2)+((self.shape.centery - jugador.shape.centery)**2))
        if not clipped_line and distancia < constantes.RANGO:
            if self.shape.centerx > jugador.shape.centerx:   #Si el enemigo esta a la derecha del jugador, el enemigo se movera a 2
                ene_dx = -constantes.VELOCIDAD_ENEMIGO
            if self.shape.centerx < jugador.shape.centerx:  
                ene_dx = constantes.VELOCIDAD_ENEMIGO
            if self.shape.centery > jugador.shape.centery:   
                ene_dy = -constantes.VELOCIDAD_ENEMIGO
            if self.shape.centery < jugador.shape.centery:   
                ene_dy = constantes.VELOCIDAD_ENEMIGO

        self.movimiento(ene_dx, ene_dy, obstaculos_tiles)

        #Atacar al jugador 
        if distancia < constantes.RANGO_ATAQUE and jugador.golpe == False:
            jugador.energia -= 5
            jugador.golpe = True
            jugador.ultimo_golpe = pygame.time.get_ticks()

    def update(self):
        #Comprobar si el personaje ha muerto 
        if self.energia <= 0:
            self.energia = 0
            self.vivo = False

        #Tiempo para volver a recibir daño
        cooldown_golpe = 1000
        if self.tipo == 1:
            if self.golpe == True:
                if pygame.time.get_ticks() - self.ultimo_golpe >cooldown_golpe:
                    self.golpe = False


        cooldown_animacion = 100   #Cuanto tiempo quiero que se mantenga una imagen en milisegundos
        self.image = self.animaciones[self.frame_index]
        if pygame.time.get_ticks() - self.update_time >= cooldown_animacion:    #HORA ACTUAL - HORA ACTUAL
            self.frame_index = self.frame_index + 1 
            self.update_time = pygame.time.get_ticks()    #Cada 100 milisegundos se actualizara la imagen
        if self.frame_index >= len(self.animaciones):
            self.frame_index=0

    def movimiento (self, delta_x, delta_y, obstaculos_tiles):
        posicion_pantalla = [0, 0]
        if delta_x < 0:
            self.flip = True
        if delta_x > 0:
            self.flip = False 
        
        self.shape.x = self.shape.x + delta_x
        for obstaculo in obstaculos_tiles:
            if obstaculo[1].colliderect(self.shape):
                if delta_x > 0:
                    self.shape.right = obstaculo[1].left
                elif delta_x < 0:
                    self.shape.left = obstaculo[1].right
                

        self.shape.y = self.shape.y + delta_y        #positivo hacia abajo, negativo hacia arriba
        for obstaculo in obstaculos_tiles:
            if obstaculo[1].colliderect(self.shape):
                if delta_y > 0:
                    self.shape.bottom = obstaculo[1].top
                elif delta_y < 0:
                    self.shape.top = obstaculo[1].bottom

        #Logica que solo aplicara para el jugador (tipo 1)
        if self.tipo == 1: 
            #Actualizar la pantalla basado en la posicion del jugador 
            #Mover la camara izquierda o derecha 
            if self.shape.right > (constantes.ANCHO_VENTANA - constantes.LIMITE_PANTALLA):
                posicion_pantalla[0] = (constantes.ANCHO_VENTANA - constantes.LIMITE_PANTALLA) - self.shape.right
                self.shape.right = constantes.ANCHO_VENTANA - constantes.LIMITE_PANTALLA
            if self.shape.left < constantes.LIMITE_PANTALLA:
                posicion_pantalla[0] = constantes.LIMITE_PANTALLA - self.shape.left
                self.shape.left = constantes.LIMITE_PANTALLA
            #Mover arriba o abajo
            if self.shape.top < constantes.LIMITE_PANTALLA:
                posicion_pantalla[1] = constantes.LIMITE_PANTALLA - self.shape.top
                self.shape.top = constantes.LIMITE_PANTALLA
            if self.shape.bottom > (constantes.ALTO_VENTANA - constantes.LIMITE_PANTALLA):
                posicion_pantalla[1] = (constantes.ALTO_VENTANA - constantes.LIMITE_PANTALLA) - self.shape.bottom
                self.shape.bottom = constantes.ALTO_VENTANA - constantes.LIMITE_PANTALLA
            return posicion_pantalla

    def dibujar (self, screen):
        image_flip = pygame.transform.flip(self.image, self.flip, False)
        screen.blit(image_flip, self.shape)
        #pygame.draw.rect(screen, constantes.COLOR_PERSONAJE, rect=self.shape, width=1) ##Encapsula el personaje en un rectangulo o cuadrado
    
    
    