from constants import SHOT_RADIUS
import pygame
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = pygame.Vector2(0, 0)

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            "green",
            (round(self.position.x), round(self.position.y)),
            self.radius,
        )

    def update(self, dt):
        self.position += self.velocity * dt