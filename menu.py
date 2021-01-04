#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 15:04:33 2020

@author: nathan
"""

import pygame
from pong4 import *
from math import inf
import time


 
# Setup pygame/window ---------------------------------------- #
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('PONG')
screen = pygame.display.set_mode((1000, 600),0,32)
 
font = pygame.font.SysFont(None, 50)
font2= pygame.font.SysFont(None,100)
font3 = pygame.font.SysFont(None,30)

black = (0,0,0)
white = (255,255,255)



    
 
click = False
 
def main_menu():
    ball_speed=300
    paddle_speed=300
    ball_width=10
    paddle_height=100
    winning_points=11
    button_color = white
    text_color = black
    where = 0
    

    while True:
 
        screen.fill((0,0,0))
        draw_text('PONG', font2, (255, 255, 255), screen, 400, 70)
 
        mx, my = pygame.mouse.get_pos()
 
        button_1 = pygame.Rect(420, 240, 180, 60)
        button_2 = pygame.Rect(420, 340, 180, 60)

        if button_1.collidepoint((mx, my)):
            button_color = white
            text_color = black
            if click:
                game(ball_speed,paddle_speed,ball_width,paddle_height,winning_points)
        if button_2.collidepoint((mx, my)):
            button_color = black
            text_color = white
            if click:
                ball_speed,paddle_speed,ball_width,paddle_height,winning_points=options(ball_speed,paddle_speed,ball_width,paddle_height,winning_points)
                
        pygame.draw.rect(screen, button_color, button_1)
        pygame.draw.rect(screen, text_color, button_2)
        draw_text('PLAY', font, text_color,screen,460,250)
        draw_text('OPTIONS', font, button_color,screen,430,350)
 
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    return
                if event.key == K_DOWN:
                    button_color = black
                    text_color = white
                    where = 1
                if event.key == K_UP:
                    button_color = white
                    text_color = black
                    where = 0
                if event.key == K_RETURN:
                    if where == 0 :
                        game(ball_speed,paddle_speed,ball_width,paddle_height,winning_points)
                    if where == 1 :
                        ball_speed,paddle_speed,ball_width,paddle_height,winning_points=options(ball_speed,paddle_speed,ball_width,paddle_height,winning_points)
                        
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.update()
        mainClock.tick(60)
 
def game(ball_speed,paddle_speed,ball_width,paddle_height,winning_points):
    play=False
    running = True
    where = 0
    j1 = 0
    j2 = 0
    button_color1 = white
    button_color2 = black
    button_color3 = black
    button_color4 = black
    button_color5 = black
    text_color1 = black
    text_color2 = white
    text_color3 = white
    text_color4 = white
    text_color5 = white
    while running:
        screen.fill((0,0,0))
        

        button_1 = pygame.Rect(50, 250, 180, 40)
        button_2 = pygame.Rect(410, 250, 180, 40)
        button_3 = pygame.Rect(770, 250, 180, 40)
        button_4 = pygame.Rect(50, 400, 180, 40)
        button_5 = pygame.Rect(410, 400, 180, 40)
        pygame.draw.rect(screen, button_color1, button_1)
        pygame.draw.rect(screen, button_color2, button_2)
        pygame.draw.rect(screen, button_color3, button_3)
        pygame.draw.rect(screen, button_color4, button_4)
        pygame.draw.rect(screen, button_color5, button_5)
        draw_text('PLAYERS', font2, white, screen, 350, 20)
        draw_text('PLAYER 1', font, white, screen, 420, 200)
        draw_text('PLAYER 2', font, white, screen, 420, 350)
        draw_text('PLAYER', font3, text_color1, screen, 100, 260)
        draw_text('STATIC AI', font3, text_color2, screen, 450, 260)
        draw_text('Q AI', font3, text_color3, screen, 840, 260)
        draw_text('PLAYER', font3, text_color4, screen, 100, 410)
        draw_text('STATIC AI', font3, text_color5, screen, 450, 410)
        
        
        
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                    return
                if event.key == K_RIGHT:
                        
                    if where == 1 :
                        button_color2 = black
                        text_color2 = white
                        button_color3 = white
                        text_color3 = black
                        where = 2   
                    if where == 0 :
                        button_color1 = black
                        text_color1 = white
                        button_color2 = white
                        text_color2 = black
                        where = 1
                        
                    if where == 3 :
                        button_color4 = black
                        text_color4 = white
                        button_color5 = white
                        text_color5 = black
                        where = 4

                if event.key == K_LEFT:
                    if where == 1 :
                        button_color1 = white
                        text_color1 = black
                        button_color2 = black
                        text_color2 = white
                        where = 0
                    if where == 2 :
                        button_color2 = white
                        text_color2 = black
                        button_color3 = black
                        text_color3 = white
                        where = 1
                    if where == 4 :
                        button_color4 = white
                        text_color4 = black
                        button_color5 = black
                        text_color5 = white
                        where = 3

                        
                if event.key == K_RETURN:
                    if where == 3 :
                        j2=0
                        play=True
                    if where == 4 :
                        j2=1
                        play=True
                    if 0<=where<3 :
                        if where == 0 :
                            j1 = 0
                        if where == 1:
                            j1 = 1
                        if where == 2:
                            j1 = 2
                        where = 3
                        text_color1 = white
                        text_color2 = white
                        text_color3 = white
                        button_color1 = black
                        button_color2 = black
                        button_color3 = black
                        text_color4 = black
                        button_color4 = white
                    while play:
                        pong = Pong(j1,j2,ball_speed,paddle_speed,ball_width,paddle_height,winning_points)
                        while pong.SCOREA < winning_points and pong.SCOREB<winning_points:
                            pong.next_step()
                            pygame.event.pump()
                            time.sleep(0.005)
                            for event in pygame.event.get():
                                if event.type == QUIT:
                                    return
                                if event.type == KEYDOWN:
                                    if event.key == K_ESCAPE:
                                        return
                        play=False
                        return
        pygame.display.update()
        mainClock.tick(60)
 
def options(ball_speed,paddle_speed,ball_width,paddle_height,winning_points):
    d=10
    e=350
    f=280
    h=355
    running = True
    where = 0
    button_color1=white
    text_color1=black
    button_color2=black
    text_color2=white
    button_color3=black
    text_color3=white
    button_color4=black
    text_color4=white
    button_color5=black
    text_color5=white
    
    while running:
        screen.fill((0,0,0))
        draw_text('OPTIONS', font2, (255, 255, 255), screen, 350, 20)
        
        button_1 = pygame.Rect(20, 105, 210, 40)
        pygame.draw.rect(screen, button_color1, button_1)
        draw_text('BALL VELOCITY', font3, text_color1,screen,30,115)
        selecteur_1=pygame.Rect(350, 115, ball_speed, 20)
        pygame.draw.rect(screen, white, selecteur_1)
        
        button_2 = pygame.Rect(20, 185, 210, 40)
        pygame.draw.rect(screen, button_color2, button_2)
        draw_text('PADDLE VELOCITY', font3, text_color2,screen,30,195)
        selecteur_2=pygame.Rect(350, 195, paddle_speed, 20)
        pygame.draw.rect(screen, white, selecteur_2)

        button_3 = pygame.Rect(20, 265, 210, 40)
        pygame.draw.rect(screen, button_color3, button_3)
        draw_text('BALL WIDTH', font3, text_color3,screen,30,275)
        selecteur_3=pygame.Rect(e, f, ball_width, d)
        pygame.draw.rect(screen, white, selecteur_3)
        
        button_4 = pygame.Rect(20, 385, 210, 40)
        pygame.draw.rect(screen, button_color4, button_4)
        draw_text('PADDLE HEIGHT', font3, text_color4,screen,30,395)
        selecteur_4=pygame.Rect(350, h, 10, paddle_height)
        pygame.draw.rect(screen, white, selecteur_4)

        button_5 = pygame.Rect(20, 520, 210, 40)
        pygame.draw.rect(screen, button_color5, button_5)
        draw_text('WINNING POINTS', font3, text_color5,screen,30,530)
        selecteur_5=draw_text(str(winning_points), font,white,screen,350,525)       

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                    return(ball_speed,paddle_speed,ball_width,paddle_height,winning_points)
                    
                if event.key == K_DOWN:
                    if where == 3 :
                        button_color4 = black
                        text_color4 = white
                        button_color5 = white
                        text_color5 = black
                        where = 4
                    if where == 2 :
                        button_color3 = black
                        text_color3 = white
                        button_color4 = white
                        text_color4 = black
                        where = 3
                    if where == 1 :
                        button_color2 = black
                        text_color2 = white
                        button_color3 = white
                        text_color3 = black
                        where = 2
                    if where == 0:
                        button_color1 = black
                        text_color1 = white
                        button_color2 = white
                        text_color2 = black
                        where = 1
                        
                if event.key == K_UP :
                    if where == 1 :
                        button_color2 = black
                        text_color2 = white
                        button_color1 = white
                        text_color1 = black
                        where = 0
                    if where == 2 :
                        button_color3 = black
                        text_color3 = white
                        button_color2 = white
                        text_color2 = black   
                        where = 1
                    if where == 3 :
                        button_color4 = black
                        text_color4 = white
                        button_color3 = white
                        text_color3 = black
                        where = 2
                    if where == 4 :
                        button_color5 = black
                        text_color5 = white
                        button_color4 = white
                        text_color4 = black
                        where = 3
                        
                if event.key == K_RIGHT :
                    if where == 0 :
                        if ball_speed != 600 :
                            ball_speed += 50
                    if where == 1 :
                        if paddle_speed != 600 :
                            paddle_speed += 50
                    if where == 2 :
                        if ball_width != 30 :
                            ball_width += 5
                            d += 5
                            e -= 2.5
                            f -= 2.5
                    if where == 3 :
                        if paddle_height != 200 :
                            paddle_height += 10
                            h -= 5
                    if where == 4 :
                        if winning_points != inf:
                            winning_points += 1
                        else : 
                            winning_points = 1
                            
                if event.key == K_LEFT :
                    if where == 0 :
                        if ball_speed != 50 :
                            ball_speed -= 50
                    if where == 1 :
                        if paddle_speed != 50 :
                            paddle_speed -= 50
                    if where == 2 :
                        if ball_width != 5 :
                            ball_width -= 5
                            d -= 5
                            e += 2.5
                            f += 2.5
                    if where == 3 :
                        if paddle_height != 10 :
                            paddle_height -= 10  
                            h += 5
                    if where == 4 :
                        if winning_points == 1 :
                            winning_points = inf
                        if type(winning_points)==int :
                            winning_points -= 1

                            
                            
        pygame.display.update()
        mainClock.tick(60)
 


main_menu()