from random import randint


class Snake:
    def __init__(self):
        self.width, self.height = 25, 25
        self.vel = 15
        self.color = (0, 255, 0)
        self.blocks = [Block(300, 250, 0, 0)]
        self.head = self.blocks[0]

    def add_block(self):
        self.blocks.append(Block(0, 0, 0, 0))

    def is_dead(self, width, height):
        if not (0 <= self.head.x < width and 0 <= self.head.y < height):
            return True
        for i in range(1, len(self.blocks)):
            if self.head.x == self.blocks[i].x and self.head.y == self.blocks[i].y:
                return True
        return False


class Block:
    def __init__(self, x, y, dx, dy):
        self.x, self.y = x, y
        self.dx, self.dy = dx, dy


class Food:
    def __init__(self):
        self.x, self.y = 0, 0
        self.get_new_pos(100, 100, Snake())
        self.color = (255, 0, 0)

    def get_new_pos(self, width, height, snake):
        valid_pos = False
        while not valid_pos:
            x, y = randint(0, width - snake.width), randint(0, height - snake.height)
            while not x % 25 == 0:
                x += 1
            while not y % 25 == 0:
                y += 1
            results = []
            for block in snake.blocks:
                if not block.x == x and block.y == y:
                    results.append(True)
            if not False in results:
                valid_pos = True
                self.x, self.y = x, y
