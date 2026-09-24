import pygame
import SpriteScript


pygame.init()
screen = pygame.display.set_mode((920, 720))
bg_color = (0, 0, 0)
pygame.display.set_caption('chess')
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()



    screen.fill(bg_color)
    clock.tick(60)
