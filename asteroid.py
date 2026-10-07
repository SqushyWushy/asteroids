import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen,"white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        random_angle = random.uniform(20, 50)
        rotated_vector = self.velocity.rotate(random_angle)

        other_angle = -1 * random_angle
        other_rotated_vector = self.velocity.rotate(other_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        split_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        split_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)

        split_asteroid_1.velocity = rotated_vector * 1.2
        split_asteroid_2.velocity = other_rotated_vector * 1.2

