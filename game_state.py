import pygame
from constants import PLAYER_LIVES, LEVEL_BASE_SCORE
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from shield import Shield
from cannon import Cannon


class GameState:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.reset()

    def reset(self):
        """Reset all game state variables"""
        self.score = 0
        self.level = 1
        self.lives = PLAYER_LIVES
        self.invulnerable_timer = 0.0
        self.game_over = False
        self.powerup_spawn_timer = 0.0
        self.shield_spawn_timer = 0.0
        self.cannon_spawn_timer = 0.0
        self.game_started = False
        self.score_threshold = LEVEL_BASE_SCORE
        
        # Create sprite groups
        self.updatable = pygame.sprite.Group()
        self.drawable = pygame.sprite.Group()
        self.asteroids = pygame.sprite.Group()
        self.shots = pygame.sprite.Group()
        self.powerups = pygame.sprite.Group()

        # Set up containers
        Player.containers = (self.updatable, self.drawable)
        Asteroid.containers = (self.asteroids, self.updatable, self.drawable)
        AsteroidField.containers = (self.updatable,)
        Shot.containers = (self.shots, self.updatable, self.drawable)
        Shield.containers = (self.powerups, self.updatable, self.drawable)
        Cannon.containers = (self.powerups, self.updatable, self.drawable)

        # Create player and asteroid field
        self.player = Player(self.x, self.y)
        self.asteroid_field = AsteroidField()

    def restart_game(self):
        """Restart the game without going to splash screen"""
        self.reset()
        self.game_started = True

    def restart_to_menu(self):
        """Restart and return to splash screen"""
        self.reset()
