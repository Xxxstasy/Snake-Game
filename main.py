from random import randint
import pygame
from pygame.locals import *
import time
from pygame import key
from copy import copy
import keyboard
import os
pygame.init()
EMPT=' '
WALL='#'
YABLOKO='$'
ZMEYA='@'
snake_direction='right'
game_over=False
score=0
score_old=score
x=0.1
pole=[
[WALL,WALL,WALL,WALL,WALL,WALL,WALL,WALL,WALL,WALL,WALL,WALL,WALL,WALL,WALL,WALL,WALL,WALL,WALL,WALL],
[WALL,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,WALL],
[WALL,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,WALL],
[WALL,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,WALL],
[WALL,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,WALL],
[WALL,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,WALL],
[WALL,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,WALL],
[WALL,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,WALL],
[WALL,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,WALL],
[WALL,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,WALL],
[WALL,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,WALL],
[WALL,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,WALL],
[WALL,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,WALL],
[WALL,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,WALL],
[WALL,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,WALL],
[WALL,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,WALL],
[WALL,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,WALL],
[WALL,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,WALL],
[WALL,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,EMPT,WALL],
[WALL,WALL,WALL,WALL,WALL,WALL,WALL,WALL,WALL,WALL,WALL,WALL,WALL,WALL,WALL,WALL,WALL,WALL,WALL,WALL]
]
with open('pole_zmeika.txt') as field:
    for line in field:
        line=line.strip()
apple=[randint(minl,maxl),randint(minc,maxc)]
snake=[[10,10],[10,11],[10,12]]
vivod=[list(range(20))for i in range(20)]
def vivod_polya(pole,vivod):
    for i in range(len(pole)):
        for j in range(len(pole[i])):
            vivod[i][j]=pole[i][j]
def vivod_yabloko(apple,vivod):
    vivod[apple[0]][apple[1]]=YABLOKO
def vivod_zmeya(snake,vivod):
    for i in range(len(snake)):
        vivod[snake[i][0]][snake[i][1]]=ZMEYA
def move_up(e):
    global snake_direction
    if snake_direction!='down':
        snake_direction='up'
keyboard.on_press_key('w',move_up)
def move_down(e):
    global snake_direction
    if snake_direction!='up':
        snake_direction='down'
keyboard.on_press_key('s',move_down)
def move_right(e):
    global snake_direction
    if snake_direction!='left':
        snake_direction='right'
keyboard.on_press_key('d',move_right)
def move_left(e):
    global snake_direction
    if snake_direction!='right':
        snake_direction='left'
keyboard.on_press_key('a',move_left)
clear = lambda: os.system('cls')
slovar={'up':[-1,0],'down':[1,0],'left':[0,-1],'right':[0,1]}
def check_apple_v_zmee(snake,apple):
    for i in range(len(snake)):
        if apple == snake[i]:
            return True
    return False
def gen_apple(apple):
    while pole[apple[0]][apple[1]]!=EMPT or check_apple_v_zmee(snake,apple)==True:
        apple[0] = randint(minl, maxl)
        apple[1] = randint(minc, maxc)
def move_snake(snake_direction, snake, apple):
    global score, minl, maxl, minc, maxc
    sl = [0, 0]
    sl[0] = slovar[snake_direction][0] + snake[-1][0]
    sl[1] = slovar[snake_direction][1] + snake[-1][1]
    if sl[0] < minl:
        sl[0] = maxl
    elif sl[0] > maxl:
        sl[0] = minl
    elif sl[1] < minc:
        sl[1] = maxc
    elif sl[1] > maxc:
        sl[1] = minc
    if sl == apple:
        snake.append(sl.copy())
        score += 1
        gen_apple(apple)
    else:
        for i in range(len(snake) - 1):
            snake[i] = copy(snake[i + 1])
        snake[-1] = sl.copy()
def check_game_over(snake):
    for i in range(len(snake)-1):
        if snake[-1]==snake[i]:
            return True
    if pole[snake[-1][0]][snake[-1][1]]==WALL:
        return True
    return False
gen_apple(apple)
def check_yskorenie(score):
    global score_old,x
    if score_old==score-20:
        score_old=score
        x=x-0.02
while check_game_over(snake)==False:
    time.sleep(x)
    move_snake(snake_direction,snake,apple)
    vivod_polya(pole, vivod)
    vivod_yabloko(apple, vivod)
    vivod_zmeya(snake, vivod)
    check_yskorenie(score)
    clear()
    for i in vivod:
        print(' '.join(i))

print('Your score is ', score)