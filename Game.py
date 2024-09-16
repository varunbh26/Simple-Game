import pygame
from pygame.locals import *
import RPS,TTT,HM
size =  1280,768
pygame.init()
winpath = "Win.png"
losepath = "Lose.png"
tiepath = "Tie.png"
win = pygame.image.load(winpath)
lose = pygame.image.load(losepath)
tie = pygame.image.load(tiepath)
RPS_tile_path = "RPS.png"
TTT_tile_path = "TTT.png"
HM_tile_path = "HM.png"
RPS_tile = pygame.image.load(RPS_tile_path)
TTT_tile = pygame.image.load(TTT_tile_path)
HM_tile = pygame.image.load(HM_tile_path)
clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)
running = True
class ListItem(Rect):
    def __init__(self,top,left):
        self.width = 180*2
        self.height = 300
        self.left = left
        self.top = top
rps = ListItem(50,100)
ttt = ListItem(50,800)
hm = pygame.Rect(100,400,1060,300)
speed = [1,1]
CYAN  = (154, 232, 242)
RED = (255,0,0)
GREEN = (0,255,0)
background = CYAN
while running:
    caption ='Game Menu'
    pygame.display.set_caption(caption)
    screen.fill(background)
    mouse_pos = pygame.mouse.get_pos()
    if rps.collidepoint(mouse_pos):
        newrps = rps.inflate(20,20)
        pygame.draw.rect(screen, GREEN, newrps)
        screen.blit(RPS_tile,newrps)
    else:
        screen.blit(RPS_tile,rps)
    if ttt.collidepoint(mouse_pos):
        newttt = ttt.inflate(20,20)
        pygame.draw.rect(screen, GREEN, newttt)
        screen.blit(TTT_tile,newttt)
    else:
        screen.blit(TTT_tile,ttt)
    if hm.collidepoint(mouse_pos):
        newhm = hm.inflate(20,20) 
        pygame.draw.rect(screen, GREEN, newhm)
        screen.blit(HM_tile,newhm)
    else:
        screen.blit(HM_tile,hm)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == MOUSEBUTTONDOWN:
            if rps.collidepoint(event.pos):
                RPS.play_game()
                running = False
            if ttt.collidepoint(event.pos):
                TTT.play_game()
                running = False
            if hm.collidepoint(event.pos):
                HM.play_game()
                running = False
pygame.quit()