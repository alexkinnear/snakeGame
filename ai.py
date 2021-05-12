import pygame
from math import sqrt
from copy import deepcopy
import main


def distance(snake, food):
    return abs(sqrt((snake.head.x - food.x) ** 2 + (snake.head.y - food.y) ** 2))


class AI:
    def __init__(self, screen, clock, snake, food, width, height):
        self.screen = screen
        self.clock = clock
        self.snake = snake
        self.food = food
        self.board_width = width
        self.board_height = height

    # returns [left, right, up, down] array for both death in each direction as well as closest to food
    def get_state(self, width, height):
        death = []
        food = []
        snake_copy = deepcopy(self.snake)
        self.snake.head.x -= self.snake.width
        death.append(self.snake.is_dead(width, height))
        food.append(distance(self.snake, self.food) < distance(snake_copy, self.food))
        self.snake.head.x += 2 * self.snake.width
        death.append(self.snake.is_dead(width, height))
        food.append(distance(self.snake, self.food) < distance(snake_copy, self.food))
        self.snake.head.x -= self.snake.width
        self.snake.head.y -= self.snake.height
        death.append(self.snake.is_dead(width, height))
        food.append(distance(self.snake, self.food) < distance(snake_copy, self.food))
        self.snake.head.y += 2 * self.snake.height
        death.append(self.snake.is_dead(width, height))
        food.append(distance(self.snake, self.food) < distance(snake_copy, self.food))
        self.snake = snake_copy
        return death, food

    def run(self):
        running = True
        while running:
            temp = deepcopy(self.snake.blocks)
            for i in range(1, len(self.snake.blocks)):
                self.snake.blocks[i].x = temp[i - 1].x
                self.snake.blocks[i].y = temp[i - 1].y

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.snake.vel += 10
                    if event.key == pygame.K_DOWN:
                        if self.snake.vel >= 11:
                            self.snake.vel -= 10

            state = self.get_state(self.board_width, self.board_height)
            next_move = 0
            if True in state[1]:
                next_move = state[1].index(True)
            if state[0][next_move]:
                if True in state[1][next_move:]:
                    next_move = state[1][next_move:].index(True)
                    if state[0][next_move]:
                        if False in state[0]:
                            next_move = state[0].index(False)
                        else:
                            main.main_menu()
            self.snake.dx = self.snake.dy = 0
            if next_move == 0:
                self.snake.dx = -self.snake.width
            elif next_move == 1:
                self.snake.dx = self.snake.width
            elif next_move == 2:
                self.snake.dy = -self.snake.height
            else:
                self.snake.dy = self.snake.height

            self.snake.head.x += self.snake.dx
            self.snake.head.y += self.snake.dy

            self.screen.fill((255, 255, 255))
            pygame.draw.rect(self.screen, self.food.color,
                             [self.food.x, self.food.y, self.snake.width, self.snake.height])
            self.snake.draw_snake(self.screen)
            main.display_msg(f'Score: {len(self.snake.blocks) - 1}', (0, 0, 0), (0, 0))
            pygame.display.flip()
            self.clock.tick(self.snake.vel)

            running = not self.snake.is_dead(self.board_width, self.board_height)

            # Check if eating food
            if self.snake.head.x == self.food.x and self.snake.head.y == self.food.y:
                self.food.get_new_pos(self.board_width, self.board_height, self.snake)
                self.snake.add_block()

        main.main_menu()
