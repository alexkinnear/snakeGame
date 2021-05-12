import pygame
from random import randint


class Snake:
    def __init__(self):
        self.width, self.height = 25, 25
        self.vel = 15
        self.color = (0, 255, 0)
        self.blocks = [Block(300, 250)]
        self.head = self.blocks[0]
        self.dx, self.dy = 0, 0

    def add_block(self):
        self.blocks.append(Block(0, 0))

    def is_dead(self, width, height):
        if not (0 <= self.head.x < width and 0 <= self.head.y < height):
            return True
        for i in range(1, len(self.blocks)):
            if self.head.x == self.blocks[i].x and self.head.y == self.blocks[i].y:
                return True
        return False

    def draw_snake(self, screen):
        for block in self.blocks:
            pygame.draw.rect(screen, self.color, [block.x, block.y, self.width, self.height])


class Block:
    def __init__(self, x, y):
        self.x, self.y = x, y


class Food:
    def __init__(self):
        self.x, self.y = 0, 0
        self.get_new_pos(400, 400, Snake())
        self.color = (255, 0, 0)

    def get_new_pos(self, width, height, snake):
        valid_pos = False
        while not valid_pos:
            x, y = randint(0, width - snake.width), randint(0, height - snake.height)
            while not x % 25 == 0:
                x += 1
            while not y % 25 == 0:
                y += 1
            result = []
            for block in snake.blocks:
                if x == block.x and y == block.y:
                    result.append(0)
            if len(result) == 0:
                valid_pos = True
                self.x, self.y = x, y
