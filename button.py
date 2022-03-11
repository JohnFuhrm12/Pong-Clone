import pygame
import os

pygame.init()

# Sounds
MENU_SELECT = pygame.mixer.Sound('Assets/menuselect.mp3')

BUTTON_TEXT = pygame.transform.scale(pygame.image.load(
                os.path.join("Assets", "mult1.png")), (400, 100))

# Screen Variables
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# RGB Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (59, 219, 97)

class Button:
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.hover = False

    def draw(self, surface):
        action = False
        # Get mouse position
        pos = pygame.mouse.get_pos()

        # If hovering over button do something
        if self.rect.collidepoint(pos):
            self.image = pygame.transform.scale(pygame.image.load(
                os.path.join("Assets", "mult2.png")), (400, 100))
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
                MENU_SELECT.play()

        if not self.rect.collidepoint(pos):
            self.image = pygame.transform.scale(pygame.image.load(
                os.path.join("Assets", "mult1.png")), (400, 100))

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        surface.blit(self.image, (self.rect.x, self.rect.y))
        return action
