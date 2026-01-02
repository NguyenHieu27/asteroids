import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH, POWERUP_RADIUS


class Cannon(CircleShape):
    def __init__(self, x, y, radius=POWERUP_RADIUS):
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(0, 0)

    def draw(self, screen):
        half = self.radius
        points = [
            self.position + pygame.Vector2(-half, -half),
            self.position + pygame.Vector2(half, -half),
            self.position + pygame.Vector2(half, half),
            self.position + pygame.Vector2(-half, half),
        ]
        pygame.draw.polygon(
            screen,
            "green",
            [(round(p.x), round(p.y)) for p in points],
            width=LINE_WIDTH,
        )

    def update(self, dt):
        self.position += self.velocity * dt
