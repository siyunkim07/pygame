import pygame
import random

# 초기화 및 디스플레이 설정

pygame.init()
background = pygame.display.set_mode((480, 360))
pygame.display.set_caption('SPACE WAR')


# 이미지 불러오기
image_bg = pygame.image.load('images/Moon.png')
image_pico = pygame.image.load('images/pico-1.png')
image_rocket = pygame.image.load('images/rocket-1.png')
image_star = pygame.image.load('images/star-1.png')
image_ball = pygame.image.load('images/ball-1.png')

# 이미지의 가로, 세로 크기 구하기...
size_bg_width = background.get_size()[0]
size_bg_height = background.get_size()[1]

size_pico_width = image_pico.get_rect().size[0]
size_pico_height = image_pico.get_rect().size[1]

size_rocket_width = image_rocket.get_rect().size[0]
size_rocket_height = image_rocket.get_rect().size[1]

size_star_width = image_star.get_rect().size[0]
size_star_height = image_star.get_rect().size[1]

size_ball_width = image_ball.get_rect().size[0]
size_ball_height = image_ball.get_rect().size[1]

# 각 이미지의 초기 좌표값을 설정....

x_pos_pico = size_bg_width / 2 - size_pico_width / 2
y_pos_pico = size_bg_height - size_pico_height

x_pos_rocket = size_bg_width / 2 - size_rocket_width / 2
y_pos_rocket = 0

x_pos_star = size_bg_width / 2 - size_star_width / 2
y_pos_star = (size_bg_height - size_pico_height) - size_star_height

x_pos_ball = size_bg_width / 2 - size_ball_width / 2
y_pos_ball = size_rocket_height

# rocket을 움직이기 위한 변수 값 설정...
to_x_rocket = 0
random_rocket = random.randrange(0, size_bg_width - size_rocket_width) # randrange() 범위 안의 값을 랜덤으로 정함

to_x_pico = 0

# 공의 타이밍 리스트

ball_time = 0
balls = []
random_time = random.randrange(100, 200)
stars = []

# pico, rocket의 체력 추가
hp_pico = 10
hp_rocket = 10

# pico, rocket의 rect 값 구하기
rect_pico = image_pico.get_rect()
rect_rocket = image_rocket.get_rect()

rect_pico.topleft = (x_pos_pico, y_pos_pico)
rect_rocket.topleft = (x_pos_rocket, y_pos_rocket)

# star , ball 의 rect리스트
rect_stars = []
rect_balls = []

# 게임 종료 font 준비...
font_hp = pygame.font.SysFont(None, 30)
font_gameover = pygame.font.SysFont(None, 100)

# game over 판정 변수
gameover = False

play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        
        # 왼쪽, 오른쪽 키보드로 to_x_pico 값 조종하기
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x_pico = -0.5
            elif event.key == pygame.K_RIGHT:
                to_x_pico = 0.5

            # 스페이스 바를 누르면 별 공격..
            if event.key == pygame.K_SPACE:
                x_pos_star = x_pos_pico + size_star_width / 2
                stars.append([x_pos_star, y_pos_star])
                # star rect 값을 저장
                rect_stars.append(image_star.get_rect())
                

        if event.type == pygame.KEYUP:
            to_x_pico = 0
    
    # pico가 움직이게 하기
    if x_pos_pico < 0:
        x_pos_pico = 0
    elif x_pos_pico > size_bg_width - size_pico_width:
        x_pos_pico = size_bg_width - size_pico_width
    else:
        x_pos_pico += to_x_pico
    # pico의 topleft를 저장
    rect_pico.topleft = (x_pos_pico, y_pos_pico)
    



    # rocket의 x좌표를 랜덤으로 움직이게 하기. 로켓이 random 값으로 찾아감..
    if random_rocket > x_pos_rocket:
        x_pos_rocket += 0.5
    elif random_rocket < x_pos_rocket:
        x_pos_rocket -= 0.5
    else:
        random_rocket = random.randrange(0, size_bg_width - size_rocket_width)
    # rocket의 topleft를 저장
    rect_rocket.topleft = (x_pos_rocket, y_pos_rocket)
    # ball 공격하기, 너무 많이 떨어지지 않게
    ball_time += 1
    if ball_time == random_time:
        random_time = random.randrange(70, 100)
        ball_time = 0
        x_pos_ball = x_pos_rocket + size_ball_width / 2
        balls.append([x_pos_ball, y_pos_ball])
        # ball의 rect를 저장...
        rect_balls.append(image_ball.get_rect())


    # 이미지 그리기
    background.blit(image_bg, (0, 0))
    background.blit(image_pico, (x_pos_pico, y_pos_pico))
    background.blit(image_rocket, (x_pos_rocket, y_pos_rocket))

    # 별 그리기 
    if len(stars):
        for star in stars:

            i = stars.index(star)

            star[1] -= 1

            # star의 topleft 저장..
            background.blit(image_star, (star[0], star[1]))

            rect_stars[i].topleft = (star[0], star[1])
            if rect_stars[i].colliderect(rect_rocket):
                stars.remove(star)
                rect_stars.remove(rect_stars[i])
                hp_rocket -= 1
                if hp_rocket == 0:
                    gameover = "PICO WIN!"

            if star[1] <= 0:
                stars.remove(star)
                rect_stars.remove(rect_stars[i])

    # ball 그리기....
    if len(balls):
        for ball in balls:
            i = balls.index(ball)
            ball[1] += 1
            background.blit(image_ball, (ball[0], ball[1]))

            # ball과 pico 충돌 판정...
            rect_balls[i].topleft = (ball[0],ball[1])

            if rect_balls[i].colliderect(rect_pico):
                balls.remove(ball)
                rect_balls.remove(rect_balls[i])
                hp_pico -= 1
                if hp_pico == 0:
                    gameover = "ROCKET WIN!"
            if ball[1] >= size_bg_height:
                rect_balls.remove(rect_balls[i])
                balls.remove(ball)




    text_hp_pico = font_hp.render('pico'+str(hp_pico), True, (255, 255, 0))
    background.blit(text_hp_pico,(10, 10))

    text_hp_rocket = font_hp.render('rocket'+str(hp_rocket), True, (255, 255, 0))
    background.blit(text_hp_rocket,(380, 10))

    if gameover:
        text_gameover = font_gameover.render(gameover, True, (255, 0, 0))
        size_text_width = text_gameover.get_rect().size[0]
        size_text_height = text_gameover.get_rect().size[1]

        x_pos_text = size_bg_width / 2 - size_text_width / 2
        y_pos_text = size_bg_height / 2 - size_text_height / 2


        background.blit(text_gameover, (x_pos_text, y_pos_text))
        pygame.display.update()
        pygame.time.delay(1000)
        play = False 
    pygame.display.update()

pygame.quit()

