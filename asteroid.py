from circleshape import CircleShape
import pygame
from constants import LINE_WIDTH, ASTEROID_MAX_RADIUS, ASTEROID_MIN_RADIUS, ASTEROID_KINDS
import random
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(0, 0)

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            "white",
            (round(self.position.x), round(self.position.y)),
            self.radius,
            LINE_WIDTH,
        )

    def split(self):
        self.kill()
        if self.radius > ASTEROID_MIN_RADIUS:
            log_event("asteroid_split")
            angle = random.uniform(20, 50)
            first_velocity = self.velocity.rotate(angle)
            second_velocity = self.velocity.rotate(-angle)

            new_radius = self.radius - ASTEROID_MIN_RADIUS

            first = Asteroid(self.position.x, self.position.y, new_radius)
            first.velocity = first_velocity * random.uniform(1.2, 1.5)

            second = Asteroid(self.position.x, self.position.y, new_radius)
            second.velocity = second_velocity * random.uniform(1.2, 1.5)

    def update(self, dt):
        self.position += self.velocity * dt