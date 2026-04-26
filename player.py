import pygame
from constants import *
from circleshape import CircleShape
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)
    
    def rotate(self, dt):
        self.rotation += (PLAYER_TURN_SPEED * dt)

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move((dt * -1))
        if keys[pygame.K_a]:
            self.rotate((dt * -1))
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
    
    def move(self, dt):
        # start with unit vector pointing straight down from (0, 0) to (0, 1)
        unit_vector = pygame.Vector2(0, 1)
        # rotate the vector by the player location so it's pointing same direction as player
        # rotate() returns a NEW vector - it doesn't modify the original so it's assigned to rotated_vector
        rotated_vector = unit_vector.rotate(self.rotation)
        # multiply vector by PS * dt so vector is length player should move during the frame
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        # add the vector to the player position to move them
        self.position += rotated_with_speed_vector

    def shoot(self):
        shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        shot.velocity = pygame.Vector2(0,1)
        rotated_shot = shot.velocity.rotate(self.rotation)
        rotated_shot *= PLAYER_SHOOT_SPEED
        shot.velocity = rotated_shot