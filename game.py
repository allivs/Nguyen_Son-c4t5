import pygame

# 1: Initilize
pygame.init()

pygame.display.set_caption("PONG GAME")

# 2: Set up game window
SIZE = (600, 600)
BG_COLOR = (0, 0, 0)
canvas = pygame.display.set_mode(SIZE)

clock = pygame.time.Clock()

paddle_image = pygame.image.load("assets/paddle.png")
ball_image = pygame.image.load("assets/ball.png")

loop = True
x1 = 0
y1 = 100

x2 = 570
y2 = 400

x3 = 300
y3 = 270
x3_v = 5
y3_v = 3

w_press = False
s_press = False

up_press = False
down_press = False

while loop:
    events = pygame.event.get()
    for e in events:
        if e.type == pygame.QUIT:
            loop = False
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_w:
                w_press = True
            elif e.key == pygame.K_s:
                s_press = True
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_UP:
                up_press = True
            elif e.key == pygame.K_DOWN:
                down_press = True
        if e.type == pygame.KEYUP:
            if e.key == pygame.K_w:
                w_press = False
            elif e.key == pygame.K_s:
                s_press = False
        if e.type == pygame.KEYUP:
            if e.key == pygame.K_UP:
                up_press = False
            elif e.key == pygame.K_DOWN:
                down_press = False
    if w_press:
        y1 -= 10
    if s_press:
        y1 += 10
    if up_press:
        y2 -= 10
    if down_press:
        y2 += 10

    x3 += x3_v
    y3 += y3_v

    if x3 >= 545 or x3 <= 30:
        x3_v = -x3_v
    if y3 >= 540 or y3 <= 30:
        y3_v = -y3_v

    canvas.fill(BG_COLOR)
    canvas.blit(paddle_image, (x1, y1))
    canvas.blit(paddle_image, (x2, y2))
    canvas.blit(ball_image, (x3, y3))
    clock.tick(60)
    pygame.display.flip()

