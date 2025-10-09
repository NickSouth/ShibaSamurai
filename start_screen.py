import pygame
import sys

WHITE = (255, 255, 255)
BLACK = [0, 0, 0]
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
button_color = [50, 50, 50]

fresh_start = True
start_count = 0

pygame.init()
pygame.font.init()

bg_img = pygame.image.load("Sprites/SamuraiShibaTitleScreen.png")

screen = pygame.display.set_mode((1400, 800))
clock = pygame.time.Clock()

intro_font = pygame.font.SysFont("Ariel", 20)
startup_text = intro_font.render("In loving memory of Rocky...", True, (255, 255, 255))
start_font = pygame.font.SysFont("Ariel", 100)
start_text = start_font.render("START GAME", True, (200, 200, 200))

start_rect = pygame.Rect(800, 600, 500, 100)

while True:
    if fresh_start:
        start_count += 1
        if start_count == 300:
            fresh_start = False
        screen.fill(BLACK)
        BLACK[0] += .3
        screen.blit(startup_text, (600, 400))

    else:

        screen.fill(WHITE)
        screen.blit(bg_img, (0, 0))
        pygame.draw.rect(screen, button_color, (800, 600, 500, 100))
        screen.blit(start_text, (825, 620))

    # Quitting pygame if needed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Handle mouse click on start button
            mouse_pos = event.pos
            if start_rect.collidepoint(mouse_pos):
                button_color[1] += 50
                # Start game
                print("Loading...")
                break

    clock.tick(60)

    pygame.display.update()
