import pygame

pygame.init()

surface = pygame.display.set_mode((500, 500))

image = pygame.image.load('monkey_banana/images/Blue-sky.png')


# 이미지를 surface에 위치 시킨다.
surface.blit(image, (0, 0))

pygame.display.update()
play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

pygame.quit()
