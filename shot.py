import pygame
from circleshape import *
from constants import *
from player import *


class Shot(CircleShape):
    def __init__(self, x, y, radius, velocity):
        super().__init__(x, y, radius)
        self.velocity = velocity

    def draw(self, surface):
        pygame.draw.circle(surface, (100, 100, 100), (self.position.x, self.position.y), self.radius, width = 2)

    def update(self, dt):
        self.position.x = (self.velocity.x * dt) + self.position.x
        self.position.y = (self.velocity.y * dt) + self.position.y