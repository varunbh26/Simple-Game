import pygame
from pygame.locals import *

size = 1440,900
width, height = size
GREEN = (150, 255, 150)
RED = (255, 0, 0)

pygame.init()
screen = pygame.display.set_mode(size)
running = True

ball = pygame.image.load("ball.gif")
rect = ball.get_rect()
speed = [1, 1]

while True:
    for event in pygame.event.get():
        if event.type == QUIT: 
            running = False

    rect = rect.move(speed)
    if rect.left < 0 or rect.right > width:
        if speed[0]>0:
            speed[0] = -(speed[0]+1)
        else:
            speed[0] = -(speed[0]-1)
    if rect.top < 0 or rect.bottom > height:
        if speed[1]>0:
            speed[1] = -(speed[1]+1)
        else:
            speed[1] = -(speed[1]-1)
    screen.fill(GREEN)
    pygame.draw.rect(screen, RED, rect, 1)
    screen.blit(ball, rect)
    pygame.display.update()

pygame.quit()