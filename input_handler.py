import pygame


class InputHandler:
    @staticmethod
    def handle_events(game_state):
        """Handle all input events and return True if game should quit"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
                
            if not game_state.game_started and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_state.game_started = True
                    
            elif game_state.game_over and event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_r, pygame.K_RETURN, pygame.K_SPACE):
                    game_state.restart_game()
                elif event.key == pygame.K_ESCAPE:
                    game_state.restart_to_menu()
        
        return False
