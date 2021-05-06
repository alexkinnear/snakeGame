import pygame
from copy import deepcopy
from sys import exit
from snake import Snake, Food

pygame.init()

WIDTH, HEIGHT = 600, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
CLOCK = pygame.time.Clock()
FONT = pygame.font.SysFont("arial", 25)


def __init_window():
    pygame.display.set_caption('Snake Game')
    background_colour = (255, 255, 255)
    SCREEN.fill(background_colour)


def draw_snake(snake):
    for block in snake.blocks:
        pygame.draw.rect(SCREEN, snake.color, [block.x, block.y, snake.width, snake.height])


def display_msg(msg, color, pos):
    text = FONT.render(msg, True, color)
    SCREEN.blit(text, pos)


def check_score(snake):
    with open('leaderboard.txt', 'r+') as f:
        high_score = int(f.read())
        if len(snake.blocks) - 1 > high_score:
            f.seek(0)
            f.write(str(len(snake.blocks) - 1))


def view_leaderboard():
    high_score = ''
    with open('leaderboard.txt') as f:
        high_score = f.read()

    viewing = True
    while viewing:
        SCREEN.fill((255, 255, 255))
        display_msg(f'High Score {high_score}', (0, 0, 0), (WIDTH / 3, HEIGHT / 4))
        display_msg('e - Back to Main Menu', (0, 0, 0), (WIDTH / 3, HEIGHT / 2))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    exit()
                elif event.key == pygame.K_e:
                    main_menu()
                    viewing = False



def main_menu():
    choosing = True
    while choosing:
        SCREEN.fill((255, 255, 255))
        display_msg("Classic Snake Game", (0, 0, 0), (WIDTH / 3.2, HEIGHT / 5))
        display_msg("p - Play", (0, 0, 0), (WIDTH / 2.8, HEIGHT / 2.3))
        display_msg("w - Watch AI", (0, 0, 0), (WIDTH / 2.8, HEIGHT / 2))
        display_msg("v - View Leaderboard", (0, 0, 0), (WIDTH / 2.8, HEIGHT / 1.75))
        display_msg("q - Quit", (0, 0, 0), (WIDTH / 2.8, HEIGHT / 1.5))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    exit()
                elif event.key == pygame.K_p:
                    play(Snake(), Food())
                    choosing = False
                elif event.key == pygame.K_w:
                    hamiltonian_cycle(Snake(), Food())
                    choosing = False
                elif event.key == pygame.K_v:
                    view_leaderboard()
                    choosing = False


def play(snake, food):
    running = True
    while running:
        temp = deepcopy(snake.blocks)
        for i in range(1, len(snake.blocks)):
            snake.blocks[i].x = temp[i - 1].x
            snake.blocks[i].y = temp[i - 1].y

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake.dx = -snake.width
                    snake.dy = 0
                elif event.key == pygame.K_RIGHT:
                    snake.dx = snake.width
                    snake.dy = 0
                elif event.key == pygame.K_UP:
                    snake.dx = 0
                    snake.dy = -snake.height
                elif event.key == pygame.K_DOWN:
                    snake.dx = 0
                    snake.dy = snake.height

        snake.head.x += snake.dx
        snake.head.y += snake.dy

        SCREEN.fill((255, 255, 255))
        pygame.draw.rect(SCREEN, food.color, [food.x, food.y, snake.width, snake.height])
        draw_snake(snake)
        display_msg(f'Score: {len(snake.blocks) - 1}', (0, 0, 0), (0, 0))
        pygame.display.flip()
        CLOCK.tick(snake.vel)

        running = not snake.is_dead(WIDTH, HEIGHT)

        # Check if eating food
        if snake.head.x == food.x and snake.head.y == food.y:
            food.get_new_pos(WIDTH, HEIGHT, snake)
            snake.add_block()

    check_score(snake)
    main_menu()


def hamiltonian_cycle(snake, food):
    running = True
    while running:
        temp = deepcopy(snake.blocks)
        for i in range(1, len(snake.blocks)):
            snake.blocks[i].x = temp[i - 1].x
            snake.blocks[i].y = temp[i - 1].y

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        if snake.head.x == snake.width and snake.head.y == 0:
            snake.dx = -snake.width
            snake.dy = 0
        elif snake.head.x == 0 and snake.head.y < HEIGHT - snake.height:
            snake.dx = 0
            snake.dy = snake.height
        elif snake.head.y % 2 == 0 and snake.head.x > snake.width:
            snake.dx = -snake.width
            snake.dy = 0
        elif snake.head.y % 2 == 0 and snake.head.x <= snake.width and snake.head.y > 0:
            snake.dx = 0
            snake.dy = -snake.height
        elif snake.head.y % 2 == 1 and snake.head.x < WIDTH - snake.width:
            snake.dx = snake.width
            snake.dy = 0
        elif snake.head.y % 2 == 1 and snake.head.x >= WIDTH - snake.width:
            snake.dx = 0
            snake.dy = -snake.width

        else:
            print(3)
            snake.dy = 0
            snake.dx = 0
        snake.head.x += snake.dx
        snake.head.y += snake.dy

        SCREEN.fill((255, 255, 255))
        pygame.draw.rect(SCREEN, food.color, [food.x, food.y, snake.width, snake.height])
        draw_snake(snake)
        display_msg(f'Score: {len(snake.blocks) - 1}', (0, 0, 0), (0, 0))
        pygame.display.flip()
        CLOCK.tick(snake.vel)

        running = not snake.is_dead(WIDTH, HEIGHT)

        # Check if eating food
        if snake.head.x == food.x and snake.head.y == food.y:
            food.get_new_pos(WIDTH, HEIGHT, snake)
            snake.add_block()

    main_menu()


if __name__ == "__main__":
    __init_window()
    main_menu()
