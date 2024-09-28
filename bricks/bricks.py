import pygame
import random

pygame.init()

background = pygame.display.set_mode((480, 360))
pygame.display.set_caption("Brick Breaking")

# 배경 사이즈
size_width_bg = background.get_size()[0]
size_height_bg = background.get_size()[1]

# 패달의 사이즈, 좌표, Rect
size_width_pedal = 100
size_height_pedal = 15

x_pos_pedal = size_width_bg // 2 - size_width_pedal // 2
y_pos_pedal = size_height_bg - size_height_pedal

rect_pedal = pygame.Rect(x_pos_pedal, y_pos_pedal, size_width_pedal, size_height_pedal)

# pedal을 좌우로 조절하기 위한 x 좌표값
to_x_pedal = 0

#공의 사이즈, 조표, Rect
size_radius_ball = 20

x_pos_ball = size_width_bg // 2
y_pos_ball = size_height_bg - size_height_pedal - size_radius_ball

rect_ball = pygame.Rect(x_pos_ball, y_pos_ball, size_radius_ball * 2, size_radius_ball * 2)
rect_ball.center = (x_pos_ball, y_pos_ball)

# 공의 방향과 스피드를 결정하는 변수 (처음엔 둘다 +)
x_speed_ball = 0.1
y_speed_ball = 0.1

# 블록 사이즈, 좌표, Rect
size_width_block = size_width_bg // 10
size_height_block = 30

x_pos_block = 0
y_pos_block = 0

rect_block = [[] for _ in range(10)]	# [[], [], [], [], [], [], [], [], [], []]
color_block = [[] for _ in range(10)]

for i in range(10):
  for j in range(3):
    rect_block[i].append(pygame.Rect(i * size_width_block, j * size_height_block, size_width_block, size_height_block))
    color_block[i].append((random.randrange(255), random.randrange(150, 255), random.randrange(150, 255)))

# print(rect_block)

# 마우스 좌표 (마우스로 pedal을 움직임)
x_pos_mouse, y_pos_mouse = 0, 0

#  점수 변수 초기화
point = 0

# 시작 변수
start = True

# 글자찍기
def game_text(word):
  font = pygame.font.SysFont(None, 100)
  text = font.render(word, True, (0, 255, 255))
  size_width_text = text.get_rect().size[0]
  size_height_text = text.get_rect().size[1]

  x_pos_text = size_width_bg / 2 - size_width_text / 2
  y_pos_text = size_height_bg / 2 - size_height_text / 2
  background.blit(text, (x_pos_text, y_pos_text))
# Gameover 판정 변수
gameover = False

play = True
while play:
  if start:
    start = False
    for i in range(3, 0, -1):
      background.fill((255, 255, 255))
      game_text(str(i))
      pygame.display.update()
      pygame.time.delay(1000)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      play = False
    
    ## 마우스로 pedal 움직이기
    if event.type == pygame.MOUSEMOTION:
      x_pos_mouse, y_pos_mouse = pygame.mouse.get_pos()
      # 화면 밖으로 나가지 않게....
      if x_pos_mouse - size_width_pedal // 2 >= 0 and x_pos_mouse + size_width_pedal // 2 <= size_width_bg:
        x_pos_pedal = x_pos_mouse - size_width_pedal // 2
        rect_pedal.left = x_pos_mouse - size_width_pedal // 2

  # 배경색 칠하기
  background.fill((255, 255, 255))

  # 페달 그리기
  #  pygame.draw.rect(surface, color, rect(x, y, width, height))
  pygame.draw.rect(background, (244, 255, 0), rect_pedal)

  # 공 좌표 계산
  if x_pos_ball - size_radius_ball <= 0:
    x_speed_ball = -x_speed_ball
  elif x_pos_ball >= size_width_bg - size_radius_ball:
    x_speed_ball = -x_speed_ball

  if y_pos_ball - size_radius_ball <= 0:
    y_speed_ball = -y_speed_ball
  elif y_pos_ball >= size_height_bg - size_radius_ball:
    background.fill((255, 255, 255))
    game_text("GAME OVER")
    pygame.display.update()
    pygame.time.delay(1000)
    break


  # 공 좌표에 스피드값 누적
  x_pos_ball += x_speed_ball 
  y_pos_ball += y_speed_ball
  
  # 공 그리기
  rect_ball.center = (x_pos_ball, y_pos_ball)  # 변경된 rect.center 값 지정
  # pagame.draw.dircle(surface, color, center, radius)
  pygame.draw.circle(background, (255, 0, 255), (x_pos_ball, y_pos_ball), size_radius_ball)


  # 공이 pedal에 닿을 때
  if rect_ball.colliderect(rect_pedal):
    y_speed_ball = -y_speed_ball

  # 블록 그리기 (for문으로 10개 * 3층 만들기)
  for i in range(10):
    for j in range(3):
      if rect_block[i][j]:
        pygame.draw.rect(background, color_block[i][j], rect_block[i][j])
        rect_block[i][j].topleft = (i * size_width_block, j * size_height_block)

        # 공 – 벽돌에 닿았을 때
        if rect_ball.colliderect(rect_block[i][j]):
          x_speed_ball = -x_speed_ball
          y_speed_ball = -y_speed_ball
          rect_block[i][j] = 0
          point += 1

    if point == 30:
      background.fill((255, 255, 255))
      game_text("congratulations!!")
      pygame.display.update()
      pygame.time.delay(1000)
      play = False
  pygame.display.update()

pygame.quit()