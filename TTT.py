import pygame
from pygame import *
import numpy as np
import array
import math
size = 1280,768
winpath = "redwinn.png"
losepath = "bkuewin.png"
tiepath = "Tie.png"
background_path = "TTT_back.png"
back = pygame.image.load(background_path)
win = pygame.image.load(winpath)
lose = pygame.image.load(losepath)
tie = pygame.image.load(tiepath)
def play_game():
    pygame.init()
    def check_winner(A):
        if (A[0] == A[1]) and (A[1] == A[2]) and A[0] !=0:
            wincon1 = True
            return wincon1
        elif (A[3] == A[4]) and (A[4] == A[5]) and A[3] !=0:
            wincon2 = True
            return wincon2
        elif (A[6] == A[7]) and (A[7] == A[8]) and A[6] !=0:
            wincon3 = True
            return wincon3
        elif (A[0] == A[3]) and (A[3] == A[6]) and A[0] !=0:
            wincon4 = True
            return wincon4
        elif (A[1] == A[4]) and (A[4] == A[7]) and A[1] !=0:
            wincon5 = True
            return wincon5
        elif (A[2] == A[5]) and (A[5] == A[8]) and A[2] !=0:
            wincon6 = True
            return wincon6
        elif (A[0] == A[4]) and (A[4] == A[8]) and A[0] !=0:
            wincon7 = True
            return wincon7
        elif (A[2] == A[4]) and (A[4] == A[6]) and A[2] !=0:
            wincon8 = True
            return wincon8
        else:
            return False

    class InputHolder(Rect):
        def __init__(self,width,height,xpos,ypos):
            self.width = width
            self.height = height
            self.x = xpos
            self.y = ypos
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(size)
    running = True
    WHITE = (255,255,255)
    BLACK = (0,0,0)
    RED = (0,0,255)
    background = WHITE      
    Circle_path = "Circle.png"
    Circle = pygame.image.load(Circle_path)
    Cross_path = "Cross.png"
    Cross = pygame.image.load(Cross_path)
    Currplayer = 0
    A = [0,0,0,0,0,0,0,0,0]
    redwin=(248,90,47)
    bluewin = (54, 151, 255)
    row1line = Rect(350,160,550,10)
    row2line = Rect(350,320,550,10)
    row3line = Rect(350,530,550,10)
    col1line = Rect(410,100,10,550)
    col2line = Rect(600,100,10,550)
    col3line = Rect(800,100,10,550)
    dialine = Rect(350,100,900,650)
    while running:
        win = check_winner(A)
        #print(win)
        caption = 'Tic-Tac-Toe'
        board = [[A[0],A[1],A[2]],[A[3],A[4],A[5]],[A[6],A[7],A[8]]]
        pygame.display.set_caption(caption)
        screen.fill(background)
        screen.blit(back,(0,0))
        vertline1 = Rect(520,100,20,550)
        vertline2 = Rect(720,100,20,550)
        horline1 = Rect(350,250,550,20)
        horline2 = Rect(350,450,550,20)
        IH1 = InputHolder(170,150,350,100)
        IH2 = InputHolder(180,150,540,100)
        IH3 = InputHolder(160,150,740,100)
        IH4 = InputHolder(170,180,350,270)
        IH5 = InputHolder(180,180,540,270)
        IH6 = InputHolder(160,180,740,270)
        IH7 = InputHolder(170,180,350,470)
        IH8 = InputHolder(180,180,540,470)
        IH9 = InputHolder(160,180,740,470)
        #pygame.draw.rect(screen,WHITE,IH1)
        #screen.blit(Cross,IH1.topleft)
        if A[0] == 1:
            screen.blit(Cross,IH1.topleft)
        elif A[0] == 2:
            screen.blit(Circle,IH1.topleft)
        #pygame.draw.rect(screen,WHITE,IH2)
        if A[1] == 1:
            screen.blit(Cross,IH2.topleft)
        elif A[1] == 2:
            screen.blit(Circle,IH2.topleft)
        #pygame.draw.rect(screen,WHITE,IH3)
        if A[2] == 1:
            screen.blit(Cross,IH3.topleft)
        elif A[2] == 2:
            screen.blit(Circle,IH3.topleft)
        #pygame.draw.rect(screen,WHITE,IH4)
        if A[3] == 1:
            screen.blit(Cross,IH4.topleft)
        elif A[3] == 2:
            screen.blit(Circle,IH4.topleft)
        #pygame.draw.rect(screen,WHITE,IH5)
        if A[4] == 1:
            screen.blit(Cross,IH5.topleft)
        elif A[4] == 2:
            screen.blit(Circle,IH5.topleft)
        #pygame.draw.rect(screen,WHITE,IH6)
        if A[5] == 1:
            screen.blit(Cross,IH6.topleft)
        elif A[5] == 2:
            screen.blit(Circle,IH6.topleft)
        #pygame.draw.rect(screen,WHITE,IH7)
        if A[6] == 1:
            screen.blit(Cross,IH7.topleft)
        elif A[6] == 2:
            screen.blit(Circle,IH7.topleft)
        #pygame.draw.rect(screen,WHITE,IH8)
        if A[7] == 1:
            screen.blit(Cross,IH8.topleft)
        elif A[7] == 2:
            screen.blit(Circle,IH8.topleft)
        #pygame.draw.rect(screen,WHITE,IH9)
        if A[8] == 1:
            screen.blit(Cross,IH9.topleft)
        elif A[8] == 2:
            screen.blit(Circle,IH9.topleft)
        pygame.draw.rect(screen,BLACK,vertline1)
        pygame.draw.rect(screen,BLACK,vertline2)
        pygame.draw.rect(screen,BLACK,horline1)
        pygame.draw.rect(screen,BLACK,horline2)
        #pygame.draw.rect(screen,redwin,col3line)
        #screen.blit(Line,dialine.topleft)
        if win == True:
            if (A[0] == A[1]) and (A[1] == A[2]) and A[0] !=0:
                if Currplayer == 0:
                    pygame.draw.rect(screen,bluewin,row1line)
                else:
                    pygame.draw.rect(screen,redwin,row1line)
            
            elif (A[3] == A[4]) and (A[4] == A[5]) and A[3] !=0:
                if Currplayer == 0:
                    pygame.draw.rect(screen,bluewin,row2line)
                else:
                    pygame.draw.rect(screen,redwin,row2line)
            
            elif (A[6] == A[7]) and (A[7] == A[8]) and A[6] !=0:
                if Currplayer == 0:
                    pygame.draw.rect(screen,bluewin,row3line)
                else:
                    pygame.draw.rect(screen,redwin,row3line)
            
            elif (A[0] == A[3]) and (A[3] == A[6]) and A[0] !=0:
                if Currplayer == 0:
                    pygame.draw.rect(screen,bluewin,col1line)
                else:
                    pygame.draw.rect(screen,redwin,col1line)
            elif (A[1] == A[4]) and (A[4] == A[7]) and A[1] !=0:
                if Currplayer == 0:
                    pygame.draw.rect(screen,bluewin,col2line)
                else:
                    pygame.draw.rect(screen,redwin,col2line)
            
            elif (A[2] == A[5]) and (A[5] == A[8]) and A[2] !=0:
                if Currplayer == 0:
                    pygame.draw.rect(screen,bluewin,col3line)
                else:
                    pygame.draw.rect(screen,redwin,col3line)
            elif (A[0] == A[4]) and (A[4] == A[8]) and A[0] !=0:
                if Currplayer == 0:
                    Line_path = "Line_blue.png"
                else:
                    Line_path = "Line.png"
                Line = image.load(Line_path)
                screen.blit(Line,dialine.topleft)
            elif (A[2] == A[4]) and (A[4] == A[6]) and A[2] !=0:
                if Currplayer == 0:
                    Line_path = "Line_blue2.png"
                else:
                    Line_path = "Line2.png"
                Line = image.load(Line_path)
                screen.blit(Line,dialine.topleft)
            
        pygame.display.update()
        pygame.display.flip()
        for event in pygame.event.get():
            #print(event)
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            elif event.type == pygame.QUIT:
                running = False
            elif (event.type == MOUSEBUTTONDOWN) and win == False:
                #print("Box")
                if IH1.collidepoint(event.pos):
                    if A[0] == 0:
                        #print("Box xlicked")
                        if Currplayer == 0:
                            A[0] = 1
                            Currplayer = 1
                            print(Currplayer)
                        elif Currplayer == 1:
                            A[0] = 2
                            Currplayer = 0
                if IH2.collidepoint(event.pos):
                    if A[1] == 0:
                        #print("Box xlicked")
                        if Currplayer == 0:
                            A[1] = 1
                            Currplayer = 1
                        else:
                            A[1] = 2
                            Currplayer = 0
                if IH3.collidepoint(event.pos):
                    if A[2] == 0:
                        #print("Box xlicked")
                        if Currplayer == 0:
                            A[2] = 1
                            Currplayer = 1
                        else:
                            A[2] = 2
                            Currplayer = 0
                if IH4.collidepoint(event.pos):
                    if A[3] == 0:
                        #print("Box xlicked")
                        if Currplayer == 0:
                            A[3] = 1
                            Currplayer = 1
                        else:
                            A[3] = 2
                            Currplayer = 0
                if IH5.collidepoint(event.pos):
                    if A[4] == 0:
                        #print("Box xlicked")
                        if Currplayer == 0:
                            A[4] = 1
                            Currplayer = 1
                        else:
                            A[4] = 2
                            Currplayer = 0
                if IH6.collidepoint(event.pos):
                    if A[5] == 0:
                        #print("Box xlicked")
                        if Currplayer == 0:
                            A[5] = 1
                            Currplayer = 1
                        else:
                            A[5] = 2
                            Currplayer = 0
                if IH7.collidepoint(event.pos):
                    if A[6] == 0:
                        #print("Box xlicked")
                        if Currplayer == 0:
                            A[6] = 1
                            Currplayer = 1
                        else:
                            A[6] = 2
                            Currplayer = 0
                if IH8.collidepoint(event.pos):
                    if A[7] == 0:
                        #print("Box xlicked")
                        if Currplayer == 0:
                            A[7] = 1
                            Currplayer = 1
                        else:
                            A[7] = 2
                            Currplayer = 0
                if IH9.collidepoint(event.pos):
                    if A[8] == 0:
                        #print("Box xlicked")
                        if Currplayer == 0:
                            A[8] = 1
                            Currplayer = 1
                        else:
                            A[8] = 2
                            Currplayer = 0
                
    pygame.quit()

