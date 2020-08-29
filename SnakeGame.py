import pygame
import time
import random
pygame.init()
clock = pygame.time.Clock()
#color we are going to use
snakecolor = (0, 76, 155)
boardcolor = (255, 255, 255)
scorecolor = (102, 0, 204)
foodcolor = (255, 123, 7)
restartcolor = (102, 102, 255)

#window Size and Title
display_width = 600
display_height = 400
dis = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('The Snake Game')

#snake Speed and Size
snake_block = 10
snake_speed = 15
snake_list = []

#snake Shape and Position
def snake(snake_block,snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, snakecolor, [x[0], x[1], snake_block, snake_block])
        
        
def snakegame():
    game_ended = False
    game_over = False
    #co-ordinators
    x1 = round(display_width / 2)
    y1 = round(display_height / 2)
    #when snake moves
    x1_new = 0
    y1_new = 0
    
    #length of snake
    snake_list = []
    snake_length = 1
    
    #co-ordinate of food
    xfood = round(random.randrange(0, display_width - snake_block) / 10) * 10
    yfood = round(random.randrange(0, display_height - snake_block) / 10) * 10
    while not game_ended:
        while game_over == True:
            dis.fill(boardcolor)
            font_style = pygame.font.SysFont('arial', 25)
            msg = font_style.render('GAME OVER (Press Space to Restart)', True, restartcolor)
            dis.blit(msg, [display_width / 6, display_height / 3])
            #for displaying the score
            score = snake_length - 1
            score_font = pygame.font.SysFont('arial', 35)
            value = score_font.render('SCORE: '+str(score), True, scorecolor)
            dis.blit(value, [display_width / 3, display_height / 5])
            pygame.display.update()
            #to restart the game
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE: #uses spacebar to restart the game
                        snakegame()
                if event.type == pygame.QUIT:
                    game_ended = True # window open
                    game_over = False # only ends the game
                    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_ended = True
            # keyboard key function for snake movements
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x1_new = round(-snake_block) #uses left arrow key to move snake to the left
                        y1_new = 0
                    elif event.key == pygame.K_RIGHT:
                        x1_new = round(snake_block) #uses rigt arrow key to move snake to the right
                        y1_new = 0
                    elif event.key == pygame.K_UP:
                        x1_new = 0
                        y1_new = round(-snake_block) #uses up arrow key to move snake to the up
                    elif event.key == pygame.K_DOWN:
                        x1_new = 0
                        y1_new = round(snake_block) #uses down arrow key to move snake to the down
                        
        if x1 >= display_width or x1 < 0 or y1 >= display_height or y1 < 0:
            game_over = True
        # update co-ordiantes with new position
        x1 += x1_new
        y1 += y1_new
        dis.fill(boardcolor)
        pygame.draw.rect(dis, foodcolor, [xfood, yfood, snake_block, snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        # when sanke length exceeds,  delete the snake_list which will be game over
        if len(snake_list) > snake_length:
            del snake_list[0]
        #even if snake hits itself, game ends
        for x in snake_list[:-1]:
            if x == snake_head:
                game_over = True
        snake(snake_block, snake_list)
        pygame.display.update()
        if x1 == xfood and y1 == yfood:
            xfood = round(random.randrange(0, display_width - snake_block) / 10) * 10
            yfood = round(random.randrange(0, display_height - snake_block) / 10) * 10
            snake_length += 1
        clock.tick(snake_speed)
    pygame.quit()
    quit()
    
snakegame()