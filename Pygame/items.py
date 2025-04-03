import pygame.sprite
import constantes
import personaje

class item(pygame.sprite.Sprite):
    def __init__(self, x, y, item_type, animacion_list):
        pygame.sprite.Sprite.__init__(self)
        self.item_type = item_type  #0 = coins, 1 = potion
        self.animacion_list = animacion_list
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        self.image = self.animacion_list[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
    
    def update(self, posicion_pantalla, personaje):
        #Reposicionar items en base a el lugar de la camara o pantalla
        self.rect.x += posicion_pantalla[0]
        self.rect.y += posicion_pantalla[1]    #Estos dos serian cero ya que en Variables, [0, 0]

        #Comprobar colision entre personaje y los items
        if self.rect.colliderect(personaje.shape):
            #comprobar si son monedas
            if self.item_type == 0:
                personaje.score += 1
            #pociones
            elif self.item_type == 1:
                personaje.energia += 20
                if personaje.energia > 100:
                    personaje.energia = 100
            #Objetos clave
            elif self.item_type == 2 or self.item_type == 3 or self.item_type == 4 or self.item_type == 5:
                personaje.object += 1
                personaje.score += 2
    
            self.kill()

        cooldown_animacion = 40            #1000 seria un segundo
        self.image = self.animacion_list[self.frame_index]

        if pygame.time.get_ticks() - self.update_time > cooldown_animacion:
            self.frame_index += 1
            self.update_time = pygame.time.get_ticks()
        if self.frame_index >= len(self.animacion_list):
            self.frame_index = 0