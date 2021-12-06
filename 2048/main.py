import pygame
from pygame import transform
import os
import Board
import Button

DIMENSION = 4
TILE_SIZE = 100
WIDTH, HEIGHT = 100 * DIMENSION, 100 * DIMENSION
TOTAL_WIDTH, TOTAL_HEIGHT = WIDTH , HEIGHT + 50
SCREEN = pygame.display.set_mode((TOTAL_WIDTH, TOTAL_HEIGHT))
pygame.display.set_caption("2048 by Mehul Gandhi")
LIGHT_YELLOW = (253, 222, 179)
BROWN = [210, 105, 30]
DARK_BROWN = [165, 69, 69]
LIGHT_BROWN = [165, 69, 50]
WHITE = (255, 255, 255)
FPS = 60
TRANSFORM = (WIDTH / 4, HEIGHT / 4)


BLANK = pygame.image.load(os.path.join("assets", "blank.png"))
_2 = pygame.image.load(os.path.join("assets", "2.png"))
_4 = pygame.image.load(os.path.join("assets", "4.png"))
_8 = pygame.image.load(os.path.join("assets", "8.png"))
_16 = pygame.image.load(os.path.join("assets", "16.png"))
_32 = pygame.image.load(os.path.join("assets", "32.png"))
_64 = pygame.image.load(os.path.join("assets", "64.png"))
_128 = pygame.image.load(os.path.join("assets", "128.png"))
_256 = pygame.image.load(os.path.join("assets", "256.png"))
_512 = pygame.image.load(os.path.join("assets", "512.png"))
_1024 = pygame.image.load(os.path.join("assets", "1024.png"))
_2048 = pygame.image.load(os.path.join("assets", "2048.png"))
_4096 = pygame.image.load(os.path.join("assets", "4096.png"))
_8192 = pygame.image.load(os.path.join("assets", "8192.png"))
_16384 = pygame.image.load(os.path.join("assets", "16384.png"))
_32768 = pygame.image.load(os.path.join("assets", "32768.png"))
_65536 = pygame.image.load(os.path.join("assets", "65536.png"))

button = pygame.Rect((TILE_SIZE * DIMENSION) - TILE_SIZE, 0, TILE_SIZE, int(TILE_SIZE /2))

def main():
    clock = pygame.time.Clock()
    run = True
    game = Board.Board(DIMENSION, False)
    game.addTwoOrFour()
    while run:
        clock.tick(FPS)
        draw_window()
        rv = drawGrid(game)
        if rv is not None:
            game = rv
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    game.shift("up")
                elif event.key == pygame.K_DOWN or event.key == pygame.K_d:
                    game.shift("down")
                elif event.key == pygame.K_LEFT or event.key == pygame.K_s:
                    game.shift("left")
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    game.shift("right")
                if game.gameOver():
                    run = False
    pygame.quit()


def draw_window():
    SCREEN.fill(LIGHT_YELLOW)


"""Draws out the 2048 matrix grid."""


def drawGrid(game):
    # for i in range(0, WIDTH, TILE_SIZE):
    #     for j in range(0, HEIGHT, TILE_SIZE):
            # tile = pygame.Rect(i, j, TILE_SIZE, TILE_SIZE)
            # pygame.draw.rect(SCREEN, WHITE, tile, 1)
            # SCREEN.blit(transform.scale(BLANK, TRANSFORM), (i, j))
    a = 0
    b = 0
    for i in range(50, TOTAL_HEIGHT, TILE_SIZE):
        b = 0
        for j in range(0, TOTAL_WIDTH, TILE_SIZE):
            SCREEN.blit(transform.scale(game.board[a][b].path, TRANSFORM), (j, i))
            b += 1
        a += 1
    drawScore(game)
    if Button.newGame.draw_button():
        game = Board.Board(DIMENSION, False)
        game.addTwoOrFour()
        return game

def drawScore(game):
    buttonScore = Button.score
    buttonScore.text = f"Score: {game.score}"
    buttonScore.drawText()


if __name__ == "__main__":
    main()
