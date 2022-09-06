import pygame
import time
import random

pygame.init()

dis_width, dis_height = 800, 600
dis = pygame.display.set_mode((dis_width,dis_height))
pygame.display.update()
pygame.display.set_caption("Snake Game")

black = (255, 255, 255)
white = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 102)

snake_block = 10
speed = 10

clock = pygame.time.Clock()
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicssansms",35)

def message(msg, color):
    mesg = font_style.render(msg,True,color)
    dis.blit(mesg,[dis_width/6,dis_height/2])

def display_score(score):
    value = score_font.render("Score : "+str(score),True,yellow)
    dis.blit(value,[0,0])

def display_snake(snake_block,snake_list):
    for x in snake_list:
        pygame.draw.rect(dis,black,[x[0],x[1],snake_block,snake_block])

def gameloop():
    game_over = False
    game_close = False

    snake_list = []
    Length_of_snake = 1

    x1 = dis_width/2
    y1 = dis_height/2

    x1_change = 0
    y1_change = 0

    foodx = round(random.randrange(0,dis_width-snake_block)/snake_block)*snake_block
    foody = round(random.randrange(0,dis_height-snake_block)/snake_block)*snake_block

    while not game_close:

        while game_over:
            dis.fill(white)
            message("You Lost...PRESS Q-QUIT or C-CONTINUE?",red)
            display_score(Length_of_snake-1)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN or event.type == pygame.QUIT:
                    if event.key == pygame.K_q or event.type == pygame.QUIT:
                        game_over = False
                        game_close = True
                    elif event.key == pygame.K_c:
                        gameloop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_close = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_block
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake_block
                elif event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0   

        if x1>dis_width or x1<0 or y1>dis_height or y1<0:
            game_over = True 

        x1 += x1_change
        y1 += y1_change

        dis.fill(white)
        pygame.draw.rect(dis,blue,[foodx,foody,snake_block,snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > Length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:   #Does not loop the last element
            if x ==snake_head:
                game_over = True

        display_snake(snake_block,snake_list)
        display_score(Length_of_snake-1)

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0,dis_width-10)/10.0)*10
            foody = round(random.randrange(0,dis_height-10)/10.0)*10
            Length_of_snake += 1

        pygame.display.update()
        clock.tick(speed)

    pygame.quit()
    quit()

gameloop()

