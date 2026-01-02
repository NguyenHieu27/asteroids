import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH, POWERUP_RADIUS


class Shield(CircleShape):
    def __init__(self, x, y, radius=POWERUP_RADIUS):
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(0, 0)

    def draw(self, screen):
        points = []
        # Build a hexagon around the center
        for i in range(6):
            angle = 60 * i
            offset = pygame.Vector2(0, 1).rotate(angle) * self.radius
            points.append(self.position + offset)
        pygame.draw.polygon(
            screen,
            "blue",
            [(round(p.x), round(p.y)) for p in points],
            width=LINE_WIDTH,
        )

    def update(self, dt):
        self.position += self.velocity * dt
