import pygame
import random

pygame.init()
screen = pygame.display.set_mode((900,600))
pygame.display.set_caption("СИМУЛЯТОР БРОСКА МОНЕТЫ")
icon = pygame.image.load('.venv/icon.png')
pygame.display.set_icon(icon)

image1 = pygame.image.load("image1.png")
image2 = pygame.image.load("image2.png")

coin_x, coin_y = (450) -65, (300)
coin_velocity = 0
gravity = 1
jump_strength = -25
coin_image = image1

clock = pygame.time.Clock()

result = random.choice(["100", "ELTANBA"])
frames = 200
show_result = False

run = True
while run:
    # screen.fill("blue")
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
    if frames>1:
        screen.fill("light blue")
        coin_velocity += gravity
        coin_y += coin_velocity

        if coin_y >= 600 - image1.get_height():
            coin_y = 600 - image1.get_height()
            coin_velocity = jump_strength

            if coin_image == image1:
                coin_image = image2
            else:
                coin_image = image1
        screen.blit(coin_image,(coin_x,coin_y))
        frames -= 1
    pygame.display.flip()
    clock.tick(40)

