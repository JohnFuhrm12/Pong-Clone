import pygame
import os

pygame.init()

# Sounds
MENU_SELECT = pygame.mixer.Sound('Assets/menuselect.mp3')

# Button Images
SINGLE_BUTTON_TEXT = pygame.transform.scale(pygame.image.load(
                os.path.join("Assets", "singleplayer1.png")), (400, 100))
MULT_BUTTON_TEXT = pygame.transform.scale(pygame.image.load(
                os.path.join("Assets", "mult1.png")), (400, 100))
CLASSIC_BUTTON_TEXT = pygame.transform.scale(pygame.image.load(
                os.path.join("Assets", "classic1.png")), (300, 100))
BLITZ_BUTTON_TEXT = pygame.transform.scale(pygame.image.load(
                os.path.join("Assets", "blitz1.png")), (280, 80))
DOUBLE_BUTTON_TEXT = pygame.transform.scale(pygame.image.load(
                os.path.join("Assets", "double1.png")), (300, 100))

# Screen Variables
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# RGB Colors
WHITE = (255, 255, 255)

class SingleButton:
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
                os.path.join("Assets", "singleplayer2.png")), (400, 100))
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
                MENU_SELECT.play()

        if not self.rect.collidepoint(pos):
            self.image = pygame.transform.scale(pygame.image.load(
                os.path.join("Assets", "singleplayer1.png")), (400, 100))

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        surface.blit(self.image, (self.rect.x, self.rect.y))
        return action

class MultButton:
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

class ClassicButton:
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
                os.path.join("Assets", "classic2.png")), (300, 100))
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
                MENU_SELECT.play()

        if not self.rect.collidepoint(pos):
            self.image = pygame.transform.scale(pygame.image.load(
                os.path.join("Assets", "classic1.png")), (300, 100))

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        surface.blit(self.image, (self.rect.x, self.rect.y))
        return action

class BlitzButton:
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
                os.path.join("Assets", "blitz2.png")), (280, 80))
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
                MENU_SELECT.play()

        if not self.rect.collidepoint(pos):
            self.image = pygame.transform.scale(pygame.image.load(
                os.path.join("Assets", "blitz1.png")), (280, 80))

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        surface.blit(self.image, (self.rect.x, self.rect.y))
        return action

class DoubleButton:
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
                os.path.join("Assets", "double2.png")), (300, 100))
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
                MENU_SELECT.play()

        if not self.rect.collidepoint(pos):
            self.image = pygame.transform.scale(pygame.image.load(
                os.path.join("Assets", "double1.png")), (300, 100))

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        surface.blit(self.image, (self.rect.x, self.rect.y))
        return action