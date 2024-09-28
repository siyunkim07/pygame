import pygame

from pygame.locals import *
import random
pygame.init()

# window 만들기
width = 500
height = 500

screen_size = (width, height)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('CAR GAME')

# color 정의

gray = (100 , 100, 100)
green = (70, 208, 56)
red = (255, 0, 0)
white = (255, 255, 255)
yellow = (255, 232, 0)

# road and marker size 설정
road_width = 300
marker_width = 10
marker_height = 50

# draw road and edge, marker
road = (100, 0, road_width, height)
left_edge_marker = (95, 0, marker_width, height)
right_edge_marker = (390, 0, marker_width, height)

# game loop 만들기

clock = pygame.time.Clock()
fps = 120

# game setting 변수 선언
gameover = False
speed = 2
score = 0

# lane 좌표 구하기
left_lane = 150
center_lane =250
right_lane = 350
lanes = [left_lane, center_lane, right_lane]

# lane markers를 움직이도록 하는 변수 설정
lane_marker_move_y = 0

# class 정의

class Vehicle(pygame.sprite.Sprite):
    def __init__(self, image, x,y):
        pygame.sprite.Sprite.__init__(self)

        # 자동차의 이미지가 lane 크기를 벗어나지 않도록 축소 시킴..
        image_scale = 45 / image.get_rect().width
        new_width = image.get_rect().width * image_scale
        new_height = image.get_rect().height * image_scale
        self.image = pygame.transform.scale(image,(new_width, new_height))

        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

class PlayerVehicle(Vehicle):
    def __init__(self, x, y):
        image = pygame.image.load('images/car.png')
        super().__init__(image, x , y)
# player's starting 좌표 
player_x = 250
player_y = 400

# player의 자동차 생성...
player_group = pygame.sprite.Group()
player = PlayerVehicle(player_x, player_y)
player_group.add(player)

# 다른 자동차들 이미지 로딩... 생성
image_filenames = ['pickup_truck.png', 'semi_trailer.png', 'taxi.png', 'van.png']
vehicle_images = []
for image_filename in image_filenames:
    image = pygame.image.load('images/' + image_filename)
    vehicle_images.append(image)

# vehicle들의 spriye group 생성
vehicle_group = pygame.sprite.Group()


# 충돌 이미지 로딩 ....
crash = pygame.image.load('images/crash.png')
crash_rect = crash.get_rect()


running = True
while running:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # 자동차를 키보드로 좌, 우로 움직이기
        if event.type == KEYDOWN:
            if event.key == K_LEFT and player.rect.center[0] > left_lane:
                player.rect.x -= 100
            elif event.key == K_RIGHT and player.rect.center[0] < right_lane:
                player.rect.x += 100
        
            # lane을 변경할 때, 충돌 side 결정..
            for vehicle in vehicle_group:
                if pygame.sprite.collide_rect(player, vehicle):
                    gameover = True

                    if event.key == K_LEFT:
                        player.rect.left = vehicle.rect.right
                        crash_rect.center = [player.rect.left, (player.rect[1] + vehicle.rect.center[1]) / 2]
                    elif event.key == K_RIGHT:
                        player.rect.right = vehicle.rect.left
                        crash_rect.center = [player.rect.right, (player.rect[1] + vehicle.rect.center[1]) / 2]



    # draw grass
    screen.fill(green)

   # 도로 그리기
    pygame.draw.rect(screen, gray, road)


    # edge , markers 그리기
    pygame.draw.rect(screen, yellow, left_edge_marker)
    pygame.draw.rect(screen, yellow, right_edge_marker)

    lane_marker_move_y += speed * 2
    if lane_marker_move_y >= marker_height * 2:
        lane_marker_move_y = 0

    # lane markers를 그리기
    for y in range(marker_height * -2, height, marker_height * 2):
        pygame.draw.rect(screen, white, (left_lane + 45, y + lane_marker_move_y, marker_width, marker_height))
        pygame.draw.rect(screen, white, (center_lane + 45, y + lane_marker_move_y, marker_width, marker_height))

    # player 자동차 그리기..
    player_group.draw(screen)

    # 자동차 추가
    if len(vehicle_group) < 2:
        add_vehicle = True
        for vehicle in vehicle_group:
            if vehicle.rect.top < vehicle.rect.height * 1.5:
                add_vehicle = False
        if add_vehicle:
            # 자동차 생성 lane을 랜덤으로 생성..
            lane = random.choice(lanes)

            # 생성할 자동차를 random으로 생성
            image = random.choice(vehicle_images)
            vehicle= Vehicle(image, lane, height / -2)
            vehicle_group.add(vehicle)

    # 자동차들을 움직이게
    for vehicle in vehicle_group:
        vehicle.rect.y += speed
    
        # 만약 자동차가 화면 밑으로 사라지면, 제거해준다
        if vehicle.rect.top >= height:
            vehicle.kill()
            score += 1
            # 자동차가 5대씩 지나가면 속도를 올려줌
            if score > 0 and score % 5 == 0:
                speed += 1
    # 자동차를 화면에 그려주기
    vehicle_group.draw(screen)

    # score 디스플레이
    font = pygame.font.Font(pygame.font.get_default_font(), 16)
    text = font.render('Score: ' + str(score), True, white)
    text_rect = text.get_rect()
    text_rect.center = (50, 400)
    screen.blit(text, text_rect)

    # 정면 충돌 여부를 판단..
    if pygame.sprite.spritecollide(player, vehicle_group, True):
        gameover = True
        crash_rect.center = [player.rect.center[0], player.rect.top]
    if gameover:
        screen.blit(crash, crash_rect)

        pygame.draw.rect(screen, red, (0, 50, width, 100))
        
        font = pygame.font.Font(pygame.font.get_default_font(), 15)
        text = font.render('GAME OVER... PLAY AGAIN? (ENTER Y OR N)', True, white)
        text_rect = text.get_rect()
        text_rect.center = (width / 2, 100)
        screen.blit(text, text_rect)
    pygame.display.update()

    # 계속 여부 사용자 입력 받기...
    while gameover:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == QUIT:
                gameover = False
                running = False


            # 사용자 입력 받기 
            if event.type == KEYDOWN:
                if event.key == K_y:
                    # game reset
                    gameover = False
                    speed = 2
                    score = 0
                    vehicle_group.empty()
                    player.rect.center = [player_x, player_y]
                elif event.key == K_n:
                    gameover = False
                    running = False
pygame.quit()