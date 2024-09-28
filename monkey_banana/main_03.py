# surface는 객체의 모양과 화면세서의 위치를 나타내는데 사용
# pygame에서 생성하는 모든 객체, 텍스트, 이미지는 모두 surface를 사용하여 생성된다.


# surface에 사각형 그리기

import pygame


pygame.init()

surface = pygame.display.set_mode((400, 300))

color = (255, 255, 0)

print(pygame.Rect(30, 30, 60, 60))

pygame.draw.rect(surface, color, pygame.Rect(30, 30, 60, 60))

pygame.display.flip()
play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
pygame.quit()