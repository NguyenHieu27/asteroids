import random
import pygame
from constants import (
    RESPAWN_INVULNERABLE_SECONDS,
    SCORE_PER_ASTEROID,
    LEVEL_BASE_SCORE,
    POWERUP_SPAWN_RATE_SECONDS,
    POWERUP_MIN_SPEED,
    POWERUP_MAX_SPEED,
    SHIELD_HITS,
    CANNON_DURATION_SECONDS,
)
from logger import log_event
from asteroidfield import AsteroidField
from shield import Shield
from cannon import Cannon


class GameLogic:
    @staticmethod
    def update_timers(game_state, dt):
        """Update all game timers"""
        if game_state.invulnerable_timer > 0:
            game_state.invulnerable_timer = max(0.0, game_state.invulnerable_timer - dt)
            game_state.player.invulnerable = True
            game_state.player.invulnerable_timer = game_state.invulnerable_timer
        else:
            game_state.player.invulnerable = False
            game_state.player.invulnerable_timer = 0.0

        if game_state.player.cannon_active:
            game_state.player.cannon_timer = max(0.0, game_state.player.cannon_timer - dt)
            if game_state.player.cannon_timer <= 0:
                game_state.player.cannon_active = False
                game_state.player.cannon_timer = 0.0

    @staticmethod
    def spawn_powerups(game_state, dt):
        """Handle power-up spawning logic"""
        game_state.powerup_spawn_timer += dt
        
        # Spawn Shield if not already on screen
        game_state.shield_spawn_timer += dt
        has_shield = any(isinstance(p, Shield) for p in game_state.powerups)
        if game_state.shield_spawn_timer > POWERUP_SPAWN_RATE_SECONDS and not has_shield:
            game_state.shield_spawn_timer = 0.0
            edge = random.choice(AsteroidField.edges)
            speed = random.randint(POWERUP_MIN_SPEED, POWERUP_MAX_SPEED)
            velocity = edge[0] * speed
            velocity = velocity.rotate(random.randint(-30, 30))
            position = edge[1](random.uniform(0, 1))
            powerup = Shield(position.x, position.y)
            powerup.velocity = velocity
        
        # Spawn Cannon if not already on screen
        game_state.cannon_spawn_timer += dt
        has_cannon = any(isinstance(p, Cannon) for p in game_state.powerups)
        if game_state.cannon_spawn_timer > POWERUP_SPAWN_RATE_SECONDS and not has_cannon:
            game_state.cannon_spawn_timer = 0.0
            edge = random.choice(AsteroidField.edges)
            speed = random.randint(POWERUP_MIN_SPEED, POWERUP_MAX_SPEED)
            velocity = edge[0] * speed
            velocity = velocity.rotate(random.randint(-30, 30))
            position = edge[1](random.uniform(0, 1))
            powerup = Cannon(position.x, position.y)
            powerup.velocity = velocity

    @staticmethod
    def check_collisions(game_state):
        """Handle all collision detection and responses"""
        # Player-asteroid collisions
        for asteroid in game_state.asteroids:
            if game_state.invulnerable_timer == 0 and game_state.player.collide_circle(asteroid):
                if game_state.player.shield_hits > 0:
                    game_state.player.shield_hits -= 1
                    log_event("shield_block")
                    asteroid.kill()
                else:
                    log_event("player_hit")
                    game_state.lives -= 1
                    game_state.player.position.update(game_state.x, game_state.y)
                    game_state.player.velocity.update(0, 0)
                    game_state.player.rotation = 0
                    game_state.invulnerable_timer = RESPAWN_INVULNERABLE_SECONDS
                    if game_state.lives <= 0:
                        log_event("game_over")
                        game_state.game_over = True
                break

        # Shot-asteroid collisions
        for shot in game_state.shots:
            for asteroid in game_state.asteroids:
                if shot.collide_circle(asteroid):
                    log_event("asteroid_hit")
                    shot.kill()
                    asteroid.split()
                    game_state.score += SCORE_PER_ASTEROID
                    
                    # Check if level up
                    next_threshold = LEVEL_BASE_SCORE * game_state.level * (game_state.level + 1) // 2
                    if game_state.score >= next_threshold:
                        game_state.level += 1
                        game_state.score_threshold = next_threshold
                        log_event("level_up", level=game_state.level)
                    break

        # Player-powerup collisions
        for powerup in game_state.powerups:
            if game_state.player.collide_circle(powerup):
                if isinstance(powerup, Shield):
                    game_state.player.shield_hits = SHIELD_HITS
                    log_event("powerup_shield")
                elif isinstance(powerup, Cannon):
                    game_state.player.cannon_active = True
                    game_state.player.cannon_timer = CANNON_DURATION_SECONDS
                    log_event("powerup_cannon")
                powerup.kill()
