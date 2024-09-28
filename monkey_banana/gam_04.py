# pygame.image.load (이미지 파일)
# image.get_rect().size() <- 이미지 사이즈
# surface.blit(이미지, (x_pos, y_pos))


import pygame

pygame.init()

background = pygame.display.set_mode((480, 360))
pygame.display.set_caption('Monkey-Banana')

# fps (1초에 while문을 몇번 실행할 것인가..)

fps = pygame.time.Clock()



# 필요한 이미지 로딩..
image_bg = pygame.image.load("monkey_banana/images/Blue-sky.png")
image_banana = pygame.image.load("monkey_banana/images/bananas.png")
image_monkey = pygame.image.load("monkey_banana/images/monkey.png")

# 이미지의 가로, 세로 값..
size_bg_width = background.get_size()[0] # width
size_bg_height = background.get_size()[1] # height

size_banana_width = image_banana.get_size()[0] # width
size_banana_height = image_banana.get_size()[1] # height

size_monkey_width = image_monkey.get_size()[0] # width
size_monkey_height = image_monkey.get_size()[1] # height

# banana, monkey의 최초 좌표값 설정

x_pos_banana = size_bg_width / 2 - size_banana_width / 2
y_pos_banana = 0

x_pos_monkey = size_bg_width / 2 - size_monkey_width / 2
y_pos_monkey = size_bg_height - size_monkey_height

# 움직임의 값 초기설정


to_x = 0
to_y = 0


point = 0

# font 로딩
font_point = pygame.font.SysFont(None, 30)
font_gameover = pygame.font.SysFont(None, 80)
text_gameover = font_gameover.render("GAME OVER", True, (255, 0, 0))

size_text_width = text_gameover.get_rect().size[0]
size_text_height = text_gameover.get_rect().size[1]

x_pos_text = size_bg_width / 2 - size_text_width / 2
y_pos_text = size_bg_height / 2 - size_text_width / 2

x_speed_banana = 1
y_speed_banana = 1


# 게임 Loop 만들기...
play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x = -1
            elif event.key == pygame.K_RIGHT:
                to_x = 1


        if event.type == pygame.KEYUP:
            to_x = 0
            
    # 원숭이가 왼쪽, 오른쪽으로 벗어나지 않게 하기...
    if x_pos_monkey < 0:
        x_pos_monkey = 0
    elif x_pos_monkey > size_bg_width - size_monkey_width:
        x_pos_monkey = size_bg_width -size_monkey_width
    else:
        x_pos_monkey += to_x

    x_pos_monkey += to_x
  

    x_pos_banana += x_speed_banana
    y_pos_banana += y_speed_banana

    if x_pos_banana <= 0:
        x_speed_banana = -(x_speed_banana)
        x_pos_banana = 0
    elif x_pos_banana >= size_bg_width - size_banana_width:
        x_speed_banana = -(x_speed_banana)
        x_pos_banana = size_bg_width - size_banana_width

    if y_pos_banana <= 0:
        y_speed_banana = -(y_speed_banana)
        y_pos_banana = 0
    elif y_pos_banana >= size_bg_height - size_banana_height:
        background.blit(text_gameover, (x_pos_text, y_pos_text))
        pygame.display.update()
        pygame.time.delay(2000)
        play = False
    # 바나나와 원숭이가 충돌하는지 판단...

    rect_banana = image_banana.get_rect()
    rect_banana.left = x_pos_banana
    rect_banana.top = y_pos_banana

    rect_monkey = image_monkey.get_rect()
    rect_monkey.left = x_pos_monkey
    rect_monkey.top = y_pos_monkey

    if rect_monkey.colliderect(rect_banana):
        x_speed_banana = -(x_speed_banana)
        y_speed_banana = -(y_speed_banana)
        point += 1

    # 이미지들을 blit 함...
    background.blit(image_bg, (0, 0))
    background.blit(image_monkey, (x_pos_monkey, y_pos_monkey))
    background.blit(image_banana, (x_pos_banana, y_pos_banana))

    text_point = font_point.render(str(point), True, (0, 0, 0))
    background.blit(text_point, (10, 10))
    pygame.display.update()

pygame.quit()
