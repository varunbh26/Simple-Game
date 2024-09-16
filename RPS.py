import pygame
from pygame.locals import *
from pygame import *
import Rock
size = 1280,768
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (0,0,255)
background = WHITE
PlayerInput = "NotChosen"
aichoice = Rock.have_computer_choice()
winpath = "Win.png"
losepath = "Lose.png"
tiepath = "Tie.png"
back_path = "RPS_back.png"
pygame.font.init()
back = pygame.image.load(back_path)
win = pygame.image.load(winpath)
lose = pygame.image.load(losepath)
tie = pygame.image.load(tiepath)
text_font = font.SysFont(None,100)
text  = text_font.render("Choose from the bottom",True,BLACK)
def play_game():
    pygame.init
    global PlayerInput
    screen = pygame.display.set_mode(size)
    running = True
    airock =  Rect(230,50,260,260)
    aipaper = Rect(510,50,260,260)
    aisci = Rect(790,50,260,260)
    prock = Rect(230,400,260,260)
    ppaper = Rect(510,400,260,260)
    psci = Rect(790,400,260,260)
    rock_path  = "Rock.png"
    rock = pygame.image.load(rock_path)
    paper_path = "Paper.png"
    paper = pygame.image.load(paper_path)
    scissors_path = "scissors.png"
    scissors = pygame.image.load(scissors_path)
    winner = None
    while running:
        caption = "Rock,Paper,Scissors"
        pygame.display.set_caption(caption)
        screen.fill(background)
        screen.blit(back,(0,0))
        screen.blit(text,(200,700))
        if PlayerInput == "NotChosen":
            screen.blit(rock,airock.topleft)
            screen.blit(paper,aipaper.topleft)
            screen.blit(scissors,aisci.topleft)
            screen.blit(rock,prock.topleft)
            screen.blit(paper,ppaper.topleft)
            screen.blit(scissors,psci.topleft)
        elif  PlayerInput != "NotChosen":
            winner = Rock.winner(PlayerInput,aichoice)
        if aichoice == "rock":
            screen.blit(rock,airock.topleft)
        elif aichoice == "paper":
            screen.blit(paper,aipaper.topleft)
        elif aichoice == "scissors":
            screen.blit(scissors,aisci.topleft)
        if PlayerInput == "rock":
            screen.blit(rock,prock.topleft)
        elif PlayerInput == "paper":
            screen.blit(paper,ppaper.topleft)
        elif PlayerInput == "scissors":
            screen.blit(scissors,psci.topleft)
        if winner == "You win!":
            screen.blit(win,(0,0))
            #print(1)
        elif winner == "Computer wins!":
            screen.blit(lose,(0,0))
            #print(2)
        elif winner == "It's a tie!":
            screen.blit(tie,(0,0))
        #print(3)
        #print(winner)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if prock.collidepoint(event.pos):
                    PlayerInput = "rock"
                elif  ppaper.collidepoint(event.pos):
                    PlayerInput = "paper"
                elif psci.collidepoint(event.pos):
                    PlayerInput = "scissors"
    pygame.quit()