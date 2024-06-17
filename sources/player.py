from pygame.sprite import Sprite
from sources.constants import (
    Surface, Rect,
    K_UP, K_DOWN, K_LEFT, K_RIGHT,
    SCREEN_WIDTH, SCREEN_HEIGHT,
    PLAYER_WIDTH, PLAYER_HEIGHT,
    MAX_X, MAX_Y,
    WHITE,
    LEFT, RIGHT, UP, DOWN
)

class Player(Sprite):
    view:   int
    body:   list[Rect]
    l_body: int
    alive:  bool
    def __init__(self):
        super(Player, self).__init__()
        self.surf = Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
        self.surf.fill(WHITE)
        self.rect = self.surf.get_rect()
        sw = (SCREEN_WIDTH >> 1)
        sh = (SCREEN_HEIGHT >> 1)
        self.body = [self.rect]
        self.length = 1
        self.rect.move_ip(
            sw - (sw % PLAYER_WIDTH),
            sh - (sh % PLAYER_HEIGHT)
        )
        self.view = LEFT 
        self.body = [self.rect]
        self.l_body = 1
        self.alive = True

    def growth(self):
        self.body.append(Rect(-PLAYER_WIDTH, -PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT))
        self.l_body += 1 

    def move(self):
        i = self.l_body -1
        while i:
            self.body[i].move_ip(
                self.body[i-1].left - self.body[i].left, 
                self.body[i-1].top - self.body[i].top
                )
            i -= 1
        self.rect.move_ip(

            PLAYER_WIDTH * (self.view %2 == 0) * (self.view -1),
            PLAYER_HEIGHT * (self.view %2 == 1) * (self.view -2)
        )

    def check_death_case(self):
        i = 1
        while (i < self.l_body and self.alive):
            self.alive ^= self.rect.colliderect(self.body[i])
            i += 1

    def update(self, pressed_keys):
        self.change_view(pressed_keys)
        if self.rect.left == 0 and self.view == LEFT :
            return
        if self.rect.top == 0 and self.view == UP :
            return
        if self.rect.right == SCREEN_WIDTH and self.view == RIGHT :
            return
        if self.rect.bottom == SCREEN_HEIGHT and self.view == DOWN :
            return
        self.check_death_case()
        if (not self.alive):
            return
        self.move()      

    def change_view(self, pressed_keys):
        if pressed_keys[K_LEFT]:
            self.view = LEFT
        elif pressed_keys[K_RIGHT]:
            self.view = RIGHT
        elif pressed_keys[K_UP]:
            self.view = UP
        elif pressed_keys[K_DOWN]:
            self.view = DOWN
    
