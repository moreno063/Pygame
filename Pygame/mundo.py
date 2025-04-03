import pygame 
import constantes
from items import item
from personaje import Personaje

obstaculos = [105, 104, 152, 153, 110, 159, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 127, 132,
               133, 178, 184, 185, 258, 260, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 
               222, 235, 277, 285, 287, 288, 308, 312, 313, 315, 316, 329, 335, 340, 341, 358, 368, 
               369, 371, 379, 385, 390, 391, 393, 408, 410, 411, 412, 414, 415, 417, 419, 420, 
               421, 429, 435, 437, 438, 443, 458, 460, 461, 470, 471, 479, 485, 493, 508, 558, 
               608, 658, 708, 560, 562, 563, 515, 516, 518, 519, 565, 566, 568, 569, 529, 579, 
               629, 679, 729, 660, 661, 662, 663, 664, 665, 666, 667, 668, 669, 670, 673, 674, 808, 
               810, 860, 812, 813, 814, 815, 816, 817, 818, 819, 820, 821, 822, 823, 824, 825, 
               827, 877, 829, 535, 585, 635, 543, 593, 643, 693, 743, 793, 754, 755, 532, 583, 634]

class Mundo():
    def __init__(self):
        self.map_tiles = []
        self.obstaculos_tiles = []
        self.exit_tile = None
        self.lista_item = []
        self.lista_enemigo = []


    def process_data(self, data, tile_list, img_items, animacion_enemigos):
        self.level_length = len(data)
        for y, row in enumerate(data):                #Enumera cada arreglo de tile
            for x, tile in enumerate(row):              #Enumera cada elemento en el arreglo
                image = tile_list[tile]                 #Obtiene la imagen según el número tile
                image_rect = image.get_rect()           # Obtiene su rectángulo delimitador
                image_x = x * constantes.TILE_SIZE
                image_y = y * constantes.TILE_SIZE
                image_rect.center = (image_x, image_y)
                tile_data = [image, image_rect, image_x, image_y]

                #Agregar tiles a obstaculos
                if tile in obstaculos:
                    self.obstaculos_tiles.append(tile_data)


                #Items 
                elif tile == 1404:                
                    moneda = item(image_x, image_y, 0, img_items[0])
                    self.lista_item.append(moneda)
                    tile_data[0] = tile_list [0]
                elif tile == 1400:
                    maquina_escribir = item(image_x, image_y, 2, img_items[2])
                    self.lista_item.append(maquina_escribir)
                    tile_data[0] = tile_list[0]
                elif tile == 1401:
                    abaco = item(image_x, image_y, 5, img_items[5])
                    self.lista_item.append(abaco)
                    tile_data[0] = tile_list[0]
                elif tile == 1403:
                    pluma = item(image_x, image_y, 3, img_items[3])
                    self.lista_item.append(pluma)
                    tile_data[0] = tile_list[0]
                elif tile == 1405:
                    pocion = item(image_x, image_y, 1, img_items[1])
                    self.lista_item.append(pocion)
                    tile_data[0] = tile_list[0]
                elif tile == 1402:
                    microscopio = item(image_x, image_y, 4, img_items[4])
                    self.lista_item.append(microscopio)
                    tile_data[0] = tile_list[0]
                
                #Enemigos
                elif tile == 1406:
                    ninja = Personaje(image_x, image_y, animacion_enemigos[0], 150, 2)
                    self.lista_enemigo.append(ninja)
                    tile_data[0] = tile_list[0]


                self.map_tiles.append(tile_data)
    

    def update(self, posicion_pantalla):
        for tile in self.map_tiles:
            tile[2] += posicion_pantalla[0]
            tile[3] += posicion_pantalla[1]
            tile[1].center = (tile[2], tile[3])
            
    def draw(self, surface):
        for tile in self.map_tiles:
            surface.blit(tile[0], tile[1])      #0 = La imagen del tile(image) y 1 = Rectangulo de la imagen para su posicion (image_rect)
