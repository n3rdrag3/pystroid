import pygame
import random
from circleshape import CircleShape
from constants import *
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return # asteroid removed from screen
        else:
            log_event("asteroid_split")
            # generate a random angle between 20 and 50 degrees
            random_angle = random.uniform(20.0, 50.0)
            new_rotation1 = self.velocity.rotate(random_angle)
            # opposite direction of angle
            opposite_random_angle = random_angle * -1
            new_rotation2 = self.velocity.rotate(opposite_random_angle)
            new_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x, self.position.y, new_asteroid_radius)
            asteroid2 = Asteroid(self.position.x, self.position.y, new_asteroid_radius)
            asteroid1.velocity = new_rotation1 * 1.2
            asteroid2.velocity = new_rotation2 * 1.2
