from sources.constants import (
    APPLE_PICTURE,
    MAX_X, MAX_Y,
    PLAYER_WIDTH, PLAYER_HEIGHT,
    SCREEN_WIDTH, SCREEN_HEIGHT
)
from pygame import Surface, image
from pygame.sprite import Sprite
from random import randint

class Pomme(Sprite):

    def __init__(self):
        super(Pomme, self).__init__()
        self.image = Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
        self.image.blit(image.load(APPLE_PICTURE),
            (0, 0), (0, 0, PLAYER_WIDTH, PLAYER_HEIGHT))
        self.rect = self.image.get_rect()
        self.replace()

    def replace(self):
        self.rect.move_ip(
            PLAYER_WIDTH * (randint(0, MAX_X) - int(self.rect.left / PLAYER_WIDTH)),
            PLAYER_WIDTH * (randint(0, MAX_Y) - int(self.rect.top / PLAYER_HEIGHT))
        )

