import pygame
import random

# Inicializar pygame
pygame.init()

# Dimensiones de la ventana
width = 800
height = 600

# Colores
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Crear la ventana del juego
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Juego de Pelea")

# Clase Jugador
class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(red)
        self.rect = self.image.get_rect()
        self.rect.center = (width // 2, height // 2)
        self.speed = 5

    def update(self):
        # Obtener las teclas presionadas
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

# Clase Oponente
class Oponente(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(black)
        self.rect = self.image.get_rect()
        self.rect.center = (width // 2 + 100, height // 2)
        self.speed = 3

    def update(self):
        # Movimiento aleatorio del oponente
        self.rect.x += random.randint(-self.speed, self.speed)
        self.rect.y += random.randint(-self.speed, self.speed)

# Grupos de sprites
jugadores = pygame.sprite.Group()
oponentes = pygame.sprite.Group()

# Crear instancias de jugador y oponente
jugador = Jugador()
oponente = Oponente()

# Agregar jugadores y oponentes a los grupos de sprites
jugadores.add(jugador)
oponentes.add(oponente)

# Reloj para controlar la velocidad de actualización de la ventana
clock = pygame.time.Clock()

# Bucle principal del juego
running = True
while running:
    # Actualizar sprites
    jugadores.update()
    oponentes.update()

    # Comprobar colisiones entre el jugador y el oponente
    if pygame.sprite.spritecollide(jugador, oponentes, False):
        print("¡Golpe recibido!")

    # Limpiar ventana
    window.fill(white)

    # Dibujar sprites en la ventana
    jugadores.draw(window)
    oponentes.draw(window)

    # Actualizar ventana
    pygame.display.flip()

    # Controlar eventos del teclado y ventana
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Controlar la velocidad de actualización de la ventana
    clock.tick(60)

# Cerrar pygame
pygame.quit()
