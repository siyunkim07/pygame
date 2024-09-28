# pygame 키보드 이벤트 처리

import pygame 

pygame.init()

background = pygame.display.set_mode((480, 360))
pygame.display.set_caption('Monkey-Banana')

x_pos = background.get_size()[0] // 2
y_pos = background.get_size()[1] // 2

fps = pygame.time.Clock()

to_x = 0 
to_y = 0

play = True
while play:

    # 1초 동안 while 문을 몇번 돌 것인지를 지정함..
    deltaTime = fps.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          play = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                to_y = -1
            elif event.key == pygame.K_DOWN:
                to_y = 1
            elif event.key == pygame.K_LEFT:
                to_x  = -1
            elif event.key == pygame.K_RIGHT:
                to_x = 1
    if event.type == pygame.KEYUP:
        # 키보드에서  뗴는 순간 증가값이 0이 된다.
        to_x = 0
        to_y = 0
    x_pos += to_x
    y_pos += to_y


# 배경 색깔 다시 그리기

background.fill((255, 0, 0))

# 원그리기 
pygame.draw.circle(background, (0, 0, 255), (x_pos, y_pos), 5)

pygame.display.update()

pygame.quit()