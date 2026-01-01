import pygame
from constants import SCREEN_WIDTH
from constants import SCREEN_HEIGHT
from logger import log_state

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return

    print("Starting Asteroids with pygame version: ", pygame.version.ver)
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    while True:
        log_state()
        screen.fill("black")
        pygame.display.flip()

if __name__ == "__main__":
    main()
