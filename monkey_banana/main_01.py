import pygame 

# pygame 초기화
pygame.init()

# pygame window 만들기 
pygame.display.set_mode((800, 800))

# pygame의 기본 loop : 모든 처리가 된다.
play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
pygame.quit()