import pygame
import button
import sys

from time import sleep

pygame.init()

# Cursors
C_WIDTH = 18
C_HEIGHT = 100
VEL = 15  # Cursor Speed

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
MULT_BUTTON = button.Button(200, 200, button.BUTTON_TEXT)

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

# Main Menu Loop
def main_menu():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        WIN.fill(BLACK)
        WIN.blit(TITLE_TEXT, (290, 50))
        MULT_BUTTON.draw(WIN)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()

        if MULT_BUTTON.draw(WIN):
            game_loop_mult()


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
        ball = pygame.draw.circle(WIN, (WHITE), [BALL_X, BALL_Y], 15, 0)

        # Cursor bounce mechanics
        if left_cursor.colliderect(ball):
            ball_speed_x *= -1
        if right_cursor.colliderect(ball):
            ball_speed_x *= -1

        # Ball re-appear and add score for sides + delay
        if BALL_X < 10:
            sleep(0.5)
            BALL_X = 400
            BALL_Y = 300
            pointsp2 += 1
        if BALL_X > 790:
            sleep(0.5)
            BALL_X = 400
            BALL_Y = 300
            pointsp1 += 1

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


if __name__ == "__main__":
    main_menu()