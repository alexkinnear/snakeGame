import pygame
from copy import deepcopy
import main


def hamiltonian_cycle(screen, clock, snake, food, width, height):
    running = True
    while running:
        temp = deepcopy(snake.blocks)
        for i in range(1, len(snake.blocks)):
            snake.blocks[i].x = temp[i - 1].x
            snake.blocks[i].y = temp[i - 1].y

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.vel += 10
                if event.key == pygame.K_DOWN:
                    if snake.vel >= 11:
                        snake.vel -= 10

        if snake.head.x == snake.width and snake.head.y == 0:
            snake.dx = -snake.width
            snake.dy = 0
        elif snake.head.x == 0 and snake.head.y < height - snake.height:
            snake.dx = 0
            snake.dy = snake.height
        elif snake.head.y % 2 == 0 and snake.head.x > snake.width:
            snake.dx = -snake.width
            snake.dy = 0
        elif snake.head.y % 2 == 0 and snake.head.x <= snake.width and snake.head.y > 0:
            snake.dx = 0
            snake.dy = -snake.height
        elif snake.head.y % 2 == 1 and snake.head.x < width - snake.width:
            snake.dx = snake.width
            snake.dy = 0
        elif snake.head.y % 2 == 1 and snake.head.x >= width - snake.width:
            snake.dx = 0
            snake.dy = -snake.width

        else:
            snake.dy = 0
            snake.dx = 0
        snake.head.x += snake.dx
        snake.head.y += snake.dy

        screen.fill((255, 255, 255))
        pygame.draw.rect(screen, food.color, [food.x, food.y, snake.width, snake.height])
        snake.draw_snake(screen)
        main.display_msg(f'Score: {len(snake.blocks) - 1}', (0, 0, 0), (0, 0))
        pygame.display.flip()
        clock.tick(snake.vel)

        running = not snake.is_dead(width, height)

        # Check if eating food
        if snake.head.x == food.x and snake.head.y == food.y:
            food.get_new_pos(width, height, snake)
            snake.add_block()

    main.main_menu()