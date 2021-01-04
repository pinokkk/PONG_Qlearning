#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 15:50:12 2020

@author: nathan & maxence
"""

import pygame, random
import numpy as np
random.seed(28)


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)



class Paddle(pygame.Rect):
    def __init__(self, velocity, up_key, down_key, ia, *args, **kwargs):
        self.velocity = velocity 
        self.up_key = up_key
        self.down_key = down_key
        self.ia=ia
        super().__init__(*args, **kwargs)
        
    def move_paddle(self, board_height, board_width, ball, action, va):
        if self.ia==0: #case where the paddle is controlled by a player
            keys_pressed = pygame.key.get_pressed()
            if keys_pressed[self.up_key]:
                if self.y - self.velocity > 0:
                    self.y -= self.velocity

            if keys_pressed[self.down_key]:
                if self.y + self.velocity < board_height - self.height:
                    self.y += self.velocity
        elif self.ia==1: #case where the paddle is controlled by static IA
            if self.x == board_width-self.width :
                if ball.velocity > 0:
                    if ball.center[1]<self.center[1]+va and abs(ball.center[1]-self.center[1]+va)>self.velocity:
                        if self.y - self.velocity > 0:
                            self.y -= self.velocity
                    elif ball.center[1]>self.center[1]+va and abs(ball.center[1]-self.center[1]+va)>self.velocity:
                        if self.y + self.velocity < board_height - self.height:
                            self.y += self.velocity
                else :
                    if self.y + self.height/2 > 305 :
                        self.y -= self.velocity
                    elif self.y + self.height/2 < 295:
                        self.y += self.velocity
                        
            else :
                if ball.velocity < 0:
                    if ball.center[1]<self.center[1]+va and abs(ball.center[1]-self.center[1]+va)>self.velocity:
                        if self.y - self.velocity > 0:
                            self.y -= self.velocity
                    elif ball.center[1]>self.center[1]+va and abs(ball.center[1]-self.center[1]+va)>self.velocity:
                        if self.y + self.velocity < board_height - self.height:
                            self.y += self.velocity
                else :
                    if self.y + self.height/2 > 305 :
                        self.y -= self.velocity
                    elif self.y + self.height/2 < 295:
                        self.y += self.velocity
                        
        elif self.ia==2:
            if action==1:
                if self.y - self.velocity > 0:
                    self.y -= self.velocity
            elif action==2:
                if self.y + self.velocity < board_height-self.height:
                    self.y += self.velocity


            
                            

class Ball(pygame.Rect):
    def __init__(self, velocity, *args, **kwargs):
        self.velocity = velocity
        self.angle = 3
        super().__init__(*args, **kwargs)
        
    def move_ball(self):
        self.x += self.velocity
        self.y += self.angle
        
class Pong:
    HEIGHT = 600
    WIDTH = 1000
    PADDLE_WIDTH = 20
    PADDLE_HEIGHT = 100
    PADDLE_VELOCITY = 8
    BALL_WIDTH = 30
    BALL_VELOCITY = 10
    COLOUR = (255, 255, 255)
    VAINQUEUR = bool(random.getrandbits(1)) 
    SCOREA = 0
    SCOREB = 0
    POINTS_TO_WIN=11
    reward=0
    visee_alea=0
    
    
    def check_ball_hits_wall(self):
        for ball in self.balls:
            if ball.x > self.WIDTH :
                self.VAINQUEUR = False
                ball.x = self.WIDTH/2 - ball.height/2
                ball.y = self.HEIGHT/2
                ball.velocity = 0
                ball.angle = 0
                self.SCOREA += 1
                self.reward=1000
            if  ball.x < 0 :
                self.reward=-abs(self.paddles[0].y+self.PADDLE_HEIGHT/2-ball.y-self.BALL_WIDTH/2)
                self.VAINQUEUR = True
                ball.x = self.WIDTH/2 - ball.height/2
                ball.y = self.HEIGHT/2
                ball.velocity=0
                ball.angle = 0
                self.SCOREB += 1
            if ball.y > self.HEIGHT - self.BALL_WIDTH or ball.y < 0:
                ball.angle = -ball.angle

    def check_ball_hits_paddle(self):
        for ball in self.balls:
                ball_center=ball.center
                for paddle in self.paddles:
                    paddle_center=paddle.center
                    stepsize=paddle.height // 2 //5
                    degrees=2
                    if ball.colliderect(paddle):
                        if paddle.ia == 2 :
                            self.reward=100
                        else:
                            self.reward=-10
                        if paddle.ia == 1 :
                            self.visee_alea=random.randint(-self.PADDLE_HEIGHT/2,self.PADDLE_HEIGHT/2)
                        ball.velocity = -(ball.velocity)
                        if ball_center[1] < paddle_center[1]:
                            factor = (paddle_center[1] - ball_center[1]) // stepsize
                            ball.angle = -int(round(factor * degrees))
                        elif ball_center[1] > paddle_center[1]:
                            factor = (ball_center[1] - paddle_center[1]) // stepsize
                            ball.angle = int(round(factor * degrees))
                        else:
                            ball.angle = 0
                        break

    def getState(self):
        for ball in self.balls:
            ballx = ball.x
            bally = ball.y
            balla = ball.angle
        paddleg = self.paddles[0].y
        paddled = self.paddles[1].y
        return np.array([ballx,bally,balla,paddleg,paddled])
            
    def __init__(self,j1,j2,ball_speed,paddle_speed,ball_width,paddle_height,winning_points):
        pygame.init()  # Start the pygame instance.
        self.central_line = pygame.Rect(self.WIDTH/2, 0, 1, self.HEIGHT)
        
        # Setup the screen
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("PONG")
        self.clock = pygame.time.Clock()
        self.BALL_VELOCITY=ball_speed/25
        self.PADDLE_VELOCITY=paddle_speed/50
        self.BALL_WIDTH=ball_width
        self.PADDLE_HEIGHT=paddle_height
        self.POINTS_TO_WIN=winning_points
        
        
        # Create the player objects.
        self.paddles = []
        self.balls = []
        
        self.paddles.append(Paddle(  # The left paddle (IA)
            self.PADDLE_VELOCITY,
            pygame.K_s,
            pygame.K_w,
            j1,
            0,
            self.HEIGHT / 2 - self.PADDLE_HEIGHT / 2,
            self.PADDLE_WIDTH,
            self.PADDLE_HEIGHT
        ))

        self.paddles.append(Paddle(  # The right paddle
            self.PADDLE_VELOCITY,
            pygame.K_UP,
            pygame.K_DOWN,
            j2,
            self.WIDTH - self.PADDLE_WIDTH,
            self.HEIGHT / 2 - self.PADDLE_HEIGHT / 2,
            self.PADDLE_WIDTH,
            self.PADDLE_HEIGHT
        ))
        
                
        self.balls.append(Ball(
            self.BALL_VELOCITY,
            self.WIDTH / 2 - self.BALL_WIDTH / 2,
            self.HEIGHT / 2 - self.BALL_WIDTH / 2,
            self.BALL_WIDTH,
            self.BALL_WIDTH
        ))
        
        
    def next_step(self,action):
        self.screen.fill((0, 0, 0))
        pygame.draw.rect(self.screen, self.COLOUR, self.central_line)

        self.reward=0
        for paddle in self.paddles:
            paddle.move_paddle(self.HEIGHT,self.WIDTH,self.balls[0],action,self.visee_alea)
            pygame.draw.rect(self.screen, self.COLOUR, paddle)

        for ball in self.balls:
            if ball.velocity == 0 :
                if self.VAINQUEUR==True:
                        ball.velocity = self.BALL_VELOCITY   
                else:
                       ball.velocity = -self.BALL_VELOCITY
                ball.angle = random.randint(-2,2) 
            ball.move_ball()
            pygame.draw.rect(self.screen, self.COLOUR, ball)
        self.check_ball_hits_paddle()
        self.check_ball_hits_wall()
        
        #Affichage score
        font = pygame.font.Font(None, 74)
        if self.SCOREA < 10:
            text = font.render(str(self.SCOREA), 1, self.COLOUR)
            self.screen.blit(text, (self.WIDTH/2-50,10))
        else : 
            text = font.render(str(self.SCOREA), 1, self.COLOUR)
            self.screen.blit(text, (self.WIDTH/2-70,10))
        text = font.render(str(self.SCOREB), 1, self.COLOUR)
        self.screen.blit(text, (self.WIDTH/2+20,10))
        pygame.display.flip()
        state=self.getState()
        
        return state, self.reward

