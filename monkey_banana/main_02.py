import pygame

pygame.init()

surface = pygame.display.set_mode((400, 300))

# 창의 이름을 변경
pygame.display.set_caption('My game')

# 창의 아이콘 변경

icon_name = pygame.image.load('images/image-01.PNG')
pygame.display.set_icon(icon_name)

# RGB color 설정
color = (255, 0, 0)


# surface 색상 지정

surface.fill(color)

pygame.display.flip() # pygame.display.update()

play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

pygame.quit()