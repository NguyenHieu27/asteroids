import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT


class UIRenderer:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 32)
        self.title_font = pygame.font.Font(None, 72)
        self.instruction_font = pygame.font.Font(None, 40)
        self.controls_font = pygame.font.Font(None, 28)

    def render_splash_screen(self):
        """Render the splash/title screen"""
        self.screen.fill("black")
        
        title = self.title_font.render("ASTEROIDS", True, "white")
        title_rect = title.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3))
        self.screen.blit(title, title_rect)

        instruction = self.instruction_font.render(
            "Press SPACE to Start", True, "yellow"
        )
        instruction_rect = instruction.get_rect(
            center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 80)
        )
        self.screen.blit(instruction, instruction_rect)

        controls = [
            "A/D - Rotate",
            "W/S - Move",
            "SPACE - Shoot",
        ]
        for i, control in enumerate(controls):
            control_text = self.controls_font.render(control, True, "cyan")
            control_rect = control_text.get_rect(
                center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 140 + i * 30)
            )
            self.screen.blit(control_text, control_rect)

    def render_game_over_screen(self, game_state):
        """Render the game over screen"""
        self.screen.fill("black")
        
        for drawable_object in game_state.drawable:
            drawable_object.draw(self.screen)

        game_over_text = self.font.render(
            f"Game Over! Score: {game_state.score}", True, "yellow"
        )
        restart_text = self.font.render("Press SPACE to Restart", True, "green")
        exit_text = self.font.render("Press ESC to Exit", True, "red")
        
        game_over_rect = game_over_text.get_rect(
            center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        )
        self.screen.blit(game_over_text, game_over_rect)

        restart_rect = restart_text.get_rect(
            center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 40)
        )
        self.screen.blit(restart_text, restart_rect)

        exit_rect = exit_text.get_rect(
            center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 80)
        )
        self.screen.blit(exit_text, exit_rect)
        
        scoreboard = self.font.render(
            f"Score: {game_state.score}   |   Lives: {game_state.lives}", True, "white"
        )
        scoreboard_rect = scoreboard.get_rect()
        scoreboard_rect.midtop = (SCREEN_WIDTH / 2, 10)
        self.screen.blit(scoreboard, scoreboard_rect)

    def render_hud(self, game_state):
        """Render the HUD during gameplay"""
        scoreboard = self.font.render(
            f"Level: {game_state.level}   |   Score: {game_state.score}   |   Lives: {game_state.lives}",
            True,
            "white",
        )
        scoreboard_rect = scoreboard.get_rect()
        scoreboard_rect.midtop = (SCREEN_WIDTH / 2, 10)
        self.screen.blit(scoreboard, scoreboard_rect)

        # Render power-ups with colored text
        if game_state.player.shield_hits > 0 or game_state.player.cannon_active:
            powerup_y = scoreboard_rect.bottom + 4
            total_width = 0
            powerup_surfaces = []

            if game_state.player.shield_hits > 0:
                shield_surface = self.font.render(
                    f"[ +Shield: {game_state.player.shield_hits} ]", True, "blue"
                )
                powerup_surfaces.append(shield_surface)
                total_width += shield_surface.get_width()

            if game_state.player.cannon_active:
                cannon_surface = self.font.render(
                    f"[ +Cannon: {game_state.player.cannon_timer:.1f}s ]", True, "green"
                )
                powerup_surfaces.append(cannon_surface)
                total_width += cannon_surface.get_width()

            if powerup_surfaces:
                total_width += (len(powerup_surfaces) - 1) * 10  # spacing
                current_x = SCREEN_WIDTH / 2 - total_width / 2
                for surface in powerup_surfaces:
                    self.screen.blit(surface, (current_x, powerup_y))
                    current_x += surface.get_width() + 10
