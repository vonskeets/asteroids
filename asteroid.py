import pygame
from circleshape import *
from constants import *
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, surface):
        pygame.draw.circle(surface, (100, 100, 100), (self.position.x, self.position.y), self.radius, width = 2)

    def update(self, dt):
        self.position.x = (self.velocity.x * dt) + self.position.x
        self.position.y = (self.velocity.y * dt) + self.position.y

    def split(self):
        pygame.sprite.Sprite.kill(self)
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            new_vel_1 = self.velocity.rotate(random_angle)
            new_vel_2 = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid_1.velocity = new_vel_1 * 1.2
            new_asteroid_2.velocity = new_vel_2 * 1.2
