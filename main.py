import pygame
import random
import sys
from settings import WINDOW_SIZE, BOARD_WIDTH, BOARD_HEIGHT, MAIN_COLORS, GAME_COLORS, CELL_SIZE


class MatchThree:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Match Three Game')

        self.screen = pygame.display.set_mode(WINDOW_SIZE)
        self.board = list()
        self.selected = None
        self.moves = 0

        for row in range(BOARD_HEIGHT):
            new_row = []
            for col in range(BOARD_WIDTH):
                new_row.append(random.choice(list(GAME_COLORS.values())))
            self.board.append(new_row)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    i, j = self.get_cell(event.pos)
                    self.change_chars(i, j)

            self.screen.fill(MAIN_COLORS['black'])

            for row in range(BOARD_HEIGHT):
                for col in range(BOARD_WIDTH):
                    color = self.board[row][col]
                    if self.selected and (self.selected[0] == row and self.selected[1] == col):
                        radius = CELL_SIZE // 2
                    else:
                        radius = CELL_SIZE // 2 - 2

                    pygame.draw.circle(
                        surface=self.screen,
                        color=color,
                        center=(
                            col * CELL_SIZE + CELL_SIZE // 2,
                            row * CELL_SIZE + CELL_SIZE // 2
                        ),
                        radius=radius
                    )

            pygame.display.flip()
            self.check_board()

    def change_chars(self, i, j):
        if not self.selected:
            self.selected = (i, j)
        else:
            di, dj = self.selected

            if abs(i - di) + abs(j - dj) > 1 or (i == di and j == dj):
                self.selected = None
            else:
                self.board[i][j], self.board[di][dj] = self.board[di][dj], self.board[i][j]
                self.selected = None
                self.moves += 1

    def get_cell(self, pos):
        x, y = pos
        j = x // CELL_SIZE
        i = y // CELL_SIZE
        return i, j

    def check_neighbours(self, row, col):
        x, y = row, col

        gem = self.board[x][y]
        try:
            if self.board[x + 1][y] == gem and self.board[x - 1][y] == gem:
                self.board[x - 1][y] = MAIN_COLORS['black']
                self.board[x + 1][y] = MAIN_COLORS['black']
                self.board[x][y] = MAIN_COLORS['black']

            elif self.board[x][y + 1] == gem and self.board[x][y - 1] == gem:
                self.board[x][y - 1] = MAIN_COLORS['black']
                self.board[x][y + 1] = MAIN_COLORS['black']
                self.board[x][y] = MAIN_COLORS['black']

        except Exception as ex:
            pass
    # Вот блять эта темка для проверни на продрял чтобы по строчке и не ебаться с соседями
    # Надо бы
    # def transposed(self, matrix):
    #     return [[*col] for col in zip(*matrix)]
    #
    # def rot90(self, matrix):
    #     return list(map(reversed, self.transposed(matrix)))

    def check_board(self):
        for j, row in enumerate(self.board):
            for i, col in enumerate(row):
                if self.check_neighbours(i, j):
                    pass


if __name__ == '__main__':
    game = MatchThree()
    game.run()
