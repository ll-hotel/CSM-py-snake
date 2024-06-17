from random import randint
from sources.constants import (
    MUSICS,
    CLOCK_TICK,
    QUIT, K_ESCAPE,
)
from pygame import (
    display,
    event,
    key,
    mixer
)
from sources.game import Game

def gameloop():
    game = Game(display)
    while True:
        if (not mixer.get_busy()):
            MUSICS[randint(0, MUSICS.__len__() - 1)].play()
        # Event handling
        for e in event.get():
            if e.type == QUIT:
                return
        # Check for escape
        pressed_keys = key.get_pressed()
        if (pressed_keys[K_ESCAPE]):
            return
        # Update
        game.update(pressed_keys)
        # End game if player died
        if not game.player.alive:
            return
        # Display game screen
        game.blit_all()
        game.display.flip()
        # Ticks
        game.clock.tick(CLOCK_TICK)

