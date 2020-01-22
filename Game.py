import pygame
import math

# Const
WINDOW_WIDTH = 960
WINDOW_HEIGHT = 540
BACKGROUND_COLOR = (255,208,210)
BLACK = (0, 0, 0)
IMAGE = ['background1.jpg', 'background2.jpg', 'background3.jpg']
SHROOM = 'shroom.png'
SOUND_FILE = "scaryTrane.mp3"
REFRESH_RATE = 60
LEFT = 1
SCROLL = 2
RIGHT = 3


# Init
pygame.init()
size = (WINDOW_WIDTH, WINDOW_HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Game")
circlePlacement = 480
circleSide = True  # true is right
clock = pygame.time.Clock()
shroom_image = pygame.image.load(SHROOM).convert()
shroom_image.set_colorkey(BLACK)
pygame.mixer.init()
pygame.mixer.music.load(SOUND_FILE)
pygame.mixer.music.play()
pygame.mixer.music.pause()
pygame.font.init()
imgIndex = 0
play = True
font = pygame.font.SysFont("comicsansms", 72)
text = font.render("Welecome to Earth", True, (0, 128, 0))
img = pygame.image.load(IMAGE[imgIndex])
screen.blit(img, (0, 0))
circleDiraction = 1
movingCricleToggle = False

finish = False
while not finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True

        # user pressed a mouse
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
            movingCricleToggle = False
            screen.blit(shroom_image, pygame.mouse.get_pos())

        # user pressed a button
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s and play:  # key is s and music is off
                pygame.mixer.music.unpause()
                play = False
            elif event.key == pygame.K_s and not play:  # key is s and music is on
                pygame.mixer.music.pause()
                play = True

            if event.key == pygame.K_SPACE:  # key is space
                movingCricleToggle = False
                screen.blit(img, (0, 0))

            if event.key == pygame.K_n:  # key is n
                imgIndex += 1
                if imgIndex == 3:
                    imgIndex = 0
                img = pygame.image.load(IMAGE[imgIndex])
                screen.blit(img, (0, 0))

            if event.key == pygame.K_m:  # key is m
                movingCricleToggle = False
                screen.blit(img, (0, 0))
                screen.blit(text, (240, 270))

            if event.key == pygame.K_k:  # key is k
                movingCricleToggle = True

            if event.key == pygame.K_o:  # key is o
                pygame.draw.line(screen, BACKGROUND_COLOR, (0, 270), (WINDOW_WIDTH, 270), 1)

            if event.key == pygame.K_j:
                for i in range(0, 360, 10):
                    pygame.draw.line(screen, BACKGROUND_COLOR, [480, 270], [480 + 100 * math.sin(i), 270 + 100 * math.cos(i)], 2)
     
    pygame.display.flip()
    clock.tick(REFRESH_RATE)

pygame.quit()
