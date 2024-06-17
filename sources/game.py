from sources.constants import (
        Surface,
        SCREEN_WIDTH, SCREEN_HEIGHT,
        BODY_SURFACE,
        FONT, GREEN, BLACK,
        SCORE_INCREMENT,
        OOF
    )
from pygame.time import Clock
from pygame.display import set_mode
from sources.player import Player
from sources.apple import Pomme

class Game:

    screen: Surface
    player: Player
    apple:  Pomme
    clock:  Clock
    score:  int

    def __init__(self, display) -> None:
        self.display = display
        self.screen = self.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.player = Player()
        self.apple = Pomme()
        self.clock = Clock()
        self.score = 0
    
    def blit_all(self):
        self.screen.fill(BLACK)
        i = self.player.l_body - 1
        while i:
            self.screen.blit(BODY_SURFACE, self.player.body[i])
            i -= 1
        self.screen.blit(self.player.surf, self.player.rect)
        self.screen.blit(self.apple.image, self.apple.rect)
        score_text = FONT.render(f"Score: {self.score}", True, GREEN)
        self.screen.blit(score_text, (10, 10))

    def update(self, pressed_keys):
        self.player.update(pressed_keys)
        if self.player.rect.colliderect(self.apple.rect):
            OOF.play()
            self.score += SCORE_INCREMENT
            self.apple.replace()
            self.player.growth()
        
