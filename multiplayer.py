import pygame
import button
import sys

from time import sleep

pygame.init()

# Sounds
SCORE = pygame.mixer.Sound('Assets/score.mp3')
HIT = pygame.mixer.Sound('Assets/hit.mp3')

# Cursors
C_WIDTH = 18
C_HEIGHT = 100
VEL = 15  # Cursor Speed
VEL2 = 6 # AI Speed

# Screen Variables
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")
BORDER = pygame.Rect(WIDTH // 2 - 5, 0, 10, HEIGHT)
FPS = 60

# RGB Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Main Menu Text
TITLE_FONT = pygame.font.SysFont('impact', 100)
TITLE_TEXT = TITLE_FONT.render(
    ("PONG"), 1, WHITE)
SINGLE_BUTTON = button.SingleButton(200, 180, button.SINGLE_BUTTON_TEXT)
MULT_BUTTON = button.MultButton(200, 300, button.MULT_BUTTON_TEXT)
CLASSIC_BUTTON = button.ClassicButton(50, 50, button.CLASSIC_BUTTON_TEXT)
BLITZ_BUTTON = button.BlitzButton(50, 230, button.BLITZ_BUTTON_TEXT)
DOUBLE_BUTTON = button.DoubleButton(50, 400, button.DOUBLE_BUTTON_TEXT)

# Winner Text
WINNER_FONT = pygame.font.SysFont('impact', 100)

# On-Screen Objects
def draw_objects():
    pygame.draw.rect(WIN, WHITE, BORDER)  # Middle Border

# Ends the game and displays who won
def end_game(text):
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width() /
                         2, HEIGHT/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(2000)

# Main multiplayer game loop
def game_loop_mult():
    # Points
    pointsp1 = 0
    pointsp2 = 0

    # Ball Variables
    ball_speed_x = -10
    ball_speed_y = 10
    BALL_X = 400
    BALL_Y = 300

    # Cursor Variables
    LEFT_X = 30
    LEFT_Y = 250
    RIGHT_X = 750
    RIGHT_Y = 250

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        WIN.fill(BLACK)
        draw_objects()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False

        # Keep track of keys pressed
        keys = pygame.key.get_pressed()

        # Left Cursor Keys
        if keys[pygame.K_w] and LEFT_Y > 10:
            LEFT_Y -= VEL
        if keys[pygame.K_s] and LEFT_Y < 590 - C_HEIGHT:
            LEFT_Y += VEL

        # Right Cursor Keys
        if keys[pygame.K_i] and RIGHT_Y > 10:
            RIGHT_Y -= VEL
        if keys[pygame.K_k] and RIGHT_Y < 590 - C_HEIGHT:
            RIGHT_Y += VEL

        # Setting ball movement speed
        BALL_X += ball_speed_x
        BALL_Y += ball_speed_y

        # Drawing on-screen objects
        left_cursor = pygame.draw.rect(WIN, WHITE, (LEFT_X, LEFT_Y, C_WIDTH, C_HEIGHT))
        right_cursor = pygame.draw.rect(WIN, WHITE, (RIGHT_X, RIGHT_Y, C_WIDTH, C_HEIGHT))
        ball = pygame.draw.circle(WIN, WHITE, [BALL_X, BALL_Y], 15, 0)

        # Left Cursor bounce mechanics
        if ball.collidepoint(left_cursor.topright):
            ball_speed_x *= -1
            ball_speed_y *= -1
            HIT.play()
        if ball.collidepoint(left_cursor.bottomright):
            ball_speed_x *= -1
            ball_speed_y *= -1
            HIT.play()
        elif left_cursor.colliderect(ball) and not ball.collidepoint(left_cursor.topright) or ball.collidepoint(left_cursor.bottomright):
            ball_speed_x *= -1
            HIT.play()

        # Right Cursor bounce mechanics
        if ball.collidepoint(right_cursor.topleft):
            ball_speed_x *= -1
            ball_speed_y *= -1
            HIT.play()
        if ball.collidepoint(right_cursor.bottomleft):
            ball_speed_x *= -1
            ball_speed_y *= -1
            HIT.play()
        elif right_cursor.colliderect(ball) and not ball.collidepoint(right_cursor.topleft) or ball.collidepoint(right_cursor.bottomleft):
            ball_speed_x *= -1
            HIT.play()

        # Ball re-appear and add score for sides + delay
        if BALL_X < 10:
            sleep(0.5)
            BALL_X = 400
            BALL_Y = 300
            pointsp2 += 1
            SCORE.play()
        if BALL_X > 790:
            sleep(0.5)
            BALL_X = 400
            BALL_Y = 300
            pointsp1 += 1
            SCORE.play()

        # Ball top/bottom bounce mechanics
        if BALL_Y < 10:
            ball_speed_y *= -1
        if BALL_Y > 590:
            ball_speed_y *= -1

        # Scoreboard Text
        SCORE_FONT = pygame.font.SysFont('impact', 50)
        P1_SCORE = SCORE_FONT.render(
            (str(pointsp1)), 1, WHITE)
        P2_SCORE = SCORE_FONT.render(
            (str(pointsp2)), 1, WHITE)

        # Score Display
        WIN.blit(P1_SCORE, (330, 10))
        WIN.blit(P2_SCORE, (445, 10))

        # End game at x points
        winner_text = ""
        if pointsp1 == 10:
            winner_text = "Player 1 Wins!"

        if pointsp2 == 10:
            winner_text = "Player 2 Wins!"

        if winner_text != "":
            end_game(winner_text)
            break

        # Update screen display
        pygame.display.update()

# Blitz multiplayer game loop
def game_loop_blitz():
    # Ball Color
    ball_color = 0

    # Cursor Speed
    VELB = 25

    # Points
    pointsp1 = 0
    pointsp2 = 0

    # Ball Variables
    ball_speed_x = -5
    ball_speed_y = 5
    BALL_X = 400
    BALL_Y = 300

    # Cursor Variables
    LEFT_X = 30
    LEFT_Y = 250
    RIGHT_X = 750
    RIGHT_Y = 250

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        WIN.fill(BLACK)
        draw_objects()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False

        # Keep track of keys pressed
        keys = pygame.key.get_pressed()

        # Left Cursor Keys
        if keys[pygame.K_w] and LEFT_Y > 10:
            LEFT_Y -= VELB
        if keys[pygame.K_s] and LEFT_Y < 590 - C_HEIGHT:
            LEFT_Y += VELB

        # Right Cursor Keys
        if keys[pygame.K_i] and RIGHT_Y > 10:
            RIGHT_Y -= VELB
        if keys[pygame.K_k] and RIGHT_Y < 590 - C_HEIGHT:
            RIGHT_Y += VELB

        # Setting ball movement speed
        BALL_X += ball_speed_x
        BALL_Y += ball_speed_y

        # Drawing on-screen objects
        left_cursor = pygame.draw.rect(WIN, WHITE, (LEFT_X, LEFT_Y, C_WIDTH, C_HEIGHT))
        right_cursor = pygame.draw.rect(WIN, WHITE, (RIGHT_X, RIGHT_Y, C_WIDTH, C_HEIGHT))
        ball = pygame.draw.circle(WIN, WHITE, [BALL_X, BALL_Y], 15, 0)

        # Left Cursor bounce mechanics
        if ball.collidepoint(left_cursor.topright):
            ball_speed_x *= -1.2
            ball_speed_y *= -1.2
            ball_color += 1
            HIT.play()
        if ball.collidepoint(left_cursor.bottomright):
            ball_speed_x *= -1.2
            ball_speed_y *= -1.2
            ball_color += 1
            HIT.play()
        elif left_cursor.colliderect(ball) and not ball.collidepoint(left_cursor.topright) or ball.collidepoint(left_cursor.bottomright):
            ball_speed_x *= -1.2
            ball_color += 1
            HIT.play()

        # Right Cursor bounce mechanics
        if ball.collidepoint(right_cursor.topleft):
            ball_speed_x *= -1.2
            ball_speed_y *= -1.2
            ball_color += 1
            HIT.play()
        if ball.collidepoint(right_cursor.bottomleft):
            ball_speed_x *= -1.2
            ball_speed_y *= -1.2
            ball_color += 1
            HIT.play()
        elif right_cursor.colliderect(ball) and not ball.collidepoint(right_cursor.topleft) or ball.collidepoint(right_cursor.bottomleft):
            ball_speed_x *= -1.2
            ball_color += 1
            HIT.play()

        # Change ball color
        if ball_color == 1:
            ball = pygame.draw.circle(WIN, (227, 232, 172), [BALL_X, BALL_Y], 15, 0)
        elif ball_color == 2:
            ball = pygame.draw.circle(WIN, (198, 207, 103), [BALL_X, BALL_Y], 15, 0)
        elif ball_color == 3:
            ball = pygame.draw.circle(WIN, (217, 235, 38), [BALL_X, BALL_Y], 15, 0)
        elif ball_color == 4:
            ball = pygame.draw.circle(WIN, (245, 185, 34), [BALL_X, BALL_Y], 15, 0)
        elif ball_color == 5:
            ball = pygame.draw.circle(WIN, (252, 114, 8), [BALL_X, BALL_Y], 15, 0)
        elif ball_color == 6:
            ball = pygame.draw.circle(WIN, (252, 77, 8), [BALL_X, BALL_Y], 15, 0)
        elif ball_color == 7:
            ball = pygame.draw.circle(WIN, (252, 8, 8), [BALL_X, BALL_Y], 15, 0)
        elif ball_color == 8:
            ball = pygame.draw.circle(WIN, (0, 229, 255), [BALL_X, BALL_Y], 15, 0)
        elif ball_color > 8:
            ball = pygame.draw.circle(WIN, (0, 26, 255), [BALL_X, BALL_Y], 15, 0)

        # Ball re-appear and add score for sides + delay
        if BALL_X < 10:
            sleep(0.5)
            BALL_X = 400
            BALL_Y = 300
            ball_speed_x = -5
            ball_speed_y = 5
            ball_color = 0
            pointsp2 += 1
            SCORE.play()
        if BALL_X > 790:
            sleep(0.5)
            BALL_X = 400
            BALL_Y = 300
            ball_speed_x = -5
            ball_speed_y = 5
            ball_color = 0
            pointsp1 += 1
            SCORE.play()

        # Ball top/bottom bounce mechanics
        if BALL_Y < 10:
            ball_speed_y *= -1
        if BALL_Y > 590:
            ball_speed_y *= -1

        # Scoreboard Text
        SCORE_FONT = pygame.font.SysFont('impact', 50)
        P1_SCORE = SCORE_FONT.render(
            (str(pointsp1)), 1, WHITE)
        P2_SCORE = SCORE_FONT.render(
            (str(pointsp2)), 1, WHITE)

        # Score Display
        WIN.blit(P1_SCORE, (330, 10))
        WIN.blit(P2_SCORE, (445, 10))

        # End game at x points
        winner_text = ""
        if pointsp1 == 10:
            winner_text = "Player 1 Wins!"

        if pointsp2 == 10:
            winner_text = "Player 2 Wins!"

        if winner_text != "":
            end_game(winner_text)
            break

        # Update screen display
        pygame.display.update()

# Double multiplayer game loop
def game_loop_double():
    # Cursor Speed
    VELD = 25

    # Points
    pointsp1 = 0
    pointsp2 = 0

    # Ball Variables
    ball1_speed_x = -10
    ball1_speed_y = 10

    ball2_speed_x = 10
    ball2_speed_y = -10

    BALL1_X = 400
    BALL1_Y = 300

    BALL2_X = 400
    BALL2_Y = 200

    # Cursor Variables
    LEFT_X = 30
    LEFT_Y = 250
    RIGHT_X = 750
    RIGHT_Y = 250

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        WIN.fill(BLACK)
        draw_objects()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False

        # Keep track of keys pressed
        keys = pygame.key.get_pressed()

        # Left Cursor Keys
        if keys[pygame.K_w] and LEFT_Y > 10:
            LEFT_Y -= VELD
        if keys[pygame.K_s] and LEFT_Y < 590 - C_HEIGHT:
            LEFT_Y += VELD

        # Right Cursor Keys
        if keys[pygame.K_i] and RIGHT_Y > 10:
            RIGHT_Y -= VELD
        if keys[pygame.K_k] and RIGHT_Y < 590 - C_HEIGHT:
            RIGHT_Y += VELD

        # Setting ball movement speed
        BALL1_X += ball1_speed_x
        BALL1_Y += ball1_speed_y

        BALL2_X += ball2_speed_x
        BALL2_Y += ball2_speed_y

        # Drawing on-screen objects
        left_cursor = pygame.draw.rect(WIN, WHITE, (LEFT_X, LEFT_Y, C_WIDTH, C_HEIGHT))
        right_cursor = pygame.draw.rect(WIN, WHITE, (RIGHT_X, RIGHT_Y, C_WIDTH, C_HEIGHT))
        ball1 = pygame.draw.circle(WIN, (WHITE), [BALL1_X, BALL1_Y], 15, 0)
        ball2 = pygame.draw.circle(WIN, (WHITE), [BALL2_X, BALL2_Y], 15, 0)

        # Left Cursor bounce mechanics
        if ball1.collidepoint(left_cursor.topright):
            ball1_speed_x *= -1
            ball1_speed_y *= -1
            HIT.play()
        if ball1.collidepoint(left_cursor.bottomright):
            ball1_speed_x *= -1
            ball1_speed_y *= -1
            HIT.play()
        elif left_cursor.colliderect(ball1) and not ball1.collidepoint(left_cursor.topright) or ball1.collidepoint(left_cursor.bottomright):
            ball1_speed_x *= -1
            HIT.play()

        if ball2.collidepoint(left_cursor.topright):
            ball2_speed_x *= -1
            ball2_speed_y *= -1
            HIT.play()
        if ball2.collidepoint(left_cursor.bottomright):
            ball2_speed_x *= -1
            ball2_speed_y *= -1
            HIT.play()
        elif left_cursor.colliderect(ball2) and not ball2.collidepoint(left_cursor.topright) or ball2.collidepoint(left_cursor.bottomright):
            ball2_speed_x *= -1
            HIT.play()

        # Right Cursor bounce mechanics
        if ball1.collidepoint(right_cursor.topleft):
            ball1_speed_x *= -1
            ball1_speed_y *= -1
            HIT.play()
        if ball1.collidepoint(right_cursor.bottomleft):
            ball1_speed_x *= -1
            ball1_speed_y *= -1
            HIT.play()
        elif right_cursor.colliderect(ball1) and not ball1.collidepoint(right_cursor.topleft) or ball1.collidepoint(right_cursor.bottomleft):
            ball1_speed_x *= -1
            HIT.play()

        if ball2.collidepoint(right_cursor.topleft):
            ball2_speed_x *= -1
            ball2_speed_y *= -1
            HIT.play()
        if ball2.collidepoint(right_cursor.bottomleft):
            ball2_speed_x *= -1
            ball2_speed_y *= -1
            HIT.play()
        elif right_cursor.colliderect(ball2) and not ball2.collidepoint(right_cursor.topleft) or ball2.collidepoint(right_cursor.bottomleft):
            ball2_speed_x *= -1
            HIT.play()

        # Ball re-appear and add score for sides + delay
        if BALL1_X < 10:
            sleep(0.5)
            BALL1_X = 400
            BALL1_Y = 300
            BALL2_X = 400
            BALL2_Y = 200
            ball1_speed_x = -10
            ball1_speed_y = 10
            ball2_speed_x = 10
            ball2_speed_y = -10
            pointsp2 += 1
            SCORE.play()
        if BALL1_X > 790:
            sleep(0.5)
            BALL1_X = 400
            BALL1_Y = 300
            BALL2_X = 400
            BALL2_Y = 200
            ball1_speed_x = -10
            ball1_speed_y = 10
            ball2_speed_x = 10
            ball2_speed_y = -10
            pointsp1 += 1
            SCORE.play()

        if BALL2_X < 10:
            sleep(0.5)
            BALL1_X = 400
            BALL1_Y = 300
            BALL2_X = 400
            BALL2_Y = 200
            ball1_speed_x = -10
            ball1_speed_y = 10
            ball2_speed_x = 10
            ball2_speed_y = -10
            pointsp2 += 1
            SCORE.play()
        if BALL2_X > 790:
            sleep(0.5)
            BALL1_X = 400
            BALL1_Y = 300
            BALL2_X = 400
            BALL2_Y = 200
            ball1_speed_x = -10
            ball1_speed_y = 10
            ball2_speed_x = 10
            ball2_speed_y = -10
            pointsp1 += 1
            SCORE.play()

        # Ball top/bottom bounce mechanics
        if BALL1_Y < 10:
            ball1_speed_y *= -1
        if BALL1_Y > 590:
            ball1_speed_y *= -1

        if BALL2_Y < 10:
            ball2_speed_y *= -1
        if BALL2_Y > 590:
            ball2_speed_y *= -1

        # Scoreboard Text
        SCORE_FONT = pygame.font.SysFont('impact', 50)
        P1_SCORE = SCORE_FONT.render(
            (str(pointsp1)), 1, WHITE)
        P2_SCORE = SCORE_FONT.render(
            (str(pointsp2)), 1, WHITE)

        # Score Display
        WIN.blit(P1_SCORE, (330, 10))
        WIN.blit(P2_SCORE, (445, 10))

        # End game at x points
        winner_text = ""
        if pointsp1 == 25:
            winner_text = "Player 1 Wins!"

        if pointsp2 == 25:
            winner_text = "Player 2 Wins!"

        if winner_text != "":
            end_game(winner_text)
            break

        # Update screen display
        pygame.display.update()