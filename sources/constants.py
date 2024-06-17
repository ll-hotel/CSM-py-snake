from pygame import (
    mixer,
    Surface, Rect,
    font
)
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    KEYDOWN,
    K_ESCAPE,
    QUIT
)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)
RED = (255, 0, 0)

#taille de l'écran
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

PLAYER_WIDTH = 25
PLAYER_HEIGHT = 25

SCREEN_WIDTH -= SCREEN_WIDTH % PLAYER_WIDTH
SCREEN_HEIGHT -= SCREEN_HEIGHT % PLAYER_HEIGHT

MAX_X:int = int(SCREEN_WIDTH / PLAYER_WIDTH) - 1
MAX_Y:int = int(SCREEN_HEIGHT / PLAYER_HEIGHT) - 1

SCORE_INCREMENT = 1

APPLE_PICTURE = "Pomme.png"

BODY_SURFACE = Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
BODY_SURFACE.fill(GREEN)



mixer.init(44100, 32, 2)
__MUSICS = ["pipi.wav", "FuckMachine.wav","SourisDeMetal.wav","Servidor.wav"]
MUSICS = list(map(lambda name: mixer.Sound(file = "./musics/" + name), __MUSICS))

OOF = mixer.Sound(file = "musics/oof.wav")

font.init()
FONT = font.Font(None, 36)


#60000000000000000000
CLOCK_TICK = 10

LEFT = 0
RIGHT = 2
UP = 1
DOWN = 3 
