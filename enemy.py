"""This is the enemy class for the game. This is going to control the player's movement, health, abilities, attacks,
cooldowns, and anything else pertaining to the player. This class will then be called into the main game for use."""

# Importing modules
import pygame
import sys
import math

# Initializing pygame
pygame.init()

# Setting size of display (this will likely be removed after player class has been made)
screen = pygame.display.set_mode((800, 600))
# Setting clock to tick
clock = pygame.time.Clock()


class NinjaCatEnemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def main(self):
        pygame.draw.rect(screen, (255, 0, 0), (self.x-screen_scroll[0], self.y-screen_scroll[1], 32, 32))
        if self.x-screen_scroll[0] > player.x:
            self.x -= 4
        elif self.x-screen_scroll[0] < player.x:
            self.x += 4
        if self.y - screen_scroll[1] > player.y:
            self.y -= 4
        elif self.y - screen_scroll[1] < player.y:
            self.y += 4


# Handling movement
screen_scroll = [0, 0]

# Main game loop. This is mostly to be used to test things as the enemy classes is made and will not remain here
while True:
    screen.fill((255, 255, 255))

    # Quitting pygame if needed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # Capping framerate at 60 fps
    clock.tick(60)
    # Updating display
    pygame.display.update()