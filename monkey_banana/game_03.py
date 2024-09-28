import pygame
background = pygame.display.set_mode((480, 360))
pygame.display.set_caption('Monkey-Banana')

play = True
while play:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False


    background.fill((255, 0, 0))

    pygame.draw.line(background, (0, 0, 0), (240, 0), (240, 360))
    # pygame.draw.rect(background, (0, 0,255), (240, 180, 100, 50), width = 3)

    # pygame.draw.ellipse(background, (0, 0, 255), (240, 180, 100, 50)) # 원형
    pygame.draw.polygon(background, (0, 0, 255), ((146, 0), (291, 105), (236, 277), (56, 277))) # 다각형

    pygame.display.update()

    pygame.quit()