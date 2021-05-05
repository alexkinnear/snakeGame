from random import randint


class Snake:
    def __init__(self):
        self.width, self.height = 25, 25
        self.vel = 15
        self.color = (0, 255, 0)
        self.blocks = [Block(300, 250, 0, 0)]
        self.head = self.blocks[0]
        self.tail = self.blocks[-1]
        self.length = 1

    def add_block(self):
        if self.tail.dx > 0:
            self.blocks.append(Block(self.tail.x - self.width, self.tail.y, self.tail.dx, self.tail.dy))
        elif self.tail.dx < 0:
            self.blocks.append(Block(self.tail.x + self.width, self.tail.y, self.tail.dx, self.tail.dy))
        elif self.tail.dy > 0:
            self.blocks.append(Block(self.tail.x, self.tail.y - self.height, self.tail.dx, self.tail.dy))
        elif self.tail.dy < 0:
            self.blocks.append(Block(self.tail.x, self.tail.y - self.height, self.tail.dx, self.tail.dy))
        self.length += 1
        self.tail = self.blocks[-1]

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
        self.get_new_pos()
        self.color = (255, 0, 0)

    def get_new_pos(self):
        x, y = randint(0, 575), randint(0, 575)
        while not x % 25 == 0:
            x += 1
        while not y % 25 == 0:
            y += 1
        self.x, self.y = x, y
