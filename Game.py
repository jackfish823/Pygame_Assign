import pygame

# Const
WINDOW_WIDTH = 960
WINDOW_HEIGHT = 540
BACKGROUND_COLOR = (255,208,210)
IMAGE = 'background1.jpg'

# Init screen
pygame.init()
size = (WINDOW_WIDTH, WINDOW_HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Game")

# Fill screen and show
img = pygame.image.load(IMAGE)
screen.blit(img, (0, 0))


pygame.draw.circle(screen, BACKGROUND_COLOR, [480,270], 50) 
pygame.display.flip()

finish = False
while not finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True

pygame.quit()
