import pygame, sys
import random

## sets up pygame & window
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((1200, 600))
clock = pygame.time.Clock()
pygame.display.set_caption('base of game')
font = pygame.font.SysFont('Comic Sans MS', 30)


##loads background image + scales it properly
bkg_img = pygame.image.load('bkg_img.jpg').convert() ## .convert_alpha() to make transparent pixels show as such
bkg_img2 = pygame.transform.scale(bkg_img, (1200, 600))


## load ALL card images from a folder
ClubsAce = pygame.image.load('CardImages\Ace_Clubs.png').convert_alpha()
SpadesAce = pygame.image.load('CardImages\Ace_Spades.png').convert_alpha()
HeartsAce = pygame.image.load('CardImages\Ace_Hearts.png').convert_alpha()
DiamondsAce = pygame.image.load('CardImages\Ace_Diamonds.png').convert_alpha()
Clubs2 = pygame.image.load('CardImages\Clubs_2.png').convert_alpha()
Spades2 = pygame.image.load('CardImages\Spades_2.png').convert_alpha()
Hearts2 = pygame.image.load('CardImages\Hearts_2.png').convert_alpha()
Diamonds2 = pygame.image.load('CardImages\Diamonds_2.png').convert_alpha()
Clubs3 = pygame.image.load('CardImages\Clubs_3.png').convert_alpha()
Spades3 = pygame.image.load('CardImages\Spades_3.png').convert_alpha()
Hearts3 = pygame.image.load('CardImages\Hearts_3.png').convert_alpha()
Diamonds3 = pygame.image.load('CardImages\Diamonds_3.png').convert_alpha()
Clubs4 = pygame.image.load('CardImages\Clubs_4.png').convert_alpha()
Spades4 = pygame.image.load('CardImages\Spades_4.png').convert_alpha()
Hearts4 = pygame.image.load('CardImages\Hearts_4.png').convert_alpha()
Diamonds4 = pygame.image.load('CardImages\Diamonds_4.png').convert_alpha()
Clubs5 = pygame.image.load('CardImages\Clubs_5.png').convert_alpha()
Spades5 = pygame.image.load('CardImages\Spades_5.png').convert_alpha()
Hearts5 = pygame.image.load('CardImages\Hearts_5.png').convert_alpha()
Diamonds5 = pygame.image.load('CardImages\Diamonds_5.png').convert_alpha()
Clubs6 = pygame.image.load('CardImages\Clubs_6.png').convert_alpha()
Spades6 = pygame.image.load('CardImages\Spades_6.png').convert_alpha()
Hearts6 = pygame.image.load('CardImages\Hearts_6.png').convert_alpha()
Diamonds6 = pygame.image.load('CardImages\Diamonds_6.png').convert_alpha()
Clubs7 = pygame.image.load('CardImages\Clubs_7.png').convert_alpha()
Spades7 = pygame.image.load('CardImages\Spades_7.png').convert_alpha()
Hearts7 = pygame.image.load('CardImages\Hearts_7.png').convert_alpha()
Diamonds7 = pygame.image.load('CardImages\Diamonds_7.png').convert_alpha()
Clubs8 = pygame.image.load('CardImages\Clubs_8.png').convert_alpha()
Spades8 = pygame.image.load('CardImages\Spades_8.png').convert_alpha()
Hearts8 = pygame.image.load('CardImages\Hearts_8.png').convert_alpha()
Diamonds8 = pygame.image.load('CardImages\Diamonds_8.png').convert_alpha()
Clubs9 = pygame.image.load('CardImages\Clubs_9.png').convert_alpha()
Spades9 = pygame.image.load('CardImages\Spades_9.png').convert_alpha()
Hearts9 = pygame.image.load('CardImages\Hearts_9.png').convert_alpha()
Diamonds9 = pygame.image.load('CardImages\Diamonds_9.png').convert_alpha()
Clubs10 = pygame.image.load('CardImages\Clubs_10.png').convert_alpha()
Spades10 = pygame.image.load('CardImages\Spades_10.png').convert_alpha()
Hearts10 = pygame.image.load('CardImages\Hearts_10.png').convert_alpha()
Diamonds10 = pygame.image.load('CardImages\Diamonds_10.png').convert_alpha()
ClubsJack = pygame.image.load('CardImages\Jack_Clubs.png').convert_alpha()
SpadesJack = pygame.image.load('CardImages\Jack_Spades.png').convert_alpha()
HeartsJack = pygame.image.load('CardImages\Jack_Hearts.png').convert_alpha()
DiamondsJack = pygame.image.load('CardImages\Jack_Diamonds.png').convert_alpha()
ClubsQueen = pygame.image.load('CardImages\Queen_Clubs.png').convert_alpha()
SpadesQueen = pygame.image.load('CardImages\Queen_Spades.png').convert_alpha()
HeartsQueen = pygame.image.load('CardImages\Queen_Hearts.png').convert_alpha()
DiamondsQueen = pygame.image.load('CardImages\Queen_Diamonds.png').convert_alpha()
ClubsKing = pygame.image.load('CardImages\King_Clubs.png').convert_alpha()
SpadesKing = pygame.image.load('CardImages\King_Spades.png').convert_alpha()
HeartsKing = pygame.image.load('CardImages\King_Hearts.png').convert_alpha()
DiamondsKing = pygame.image.load('CardImages\King_Diamonds.png').convert_alpha()
GrayJoker = pygame.image.load('CardImages\Grey_Joker.png').convert_alpha()
ColorJoker = pygame.image.load('CardImages\Color_Joker.png').convert_alpha()




x = 0

## variables & data n such
running = True
forwards = True
cardCount = 5
cardSelectedCount = 0
countTracker1 = False
countTracker2 = False
countTracker3 = False
countTracker4 = False
countTracker5 = False
countTracker6 = False
leftClick = False
rightClick = False
middleClick = False
select1 = True
select2 = True
select3 = True
select4 = True
select5 = True
select6 = True
card6Setup = False
offset = [425, 450]
card1ypos = offset[0]
card2ypos = offset[0]
card3ypos = offset[0]
card4ypos = offset[0]
card5ypos = offset[0]
card6hb = pygame.Rect(0, 0, 0, 0)
deck = [ClubsAce, SpadesAce, HeartsAce, DiamondsAce, Clubs2, Spades2, Hearts2, Diamonds2, Clubs3, Spades3, Hearts3, Diamonds3, Clubs4, Spades4, Hearts4, Diamonds4, Clubs5, Spades5, Hearts5, Diamonds5, Clubs6, Spades6, Hearts6, Diamonds6, Clubs7, Spades7, Hearts7, Diamonds7, Clubs8, Spades8, Hearts8, Diamonds8, Clubs9, Spades9, Hearts9, Diamonds9, Clubs10, Spades10, Hearts10, Diamonds10, ClubsJack, SpadesJack, HeartsJack, DiamondsJack, ClubsQueen, SpadesQueen, HeartsQueen, DiamondsQueen, ClubsKing, SpadesKing, HeartsKing, DiamondsKing, GrayJoker, ColorJoker]
shuffledDeck = random.sample(deck, len(deck))

delta_time = 0.1

##loads test image & test cards 
image = pygame.Surface((176, 64))
card1 = shuffledDeck[0] ## cards have a 5:7 ratio of length to height
card2 = shuffledDeck[1]
card3 = shuffledDeck[2]
card4 = shuffledDeck[3]
card5 = shuffledDeck[4]
card6 = pygame.Surface((100, 120))


while running:
    
    ## makes the background image
    screen.blit(bkg_img2, (0, 0))

    ## equally spaces cards based on the amount of cards
    card1xpos = (800 / cardCount) - 100
    card2xpos = (2 * (800 / cardCount)) - 100
    card3xpos = (3 * (800 / cardCount)) - 100
    card4xpos = (4 * (800 / cardCount)) - 100
    card5xpos = (5 * (800 / cardCount)) - 100

    ## gets mouse position
    mpos = pygame.mouse.get_pos()

    ## rotation & location setup
    rot = 0
    loc = [0, 0]

    ## makes middle click do something, for now sets card count to 6 for testing purposes
    if middleClick == True:
        cardCount = 6

    ## mouse position
    mx, my = pygame.mouse.get_pos()


    ## hitbox test
    hitbox = pygame.Rect(x, 0, image.get_width(), image.get_height())
    card1hb = pygame.Rect(card1xpos, card1ypos, card1.get_width(), card1.get_height())
    card2hb = pygame.Rect(card2xpos, card2ypos, card2.get_width(), card2.get_height())
    card3hb = pygame.Rect(card3xpos, card3ypos, card3.get_width(), card3.get_height())
    card4hb = pygame.Rect(card4xpos, card4ypos, card4.get_width(), card4.get_height())
    card5hb = pygame.Rect(card5xpos, card5ypos, card5.get_width(), card5.get_height())

    ## makes a test image & test cards
    screen.blit(image, (x, 0))
    screen.blit(card1, (card1xpos, card1ypos))
    screen.blit(card2, (card2xpos, card2ypos))
    screen.blit(card3, (card3xpos, card3ypos))
    screen.blit(card4, (card4xpos, card4ypos))
    screen.blit(card5, (card5xpos, card5ypos))


    ## if selected = True:
        ##


    ## tracks the amount of cards currently selected, likely very inefficently... 
    if select1 == True and countTracker1 == False:
        cardSelectedCount += 1
        countTracker1 = True
    elif select1 == False and countTracker1 == True:
        cardSelectedCount -= 1
        countTracker1 = False
    if select2 == True and countTracker2 == False:
        cardSelectedCount += 1
        countTracker2 = True
    elif select2 == False and countTracker2 == True:
        cardSelectedCount -= 1
        countTracker2 = False
    if select3 == True and countTracker3 == False:
        cardSelectedCount += 1
        countTracker3 = True
    elif select3 == False and countTracker3 == True:
        cardSelectedCount -= 1
        countTracker3 = False
    if select4 == True and countTracker4 == False:
        cardSelectedCount += 1
        countTracker4 = True
    elif select4 == False and countTracker4 == True:
        cardSelectedCount -= 1
        countTracker4 = False
    if select5 == True and countTracker5 == False:
        cardSelectedCount += 1
        countTracker5 = True
    elif select5 == False and countTracker5 == True:
        cardSelectedCount -= 1
        countTracker5 = False
    if cardCount == 6:
        if select6 == True and countTracker6 == False:
            cardSelectedCount += 1
            countTracker6 = True
        elif select6 == False and countTracker6 == True:
            cardSelectedCount -= 1
            countTracker6 = False


    ## makes target & gives collision
    target = pygame.Rect(300, 0, 160, 280)
    collision = hitbox.colliderect(target)
    m_collision = target.collidepoint(mpos) ## signifies mouse collision w/target using colors

    pygame.draw.rect(screen, (255 * collision, 255 * m_collision, 0), target)


    ## test for if there's 6 cards rather than 5
    if cardCount == 6: ## and card6Setup == False:
        card6xpos = (6 * (800 / cardCount)) - 100
        card6ypos = offset[0] ## currently facing a bug where card 6 cannot be selected, or at least does not visually show as such...
        screen.blit(card6, (card6xpos, card6ypos))
        card6hb = pygame.Rect(card6xpos, card6ypos, card6.get_width(), card6.get_height())
        ## card6Setup = True
    m_collision6 = card6hb.collidepoint(mpos) ## mouse collision w/card6




    ## leftClick detection; flips between 'selected' and 'unselected' states when right clicked, and changes their position accordingly
    if leftClick == True:
        if pygame.Rect.collidepoint(card1hb, mx, my):
            if select1 == True and cardSelectedCount <= 5:
                card1ypos = offset[1]
            else:
                card1ypos = offset[0]
            select1 = not select1
        if pygame.Rect.collidepoint(card2hb, mx, my):
            if select2 == True and cardSelectedCount <= 5:
                card2ypos = offset[1]
            else:
                card2ypos = offset[0]
            select2 = not select2
        if pygame.Rect.collidepoint(card3hb, mx, my):
            if select3 == True and cardSelectedCount <= 5:
                card3ypos = offset[1]
            else:
                card3ypos = offset[0]
            select3 = not select3
        if pygame.Rect.collidepoint(card4hb, mx, my):
            if select4 == True and cardSelectedCount <= 5:
                card4ypos = offset[1]
            else:
                card4ypos = offset[0]
            select4 = not select4
        if pygame.Rect.collidepoint(card5hb, mx, my):
            if select5 == True and cardSelectedCount <= 5:
                card5ypos = offset[1]
            else:
                card5ypos = offset[0]
            select5 = not select5
        if pygame.Rect.collidepoint(card6hb, mx, my):
            if cardCount == 6: 
                if select6 == True and cardSelectedCount <= 5:
                    card6ypos = offset[1]
                else:
                    card6ypos = offset[0]
                select6 = not select6


    ## stupid test collision thingy
    if forwards == True:
        x += 100 * delta_time
    else:
        x -= 100 * delta_time
    if x > (1000 - image.get_width()):
        forwards = False
    if x < 0:
        forwards = True
    
    
    leftClick = False ## resets left click each frame

    for event in pygame.event.get():
        if event.type == pygame.QUIT: ## makes the game stop running when quit by closing window
            running = False
        if event.type == pygame.KEYDOWN: ## makes the game stop running when quit with escape key
            if event.key == K_ESCAPE:
                running = False
        if event.type == pygame.MOUSEBUTTONDOWN: ## detects any mouse button input
            if event.button == 1: ## detects left click (left click = 1, middle click = 2, right click = 3, scroll up = 4, scroll down = 5)
                leftClick = True
            if event.button == 3: ## detects right click
                rightClick = True
            if event.button == 2: ## detects middle click
                middleClick = not middleClick
        if event.type == pygame.MOUSEBUTTONUP: ## detects any mouse button let go
            if event.button == 3: ## detects right click let go, right click is for holding
                rightClick = False



    ## makes it actually display on the screen, i guess
    pygame.display.flip()

    ## ticks clock, uses delta time
    delta_time = clock.tick(60) / 1000
    delta_time = max(0.001, min(0.1, delta_time))

pygame.quit()
