import pygame
from pygame import *
import random
size = 1280,768
winpath = "Win.png"
losepath = "Lose.png"
tiepath = "Tie.png"
win = pygame.image.load(winpath)
lose = pygame.image.load(losepath)
tie = pygame.image.load(tiepath)
def ch_word():
    words = ["plate", "batman", "notebook", "airplane", "love", "college", "teacher"]
    return random.choice(words)
def play_game():
    pygame.init
    screen = pygame.display.set_mode(size)
    WHITE = (255,255,255)
    BLACK = (0,0,0)
    RED = (255,0,0)
    BLUE = (0,0,255)
    text_font = font.SysFont(None,34)
    letter_font = font.SysFont(None,150)
    background = WHITE
    runnning = True
    hangman_path = "hangman5.png"
    line_path = "HM_line.png"
    line = image.load(line_path)
    screen_rect = Rect(0,0,1280,768)
    word = ch_word()
    text = text_font.render("The word is " + word, True ,BLACK)
    letters = list(word)
    guesses = Rect(100,500,1080,200)
    guessed_letters = []
    incorrect_attempts = 0
    max_attempts = 5
    guess = "yes"
    status = False
    guesses_key = {
        K_a: 'a',
        K_b: 'b',
        K_c: 'c',
        K_d: 'd',
        K_e: 'e',
        K_f: 'f',
        K_g: 'g',
        K_h: 'h',
        K_i: 'i',
        K_j: 'j',
        K_k: 'k',
        K_l: 'l',
        K_m: 'm',
        K_n: 'n',
        K_o: 'o',
        K_p: 'p',
        K_q: 'q',
        K_r: 'r',
        K_s: 's',
        K_t: 't',
        K_u: 'u',
        K_v: 'v',
        K_w: 'w',
        K_x: 'x',
        K_y: 'y',
        K_z: 'z'
    }
    while runnning:
        caption = "Hangman"
        pygame.display.set_caption(caption)
        hangman = image.load(hangman_path)
        screen.fill(background)
        screen.blit(hangman,screen_rect.topleft)
        if incorrect_attempts == 1:
            hangman_path = "hangman4.png"
        elif incorrect_attempts == 2:
            hangman_path = "hangman3.png"
        elif incorrect_attempts == 3:
            hangman_path = "hangman2.png"
        elif incorrect_attempts == 4:
            hangman_path = "hangman1.png"
        elif incorrect_attempts == 5:
            hangman_path = "hangman0.png"
            screen.blit(lose,(0,0))
        if guess.isalpha() and len(guess) == 1:
                if guess in guessed_letters:
                    pass
                elif guess in word:
                    guessed_letters.append(guess)
                else:
                    incorrect_attempts += 1
                    guessed_letters.append(guess)

                if incorrect_attempts == max_attempts:
                    status = True
                    
                elif set(word) <= set(guessed_letters):
                    status = True   
        c = 1
        if incorrect_attempts < 5  and status == True:
            screen.blit(win,(0,0))
        #draw.rect(screen,BLUE,guesses)
        for i in letters:
            rect_letter = Rect(100+(c-1)*(80+((1080-(len(letters) * 80))//len(letters))),500,80,200)
            screen.blit(line,rect_letter.topleft)
            c += 1
        c = 1
        for letter in word:
            if letter in guessed_letters:
                alphabet = letter_font.render(letter,True,BLACK)
                screen.blit(alphabet,(100+(c-1)*(80+((1080-(len(letters) * 80))//len(letters))),550))
                c += 1
            else:
                c += 1
        if status:
            screen.blit(text,(500,740))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                runnning = False
            elif event.type == KEYDOWN and status == False:
                if event.key in guesses_key:
                    guess = guesses_key[event.key]
    pygame.quit()