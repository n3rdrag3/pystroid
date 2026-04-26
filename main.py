import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: 1280")
    print(f"Screen height: 720")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # delta time clock
    game_clock = pygame.time.Clock()
    dt = 0.0

    # groups
    updatable = pygame.sprite.Group()
    drawable  = pygame.sprite.Group()

    # add all Player class instances before instantiation
    Player.containers = (updatable, drawable)

    # spawn player object in middle of screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # main game loop
    while True:
        log_state()
        screen.fill("black")

        for u in updatable: # loop over each item in group and update individually
            u.update(dt)
        for d in drawable: # loop over each item in group and re-render the player each frame
            d.draw(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # user closes window
                return
        pygame.display.flip() # keeps window active by alerting OS
        gs_delta = game_clock.tick(60) # pause the game loop until 1/60th of a second has passed
        dt = gs_delta / 1000 # gs_delta - amount of time passed since last time .tick() was called (delta time)


if __name__ == "__main__":
    main()
