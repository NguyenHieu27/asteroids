import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from game_state import GameState
from ui_renderer import UIRenderer
from input_handler import InputHandler
from game_logic import GameLogic


def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    # Initialize game components
    game_state = GameState(x, y)
    ui_renderer = UIRenderer(screen)
    input_handler = InputHandler()

    while True:
        log_state()
        if input_handler.handle_events(game_state):
            return
        
        if not game_state.game_started:
            ui_renderer.render_splash_screen()
            pygame.display.flip()
            dt = clock.tick(60) / 1000.0
            continue

        if game_state.game_over:
            ui_renderer.render_game_over_screen(game_state)
            pygame.display.flip()
            dt = clock.tick(60) / 1000.0
            continue

        GameLogic.update_timers(game_state, dt)
        GameLogic.spawn_powerups(game_state, dt)
        
        game_state.asteroid_field.level = game_state.level
        game_state.updatable.update(dt)
        GameLogic.check_collisions(game_state)
        screen.fill("black")

        for drawable_object in game_state.drawable:
            drawable_object.draw(screen)
        
        ui_renderer.render_hud(game_state)
        pygame.display.flip()
        dt = clock.tick(60) / 1000.0


if __name__ == "__main__":
    main()
