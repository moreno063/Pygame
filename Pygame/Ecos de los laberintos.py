import pygame
import constantes
from personaje import Personaje
from weapon import Weapon
import os
from textos import DamageText
from items import item
from mundo import Mundo
import csv 

#-------------------------------------------------------------------------------------------------------------------------------------------

#FUNCIONES
# Escalar imagen 
def escalar_imagen(image, scale):
    w = image.get_width()
    h = image.get_height()
    nueva_imagen = pygame.transform.smoothscale(image, (w * scale, h * scale))
    return nueva_imagen

#Contar elementos 
def contar_elementos(carpeta):
    return len(os.listdir(carpeta))   #Cuantos elementos hay en la carpeta

#Listar nombres de elementos
def nombre_carpetas(carpeta):
    return os.listdir(carpeta)     #os.listdir lista los nombres de los elementos/carpetas en la carpeta

#Crear items de energia 
def vida_jugador():
    corazon_medio_dibujado = False
    for i in range(5):
        if jugador.energia >= ((i+1) * 20):            
            screen.blit(corazon_lleno, (5 + i * 50, 5))  #Se multiplica por 50 para que haya una distancia de 50 px entre corazones, ademas se suman 5 l inicio para que el primer corazon no quede pegado al borde de la pantalla
        elif jugador.energia > 0 and jugador.energia % 20 >= 10 and not corazon_medio_dibujado:
            screen.blit(corazon_medio, (5 + i * 50, 5))
            corazon_medio_dibujado = True
        else:
            screen.blit(corazon_vacio, (5 + i * 50, 5))

#Dibujar texto en pantalla
def dibujar_texto(texto, fuente, color, x, y):
    img = fuente.render(texto, True, color)
    screen.blit(img, (x, y))


#Dibujar malla
def dibujar_grid():
    for x in range(50):
        pygame.draw.line(screen, constantes.COLOR_BLANCO, (x*constantes.TILE_SIZE, 0), (x*constantes.TILE_SIZE, constantes.ALTO_VENTANA))
        pygame.draw.line(screen, constantes.COLOR_BLANCO, (0, x*constantes.TILE_SIZE), (constantes.ANCHO_VENTANA, x*constantes.TILE_SIZE))

def resetear_mundo():
    grupo_text_daño.empty()
    grupo_balas.empty()
    grupo_items.empty()
    #Crear lista de tile vacia
    data = []
    for fila in range(constantes.FILAS):
        filas = [36] * constantes.COLUMNAS
        data.append(filas)
    return data

#Pantalla de inicio
def pantalla_inicio():
    screen.fill(constantes.COLOR_MORADO)
    dibujar_texto('ECOS DE LOS LABERINTOS', font_titulo, constantes.COLOR_BLANCO, constantes.ANCHO_VENTANA /2-200, constantes.ALTO_VENTANA/2-200)
    pygame.draw.rect(screen, constantes.COLOR_BOTON, boton_jugar)
    pygame.draw.rect(screen, constantes.COLOR_BOTON, boton_salir)
    screen.blit(texto_boton_jugar, (boton_jugar.x + 50, boton_jugar.y + 10))
    screen.blit(texto_boton_salir, (boton_salir.x + 50, boton_salir.y + 10))
    pygame.display.update()

#-------------------------------------------------------------------------------------------------------------------------------------------

pygame.init()
pygame.mixer.init()

#Creacion de la ventana
screen = pygame.display.set_mode((constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA))
pygame.display.set_caption('Eco de los laberintos')

#Variables
posicion_pantalla = [0, 0]
nivel = 1

#Fuentes
font = pygame.font.Font('assets/fonts/Silver.ttf', constantes.TAMAÑO_FUENTE)
font_game_over = pygame.font.Font('assets/fonts/Silver.ttf', 100)
font_reinicio = pygame.font.Font('assets/fonts/Silver.ttf', 40)
font_inicio = pygame.font.Font('assets/fonts/Silver.ttf', 50)
font_titulo = pygame.font.Font('assets/fonts/Silver.ttf', 60)

game_over_text = font_game_over.render('Game Over', True, constantes.COLOR_BLANCO, None)

texto_boton_reinicio = font_reinicio.render('Reiniciar', True, constantes.COLOR_NEGRO, None)

#Botones de inicio
boton_jugar = pygame.Rect (constantes.ANCHO_VENTANA/2-100, constantes.ALTO_VENTANA / 2 - 50, 170, 50)
boton_salir = pygame.Rect (constantes.ANCHO_VENTANA/2-100, constantes.ALTO_VENTANA / 2 + 50, 170, 50)
texto_boton_jugar = font_inicio.render('Jugar', True, constantes.COLOR_NEGRO, None)
texto_boton_salir = font_inicio.render('Salir', True, constantes.COLOR_NEGRO, None)

#Boton reinicio
boton_reinicio = pygame.Rect(constantes.ANCHO_VENTANA/2-100, constantes.ALTO_VENTANA / 2+100, 200, 50)

#-------------------------------------------------------------------------------------------------------------------------------------------

#Importar imagenes 

    #Energia
corazon_vacio = pygame.image.load('assets/images/items/heart_empty.png').convert_alpha()
corazon_vacio = escalar_imagen(corazon_vacio, constantes.ESCALA_CORAZON)
corazon_medio = pygame.image.load('assets/images/items/heart_half.png').convert_alpha()
corazon_medio = escalar_imagen(corazon_medio, constantes.ESCALA_CORAZON)
corazon_lleno = pygame.image.load('assets/images/items/heart_full.png').convert_alpha()
corazon_lleno = escalar_imagen(corazon_lleno, constantes.ESCALA_CORAZON)

    #Personaje
animaciones = []
for i in range (3):
    img = pygame.image.load(f'assets/images/characters/player/Player_{i}.png')
    img = escalar_imagen(img, constantes.ESCALA_PERSONAJE)
    animaciones.append(img)


    #Enemigos
directorio_enemigos = "assets/images/characters/enemies"
tipo_enemigos = nombre_carpetas(directorio_enemigos)
animaciones_enemigos = []
for en in tipo_enemigos:
    lista_temporal = []
    ruta_temporal = f"assets/images/characters/enemies/{en}"
    numero_de_animaciones = contar_elementos(ruta_temporal)
    for i in range (numero_de_animaciones):
        img_enemigo = pygame.image.load(f"{ruta_temporal}/{en}_{i}.png").convert_alpha()
        img_enemigo = escalar_imagen(img_enemigo, constantes.ESCALA_ENEMIGOS)
        lista_temporal.append(img_enemigo)
    animaciones_enemigos.append(lista_temporal)

    #Arma 
image_pistola = pygame.image.load(f'assets/images/weapons/gun.png').convert_alpha() #Esto por si no se ve el png.
image_pistola = escalar_imagen(image_pistola, constantes.ESCALA_ARMA)

    #Bala
image_bullet = pygame.image.load(f'assets/images/weapons/bullet.png').convert_alpha() #Esto por si no se ve el png.
image_bullet = escalar_imagen(image_bullet, constantes.ESCALA_BALA)

    #Tiles- Mundo
tile_list=[]
for x in range(constantes.TILE_TYPE):
        tile_image = pygame.image.load(f"assets/tiles/images/tile ({x}).png").convert_alpha()
        tile_image = pygame.transform.smoothscale(tile_image, (constantes.TILE_SIZE, constantes.TILE_SIZE))
        tile_list.append(tile_image)

    #Item pocion
potion_image = pygame.image.load('assets/images/items/potion.png').convert_alpha()
potion_image = escalar_imagen(potion_image, constantes.ESCALA_POCION)

    #Item moneda
coin_image = []
ruta_image = 'assets/images/items/coin'
num_coin_image = contar_elementos(ruta_image)
for i in range(num_coin_image):
    img_coin = pygame.image.load(f'assets/images/items/coin/coin_{i}.png')
    img_coin = escalar_imagen(img_coin, constantes.ESCALA_MONEDA)
    coin_image.append(img_coin)
    
    #Item maquina de escribir 
maquina_img = pygame.image.load('assets/images/items/maquina.png').convert_alpha()
maquina_img = escalar_imagen(maquina_img, constantes.ESCALA_MAQUINA)
    
    #Item pluma
pluma_img = pygame.image.load('assets/images/items/pluma.png').convert_alpha()
pluma_img = escalar_imagen(pluma_img, constantes.ESCALA_PLUMA)

    #Item micro
microscopio_img = pygame.image.load('assets/images/items/microscopio.png').convert_alpha()
microscopio_img = escalar_imagen(microscopio_img, constantes.ESCALA_MICROSCOPIO)

    #Item ábaco
abaco_img = pygame.image.load('assets/images/items/abaco.png').convert_alpha()
abaco_img = escalar_imagen(abaco_img, constantes.ESCALA_ABACO)

item_imagenes = [coin_image, [potion_image], [maquina_img], [pluma_img], [microscopio_img], [abaco_img]]         #Como coin es una lista, convertimos las otras dos para que queden del mismo tipo

#-------------------------------------------------------------------------------------------------------------------------------------------
#Fondo


world_data = []

for fila in range (constantes.FILAS):
    filas = [36] * constantes.COLUMNAS
    world_data.append(filas)

#Cargar el archivo con los niveles 
with open('assets/backgrounds/fondo_Capa de patrones 1.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter= ';')
    for x, fila in enumerate(reader):
        for y, columna in enumerate(fila):
            world_data[x][y] = int(columna)

#-------------------------------------------------------------------------------------------------------------------------------------------
world = Mundo()
world.process_data(world_data, tile_list, item_imagenes, animaciones_enemigos)

#-------------------------------------------------------------------------------------------------------------------------------------------

#Crear un jugador de la clase personaje 
jugador = Personaje(x=100, y=748, animaciones = animaciones, energia=100, tipo = 1)

#Crear lista de enemigos 
lista_enemigos = []
for ene in world.lista_enemigo:
    lista_enemigos.append(ene)

#Crear un  arma de la clase weapon
pistola= Weapon(image_pistola, image_bullet)

#Crear un grupo de sprites
grupo_text_daño = pygame.sprite.Group() #Cantidad de daño, este se 'llena' mas abajo actualizando el estado del arma
grupo_balas = pygame.sprite.Group()     #Balas, este se 'llena' mas abajo actualizando el estado del arma
grupo_items = pygame.sprite.Group()     #Monedas

#Añadir items de la data de nivel
for item in world.lista_item:
   grupo_items.add(item)


#-------------------------------------------------------------------------------------------------------------------------------------------

#definir las variables de movimiento del personaje 
mover_arriba = False
mover_abajo = False
mover_izquierda = False
mover_derecha = False

#controlar el frame rate
reloj = pygame.time.Clock()

pygame.mixer.music.load('assets\sounds\cancion.mp3')
pygame.mixer.music.play(-1)

sonido_disparo = pygame.mixer.Sound('assets\sounds\disparo.mp3')


mostrar_inicio = True
run = True 
while run:

    if mostrar_inicio:
        pantalla_inicio()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if boton_jugar.collidepoint(event.pos):
                    mostrar_inicio = False
                if boton_salir.collidepoint(event.pos):
                    run = False
    else:
        #Que vaya a 60 FPS 
        reloj.tick(constantes.FPS)

        if jugador.vivo:

            #Calcular el movimiento
            delta_x = 0
            delta_y = 0 

            if mover_derecha == True:
                delta_x = constantes.VELOCIDAD
            if mover_izquierda == True:
                delta_x = -constantes.VELOCIDAD
            if mover_abajo == True:
                delta_y = constantes.VELOCIDAD
            if mover_arriba == True:
                delta_y = -constantes.VELOCIDAD

            #Mover al jugador
            posicion_pantalla = jugador.movimiento(delta_x, delta_y, world.obstaculos_tiles)
            
            #--------------------------------------------------------------------------------------------------

            #Actualiza el mapa 
            world.update(posicion_pantalla)

            #Actualiza estado del jugador 
            jugador.update()

            #Actualiza estado de los enemigos 
            for en in lista_enemigos:
                en.update()

            #Actualizar el daño
            grupo_text_daño.update(posicion_pantalla)

            #Actualizar items 
            grupo_items.update(posicion_pantalla, jugador)

            #Actualiza el estado del arma
            bala = pistola.update(jugador)
            if bala:
                grupo_balas.add(bala)
                sonido_disparo.play()

            for bala in grupo_balas:
                daño, pos_daño = bala.update(lista_enemigos, world.obstaculos_tiles)
                if daño != 0 :
                    daño_text = DamageText(pos_daño.centerx, pos_daño.centery, '-' + str(daño), font, constantes.COLOR_ROJO)
                    grupo_text_daño.add(daño_text)
            
            #--------------------------------------------------------------------------------------------------
            #Dibujar malla
            dibujar_grid()

            #Dibujar mundo
            screen.fill(constantes.COLOR_FONDO_ESCENARIO)  # Rellena el fondo 
            world.draw(screen)  # Dibujar los tiles

            #Mostrar o dibujar la figura del personaje
            jugador.dibujar(screen)

            #Mostrar figura de los enemigos 
            for en in lista_enemigos:
                if en.energia == 0:
                    lista_enemigos.remove(en)
                if en.energia > 0:
                    en.enemigos(jugador, posicion_pantalla, world.obstaculos_tiles)
                    en.dibujar(screen)
            
            
            #Mostrar textos
            grupo_text_daño.draw(screen)        #Daño
            dibujar_texto(f'Score: {jugador.score}', font, constantes.COLOR_AMARILLO, 700, 20)
            dibujar_texto(f'Nivel: '+ str(nivel), font, constantes.COLOR_BLANCO, constantes.ANCHO_VENTANA / 2, 5)
            dibujar_texto(f'Objetos clave: {jugador.object}', font, constantes.COLOR_AMARILLO, 670, 40 )


            #Mostrar los items 
            grupo_items.draw(screen)

            #Mostrar la figura del arma
            pistola.dibujar(screen)

            #Mostrar las balas 
            for bala in grupo_balas:
                bala.dibujar(screen)
            
            #Mostrar items de energia
            vida_jugador()


        #--------------------------------------------------------------------------------------------------
        #GAME OVER
        if jugador.vivo == False:
            screen.fill(constantes.COLOR_BG)
            text_rect = game_over_text.get_rect(center = (constantes.ANCHO_VENTANA/2, constantes.ALTO_VENTANA/2))
            screen.blit(game_over_text, text_rect)
            pygame.draw.rect(screen, constantes.COLOR_BOTON, boton_reinicio)
            screen.blit(texto_boton_reinicio, (boton_reinicio.x+50, boton_reinicio.y +10))

        #Cerrar el juego
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        #Movimiento del personaje
            if event.type == pygame.KEYDOWN:
                if event.key ==  pygame.K_LEFT:
                    mover_izquierda = True  
                if event.key == pygame.K_RIGHT:
                    mover_derecha = True 
                if event.key ==  pygame.K_UP:
                    mover_arriba = True
                if event.key == pygame.K_DOWN:
                    mover_abajo = True 
        
        #Parar el movimiento del personaje
            if event.type == pygame.KEYUP:
                if event.key ==  pygame.K_LEFT:
                    mover_izquierda = False  
                if event.key == pygame.K_RIGHT:
                    mover_derecha = False
                if event.key ==  pygame.K_UP:
                    mover_arriba = False
                if event.key == pygame.K_DOWN:
                    mover_abajo = False 
        
        #Que el boton de reiniciar funcione
        if event.type == pygame.MOUSEBUTTONDOWN:
            if boton_reinicio.collidepoint(event.pos) and not jugador.vivo:  #Si el boton colisiona con la posicion del mouse
                jugador.vivo = True
                jugador.energia = 100
                jugador.score = 0 
                world_data = resetear_mundo()
                with open('assets/backgrounds/fondo_Capa de patrones 1.csv', newline='') as csvfile:
                    reader = csv.reader(csvfile, delimiter= ';')
                    for x, fila in enumerate(reader):
                        for y, columna in enumerate(fila):
                            world_data[x][y] = int(columna)
                world = Mundo()
                world.process_data(world_data, tile_list, item_imagenes, animaciones_enemigos)
                
                #Crear un jugador de la clase personaje 
                jugador = Personaje(x=100, y=748, animaciones = animaciones, energia=100, tipo = 1)

                #Crear lista de enemigos 
                lista_enemigos = []
                for ene in world.lista_enemigo:
                    lista_enemigos.append(ene)

                #Crear un  arma de la clase weapon
                pistola= Weapon(image_pistola, image_bullet)

                #Crear un grupo de sprites
                grupo_text_daño = pygame.sprite.Group() #Cantidad de daño, este se 'llena' mas abajo actualizando el estado del arma
                grupo_balas = pygame.sprite.Group()     #Balas, este se 'llena' mas abajo actualizando el estado del arma
                grupo_items = pygame.sprite.Group()     #Monedas

                #Añadir items de la data de nivel
                for item in world.lista_item:
                    grupo_items.add(item)

                


        pygame.display.update()

pygame.quit()

