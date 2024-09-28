import pygame
background = pygame.display.set_mode((480, 360))
pygame.display.set_caption('Monkey-Banana')

x_pos = background.get_size()[0] // 2
y_pos = background.get_size()[1] // 2

fps = pygame.time.Clock()

play = True
while play:
    deltaTime = fps.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
    if event.type == pygame.MOUSEMOTION:
        x_pos = pygame.mouse.get_pos()[0]
        y_pos = pygame.mouse.get_pos()[1]


    background.fill((255, 0, 0))

    # 원그리기 
    pygame.draw.circle(background, (0, 0, 255), (x_pos, y_pos), 30)

    pygame.display.update()

    pygame.quit()

