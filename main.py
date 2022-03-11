import pygame
import button
import sys

pygame.init()

# Cursors
C_WIDTH = 18
C_HEIGHT = 100
VEL = 5

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


# On-Screen Objects
def draw_objects():
    pygame.draw.rect(WIN, WHITE, BORDER)  # Middle Border

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
    LEFT_X = 30
    LEFT_Y = 250

    RIGHT_X = 750
    RIGHT_Y = 250

    BALL_X = 300
    BALL_Y = 300

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

        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] and LEFT_Y > 10:
            LEFT_Y -= VEL
        if keys[pygame.K_s] and LEFT_Y < 590 - C_HEIGHT:
            LEFT_Y += VEL

        if keys[pygame.K_i] and RIGHT_Y > 10:
            RIGHT_Y -= VEL
        if keys[pygame.K_k] and RIGHT_Y < 590 - C_HEIGHT:
            RIGHT_Y += VEL

        BALL_X -= 3

        left_cursor = pygame.draw.rect(WIN, WHITE, (LEFT_X, LEFT_Y, C_WIDTH, C_HEIGHT))
        right_cursor = pygame.draw.rect(WIN, WHITE, (RIGHT_X, RIGHT_Y, C_WIDTH, C_HEIGHT))
        ball = pygame.draw.circle(WIN, (WHITE), [BALL_X, BALL_Y], 15, 0)

        if left_cursor.colliderect(ball):
            BALL_X += 3

        pygame.display.update()


if __name__ == "__main__":
    main_menu()