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
                if self.update_board():
                    self.board[i][j], self.board[di][dj] = self.board[di][dj], self.board[i][j]
                    self.moves -= 1

    def get_cell(self, pos):
        x, y = pos
        j = x // CELL_SIZE
        i = y // CELL_SIZE
        return i, j

    def transposed(self):
        self.board = [[*col] for col in zip(*self.board)]

    def update_board(self):
        old_board = self.board
        self.checking_compliance()
        self.transposed()
        self.checking_compliance()
        self.transposed()
        return self.board == old_board

    def checking_compliance(self):
        for row in self.board:
            j = 0
            while j < len(row):
                count = 1
                while j + count < len(row) and row[j] == row[j + count]:
                    count += 1
                if count > 2:
                    for k in range(j, j + count):
                        row[k] = MAIN_COLORS['black']
                    j += count
                else:
                    j += 1

    # Надо чета лютое придумать как их вниз двигать

    def move_cells(self):
        pass



if __name__ == '__main__':
    game = MatchThree()
    game.run()
