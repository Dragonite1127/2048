import pygame
from pygame.locals import *

pygame.font.init()
clicked = False
font = pygame.font.SysFont("Arial", 30)

WIDTH = 400
HEIGHT = 450
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Button demo")
BROWN = [210, 105, 30]
DARK_BROWN = [165, 69, 69]
WHITE = (255, 255, 255)
LIGHT_BROWN = [165, 69, 50]
BLACK = [0, 0, 0]

class Button():
    # colours for button and text
    button_col = LIGHT_BROWN
    hover_col = BROWN
    click_col = DARK_BROWN
    text_col = WHITE
    width = 150
    height = 50

    def __init__(self, x, y, text):
        self.x = x
        self.y = y
        self.text = text

    def draw_button(self):

        global clicked
        action = False

        # get mouse position
        pos = pygame.mouse.get_pos()

        # create pygame Rect object for the button
        button_rect = Rect(self.x, self.y, self.width, self.height)

        # check mouseover and clicked conditions
        if button_rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                clicked = True
                pygame.draw.rect(SCREEN, self.click_col, button_rect)
            elif pygame.mouse.get_pressed()[0] == 0 and clicked:
                clicked = False
                action = True
            else:
                pygame.draw.rect(SCREEN, self.hover_col, button_rect)
        else:
            pygame.draw.rect(SCREEN, self.button_col, button_rect)

        # add shading to button
        pygame.draw.line(SCREEN, WHITE, (self.x, self.y), (self.x + self.width, self.y), 2)
        pygame.draw.line(SCREEN, WHITE, (self.x, self.y), (self.x, self.y + self.height), 2)
        pygame.draw.line(SCREEN, BLACK, (self.x, self.y + self.height), (self.x + self.width, self.y + self.height), 2)
        pygame.draw.line(SCREEN, BLACK, (self.x + self.width, self.y), (self.x + self.width, self.y + self.height), 2)

        # add text to button
        text_img = font.render(self.text, True, self.text_col)
        text_len = text_img.get_width()
        SCREEN.blit(text_img, (self.x + 20, self.y))
        return action

    """A function that draws a rectangular button and text. Has no clicking capabilities."""
    def drawText(self):
        button_rect = Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(SCREEN, BROWN, button_rect)

        pygame.draw.line(SCREEN, WHITE, (self.x, self.y), (self.x + self.width, self.y), 2)
        pygame.draw.line(SCREEN, WHITE, (self.x, self.y), (self.x, self.y + self.height), 2)
        pygame.draw.line(SCREEN, BLACK, (self.x, self.y + self.height), (self.x + self.width, self.y + self.height), 2)
        pygame.draw.line(SCREEN, BLACK, (self.x + self.width, self.y), (self.x + self.width, self.y + self.height), 2)

        text_img = font.render(self.text, True, WHITE)

        SCREEN.blit(text_img, (20, self.y))


newGame = Button(250, 0, 'New Game')
score = Button(0, 0, 'Score')
# down = Button(75, 350, 'Down')
# up = Button(325, 350, 'Up')
