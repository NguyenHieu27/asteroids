from constants import (
    PLAYER_RADIUS,
    PLAYER_SPEED,
    PLAYER_TURN_SPEED,
    PLAYER_SHOOT_SPEED,
    PLAYER_SHOOT_COOLDOWN_SECONDS,
)
import pygame
from circleshape import CircleShape
from shot import Shot

# Class Player inherits from CircleShape
class Player(CircleShape):
    def __init__(self, x, y, radius=PLAYER_RADIUS):
        super().__init__(x, y, radius)
        self.rotation = 0
        self.cooldown_timer = 0.0  # Timer to manage shooting cooldown
        self.invulnerable = False
        self.invulnerable_timer = 0.0
        self.shield_hits = 0
        self.cannon_active = False
        self.cannon_timer = 0.0
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        blink = False
        if self.invulnerable:
            blink = int(self.invulnerable_timer * 10) % 2 == 0

        if blink:
            color = "yellow"
        elif self.cannon_active:
            color = "green"
        elif self.shield_hits > 0:
            color = "blue"
        else:
            color = "white"
        pygame.draw.polygon(screen, color, self.triangle())
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector

    def shoot(self):
        if not self.cannon_active and self.cooldown_timer > 0.0:
            return
        self.cooldown_timer = 0.0 if self.cannon_active else PLAYER_SHOOT_COOLDOWN_SECONDS

        shot = Shot(self.position.x, self.position.y)
        direction = pygame.Vector2(0, 1).rotate(self.rotation)
        shot.velocity = direction * PLAYER_SHOOT_SPEED
    
    def update(self, dt):
        keys = pygame.key.get_pressed()
        if self.cooldown_timer > 0.0:
            self.cooldown_timer -= dt

        if keys[pygame.K_a]: # Left turn
            self.rotate(-dt)
        if keys[pygame.K_d]: # Right turn
            self.rotate(dt)     
        if keys[pygame.K_w]: # Move forward
            self.move(dt)
        if keys[pygame.K_s]: # Move backward
            self.move(-dt)   
        if keys[pygame.K_SPACE]: # Shoot
            self.shoot()
