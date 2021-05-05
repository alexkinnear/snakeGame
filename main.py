import pygame
from copy import deepcopy
from snake import Snake, Food

pygame.init()

WIDTH, HEIGHT = 400, 400
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
CLOCK = pygame.time.Clock()
SCORE_FONT = pygame.font.SysFont("arial", 25)

snake = Snake()
food = Food()


def __init_window():
    pygame.display.set_caption('Snake Game')
    background_colour = (255, 255, 255)
    SCREEN.fill(background_colour)


def draw_snake():
    for block in snake.blocks:
        pygame.draw.rect(SCREEN, snake.color, [block.x, block.y, snake.width, snake.height])


def draw_score():
    score = SCORE_FONT.render(f"Score: {len(snake.blocks)-1}", True, (0, 0, 0))
    SCREEN.blit(score, [0, 0])


if __name__ == "__main__":
    __init_window()

    running = True
    while running:
        temp = deepcopy(snake.blocks)
        for i in range(1, len(snake.blocks)):
            snake.blocks[i].x = temp[i - 1].x
            snake.blocks[i].y = temp[i - 1].y

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                keyPressed = True
                if event.key == pygame.K_LEFT:
                    snake.head.dx = -snake.width
                    snake.head.dy = 0
                elif event.key == pygame.K_RIGHT:
                    snake.head.dx = snake.width
                    snake.head.dy = 0
                elif event.key == pygame.K_UP:
                    snake.head.dx = 0
                    snake.head.dy = -snake.height
                elif event.key == pygame.K_DOWN:
                    snake.head.dx = 0
                    snake.head.dy = snake.height

        snake.head.x += snake.head.dx
        snake.head.y += snake.head.dy

        SCREEN.fill((255, 255, 255))
        pygame.draw.rect(SCREEN, food.color, [food.x, food.y, snake.width, snake.height])
        draw_snake()
        draw_score()
        pygame.display.flip()
        CLOCK.tick(snake.vel)

        running = not snake.is_dead(WIDTH, HEIGHT)

        # Check if eating food
        if snake.head.x == food.x and snake.head.y == food.y:
            food.get_new_pos(WIDTH, HEIGHT, snake)
            snake.add_block()
