#########################################
# File Name: Gravity Guy.py
# Description: This is a gravity guy game that allows you to play by your self or challange your friends.
#               You manipulate your gravity by the press of a buton and try to go for as long as possible
# Author: Matthew Bodenstein
# Date: 6/12/2019
#########################################
import pygame
import random
import time
pygame.init()
WIDTH = 800     # the width and height of the screen
HEIGHT = 600    #
gameWindow = pygame.display.set_mode((WIDTH, HEIGHT))    # this creates the screen
score = 0     # initialises the score
WHITE = (255, 255, 255) # creates colour white
RED = (255, 0, 0)   # creates colour red
player1_choice = False  # checks if the player picked their character
player2_choice = False  #
GROUND = HEIGHT   # where the ground is
GRAVITY = 2       # The gravity
GRAVITY2 = 2       # The gravity for the second player
############ All image properties ###################
chr_choice = "mario"    # sets default choice for player 1
chr_choice2 = "luigi"   # sets default choice for player 2
character_one = "mario"     # allows the players to change their character
character_two = "luigi"     #
character_three = "wario"   #
character_four = "waluigi"  #
backroundstart = pygame.image.load("backroundstart.jpg")       # sets all the backrounds
backroundstart = backroundstart.convert_alpha()                # converts the image for faster blitting
backroundend = pygame.image.load("backroundend.jpg")
backroundend = backroundend.convert_alpha()
backroundselect = pygame.image.load("backroundselect.jpg")
backroundselect = backroundselect.convert_alpha()
win_screen_p1 = pygame.image.load("P1 WIN.jpg")           # sets all the backrounds
win_screen_p1 = win_screen_p1.convert_alpha()
win_screen_p2 = pygame.image.load("P2 WIN.jpg")
win_screen_p2 = win_screen_p2.convert_alpha()
music_select_screen = pygame.image.load("music_screen.jpg")
music_select_screen = music_select_screen.convert_alpha()
instruction_screen_1 = pygame.image.load("p1screen.jpg")
instruction_screen_1 = instruction_screen_1.convert_alpha()
instruction_screen_2 = pygame.image.load("p2screen.jpg")
instruction_screen_2 = instruction_screen_2.convert_alpha()
####### all sound properties ##########
gravitysound = pygame.mixer.Sound("gravity.wav")
warioSelect = pygame.mixer.Sound("warioSelect.wav")
marioSelect = pygame.mixer.Sound("marioSelect.wav")
luigiSelect = pygame.mixer.Sound("luigiSelect.wav")
waluigiSelect = pygame.mixer.Sound("waluigiSelect.wav")
music_1 =pygame.mixer.Sound("music_1.ogg")
music_2 =pygame.mixer.Sound("music_2.ogg")
music_3 =pygame.mixer.Sound("music_3.ogg")
music_4 =pygame.mixer.Sound("music_4.ogg")
music_choice = music_1  # checks if the players picked the music for the game
# ---------------------------------------#
# functions                              #
# ---------------------------------------#
def redrawGameWindow(gameWindow):     # this redraws the game window
    background1.draw(gameWindow)
    background2.draw(gameWindow)
    for tile in tiles[chosenTile]:   # draws each tile on screen
        tile.draw(gameWindow)
    for tile in tiles[nextChosenTile]:  # draws each tile that will be on screen (next tiles)
        tile.draw(gameWindow)
    player1.draw(gameWindow)   # draws player 1
    if two_player == True:             # if 2 player is selected this will draw the second player
        player2.draw(gameWindow)
    if one_player == True:              # the score will be shown only in 1 player mode
         txt(str(score), WIDTH -60, 50, 50, RED)                  # shows the actual score
         txt("SCORE:", WIDTH - 310, 50, 50, RED)                  # shows the name score
    pygame.display.update()

############# CUSTOM TXT FEATURE ############
def text_objects(text,font,colour):
    textSurface = font.render(text,True,colour)
    return textSurface, textSurface.get_rect()
def txt(text,x,y,size,colour):     # custom text function with custom font
    largeText = pygame.font.Font("Android 101.ttf",size)
    TextSurf, TextRect = text_objects(text,largeText,colour)
    TextRect.center = (x,y)
    gameWindow.blit(TextSurf,TextRect)
#########################################
def start_screen():   # this is the function for the start screen
    gameWindow.blit(backroundstart, (0, 0))   # blits the img for the start screen
    pygame.display.update()

def instructions():
    if one_player == True:
        gameWindow.blit(instruction_screen_1, (0,0))
    if two_player == True:
        gameWindow.blit(instruction_screen_2, (0,0))

def end_screen():   # the function for the end screen
    if one_player == True:   # if 1 player mode is on, it will display this backround
        gameWindow.blit(backroundend, (0, 0))
        txt("SCORE", WIDTH//2, 375, 40, RED)          # displays final score
        txt(str(score), WIDTH // 2+150, 375, 40, RED) #
    if two_player == True and player1_win:   # if 2 player mode is on and player 1 wins, it displays this
        gameWindow.blit(win_screen_p1, (0, 0))
    elif two_player == True and player2_win:    # if 2 player mode is on and player 2 wins, it displays this
        gameWindow.blit(win_screen_p2, (0, 0))
    pygame.display.update()

def character_choosing_screen_p1(chr_choice):     # 1 player chosing screen
    gameWindow.blit(backroundselect, (0,0))
    keys = pygame.key.get_pressed()    # declares what a key is
    if one_player == True:       # if 1 player mode is on
        txt("PLAYER 1 CHOOSES:", WIDTH // 2, 50, 50, RED)          #   text for instructions
        if keys[pygame.K_1]:
            chr_choice = character_one      # when the button is pressed, it picks this character
            marioSelect.play(0)             # when the character is picked, the sound is played
        if keys[pygame.K_2]:
            chr_choice = character_two
            luigiSelect.play(0)
        if keys[pygame.K_3]:
            chr_choice = character_three
            warioSelect.play(0)
        if keys[pygame.K_4]:
            chr_choice = character_four
            waluigiSelect.play(0)
    return chr_choice   # returns the choice made by the player

def character_choosing_screen_p2(player1_choice, player2_choice, chr_choice, chr_choice2):   # 2 player chosing screen
    gameWindow.blit(backroundselect, (0,0))
    keys = pygame.key.get_pressed()
    if two_player == True:
        if player1_choice == False and player2_choice == False: # if player 1 and 2 have not gone, player 1 selects
            txt("PLAYER 1 CHOOSES:", WIDTH // 2, 50, 50, RED)
            if keys[pygame.K_1]:
                chr_choice = character_one      # when the button is pressed, it picks this character
                marioSelect.play(0)             # when the character is picked, the sound is played
                player1_choice = True           # makes the player 1 choice true
                player2_choice = True
            if keys[pygame.K_2]:
                chr_choice = character_two
                luigiSelect.play(0)
                player1_choice = True
                player2_choice = True
            if keys[pygame.K_3]:
                chr_choice = character_three
                warioSelect.play(0)
                player1_choice = True
                player2_choice = True
            if keys[pygame.K_4]:
                chr_choice = character_four
                waluigiSelect.play(0)
                player1_choice = True
                player2_choice = True
        if player1_choice == True and player2_choice == True:     # allows the second player to pick
            txt("PLAYER 2 CHOOSES:", WIDTH // 2, 50, 50, RED)
            if keys[pygame.K_1]:
                marioSelect.play(0)
                chr_choice2 = character_one
            if keys[pygame.K_2]:
                luigiSelect.play(0)
                chr_choice2 = character_two
            if keys[pygame.K_3]:
                warioSelect.play(0)
                chr_choice2 = character_three
            if keys[pygame.K_4]:
                waluigiSelect.play(0)
                chr_choice2 = character_four
    return player1_choice, player2_choice ,chr_choice, chr_choice2

def music_screen(music_choice):     # allows the player to choose the music
    gameWindow.blit(music_select_screen, (0, 0))      # blits the music screen backround
    keys = pygame.key.get_pressed()
    if keys[pygame.K_1]:           # WHEN BUTTON IS PRESSED IT CHOOSES THE MUSIC
        music_choice = music_1
    if keys[pygame.K_2]:
        music_choice = music_2
    if keys[pygame.K_3]:
        music_choice = music_3
    if keys[pygame.K_4]:
        music_choice = music_4
    return music_choice # returns the music choice
#---------------------------------------#
#   classes                             #
#---------------------------------------#
class Player():   # this class creates the player
    '''
    This class is the structure of the player.
    The players imgs get loaded and determined
    with this class and the x and y as well.
    This class works on the animation and
    the collision of the player as well.
    '''
    def __init__(self,x,y, marioPic):
        self.mario = pygame.image.load("images/mario1.png")
        self.h = 63  #
        self.w = 33  #
        self.x = x  # dimensions of mario
        self.y = y  #
        self.vy = 10
        self.marioPicNum = 1  # current picture of mario
        self.marioDir = "right"  # direction in which mario is facing
        self.marioPic = [0] * 12  # 12 pictures represent all animated views of mario
        for i in range(12):  # these pictures must be in the same folder
            self.marioPic[i] = pygame.image.load("images/" + marioPic + str(i) + ".png")
        self.nextLeftPic = [1, 2, 3, 1, 1, 1, 1, 1, 1, 1, 1,1]
        self.nextRightPic = [4, 4, 4, 4, 5, 6, 7, 5, 4, 4, 4, 4]
    def draw(self, gameWindow):
        gameWindow.blit(self.marioPic[self.marioPicNum], (self.x, self.y))
    def collide(self, other):
        if pygame.Rect(self.x, self.y, self.w, self.h).colliderect(other.x, other.y, other.w, other.h):
            return True
    def flip(self):
        for i in range(len(self.marioPic)):
            self.marioPic[i] = pygame.transform.flip(self.marioPic[i], False, True)

class Tile():   # this class creates the tiles for the level
    '''
    This class is the structure of the tiles and platforms.
    Each of the tiles will be apart of a section and the
    sections will be called randomly to challenge the player.
    '''
    def __init__(self,x,y,w,h):    # initialises the attributes for the tile
        self.x = x     # X CORD OF THE TILE
        self.y = y     # Y CORD OF THE TILE
        self.w = w     # WIDTH OF THE TILE
        self.h = h     # HEIGHT OF THE TILE
        self.img = pygame.image.load("line.png")
        self.img = pygame.transform.scale(self.img, (self.w, self.h))   # SCALE THE IMG FOR EACH TILE
        self.img = self.img.convert_alpha()
        self.img2 = pygame.image.load("line2.jpg")
        self.img2 = pygame.transform.scale(self.img2, (self.w, self.h))  # SCALE THE IMG FOR EACH TILE
        self.img2 = self.img2.convert_alpha()
        self.img3 = pygame.image.load("line3.jpg")
        self.img3 = pygame.transform.scale(self.img3, (self.w, self.h))  # SCALE THE IMG FOR EACH TILE
        self.img3 = self.img3.convert_alpha()
    def draw(self, gameWindow):   # draws the tile
        if self.w == self.h:
            gameWindow.blit(self.img, (self.x, self.y))
        elif self.h > self.w:
            gameWindow.blit(self.img3, (self.x, self.y))
        else:
            gameWindow.blit(self.img2, (self.x, self.y))
    def move(self, speed):   # moves the tile
        self.x -= speed

class Level():   # this class creates the levels
    '''
    This class is the structure that compiles all
    of the tiles into a level, draws the levels,
    and moves the levels
    '''
    def __init__(self, number, tileL):
        self.number=number
        self.tileList=tileL
        self.passLevel=False

    def draw(self, gameWindow): # draws the tile
        for i in self.tileList:
            i.draw(gameWindow)
    def move(self, speed):      # moves the tile/tiles
        for i in self.tileList:
            i.move_tile(speed)

class Sprite(pygame.sprite.Sprite):   # this class moves the backround
    """ (fileName)
        Visible game object.
        Inherits Sprite to use its Rect property.
        See Sprite documentation here:
        http://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Sprite
    """

    def __init__(self, picture=None, x=0, y=0, speed=0):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.speed = speed
        self.visible = False
        image1 = pygame.image.load(picture)
        self.image = pygame.transform.scale(image1, (800, 600))
        self.rect = self.image.get_rect()  # each sprite has a rect attribute - a list of 4 numbers: left, top, width, height
        self.update()
    def spawn(self, x, y):
        """ Assign coordinates to the center of the object and make it visible.
        """
        self.x = x - self.rect.width / 2
        self.y = y - self.rect.height / 2
        self.rect = pygame.Rect(self.x, self.y, self.rect.width, self.rect.height)
        self.visible = True
        self.update()
    def draw(self, surface):
        surface.blit(self.image, self.rect)
    def update(self):  # after moving a sprite, the rect attribute must be updated
        self.rect = pygame.Rect(self.x, self.y, self.rect.width, self.rect.height)
    def moveLeft(self, shift):
        self.x -= shift
        self.update()
# ---------------------------------------#
#       more properties                  #
# ---------------------------------------#
####################### These are all of the starting segments #############################
tiles1 = [Tile(0, 100, 300, 50), Tile(400, 100, 300, 50), Tile(0, 450, 200, 50), Tile(200, 450, 200, 50),
          Tile(500, 450, 300, 50), Tile(600, 225, 50, 150), Tile(200, 225, 50, 150)]

tiles2 = [Tile(0, 400, 200, 50),Tile(200, 400, 200, 50),Tile(400, 400, 200, 50),Tile(600, 400, 200, 50), Tile(0, 200, 200, 50), Tile(200, 350, 50, 50),
          Tile(350, 250, 50, 50), Tile(500, 350, 50, 50), Tile(650, 250, 50, 50), Tile(200, 200, 200, 50), Tile(400, 200, 200, 50),Tile(600, 200, 200, 50),]

tiles3 = [Tile(0, 100, 200, 50),Tile(200, 100, 200, 50),Tile(400, 100, 200, 50),Tile(600, 100, 200, 50), Tile(200, 150, 200, 50),Tile(400, 150, 200, 50), Tile(300, 200, 200, 50),
          Tile(0, 450, 200, 50),Tile(200, 450, 200, 50),Tile(400, 450, 200, 50),Tile(600, 450, 200, 50), Tile(200, 400, 200, 50),Tile(400, 400, 200, 50), Tile(300, 350, 200, 50)]

tiles4 = [Tile(0, 150, 200, 50), Tile(200, 100, 100, 50), Tile(300, 50, 200, 50), Tile(500, 100, 100, 50),
          Tile(600, 150, 200, 50),
          Tile(0, 400, 200, 50), Tile(200, 450, 100, 50), Tile(300, 500, 200, 50), Tile(500, 450, 100, 50),
          Tile(600, 400, 200, 50)]

tiles5 = [Tile(0, 100, 200, 50),Tile(200, 100, 200, 50),Tile(400, 100, 200, 50),Tile(600, 100, 200, 50), Tile(150, 225, 50, 150), Tile(450, 225, 50, 150),
          Tile(300, 350, 50, 100), Tile(300, 150, 50, 100), Tile(600, 350, 50, 100), Tile(600, 150, 50, 100)
          ,Tile(0, 450, 200, 50),Tile(200, 450, 200, 50),Tile(400, 450, 200, 50),Tile(600, 450, 200, 50)]
#### Chooses next random segments to create an "infinite loop" for the game ########
tiles=[tiles1,tiles2,tiles3, tiles4, tiles5]
chosenTile = random.randint(0,len
(tiles) - 1)
nextChosenTile = random.randint(0, len(tiles) - 1)
while (nextChosenTile == chosenTile):
    nextChosenTile = random.randint(0, len(tiles) - 1)
for tile in tiles[nextChosenTile]:   # for each tile in the next list of tiles to be shown
    tile.x += WIDTH   # puts the tile 800 pixels to so that it could create the new segment when it gets out of screen
################# BACKROUND PROPERTIES #######################
BACKGROUND_SPEED = 5   # speed of moving backround
background1 = Sprite("backround1.jpg")     #
background1.spawn(WIDTH/2,HEIGHT/2)        #
background2 = Sprite("backround2.jpg")     #
background2.spawn(WIDTH/2+background1.rect.width,HEIGHT/2) #
###################################################
player1 = Player(WIDTH // 3, 300, chr_choice)       # creates the two players
player2 = Player(WIDTH // 3-20, 300, chr_choice2)   # creates the two players
two_player = False      # checks if the gamemode is 1 player or 2 player
one_player = False      # checks if the gamemode is 1 player or 2 player
clock = pygame.time.Clock()
FPS = 30
isOnGround = False   # checks if on ground
isOnGround2 = False  #
inPlay = False          # checks if the game is in play or not
game_over = False   # checks if the game is over
player2_win = False   # Checks if player 2 wins
player1_win = False   # Checks if player 1 wins
choice_lobby = False    # when true, the lobby for the character choice starts and allows the player to pick the character
music_lobby = False     # when true, the lobby for the music starts and allows the player to pick the music
start = True    # when start == true, the start up screen runs
instruction_lobby = False
# ---------------------------------------#
# main program                           #
# ---------------------------------------#
while start == True: # this is the start screen
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]: # if escape is pressed it ends the whole program
            start = False
        start_screen()
        if keys[pygame.K_1]:   # if the input key 1 is pressed then 1 player mode is activated
            one_player = True
            start = False
            instruction_lobby = True
        elif keys[pygame.K_2]: # if the input key 2 is pressed then 2 player mode is activated
            two_player = True
            start = False
            instruction_lobby = True  # after the input key is pressed, it moves to the instruction lobby and ends the loop of the start screen
    pygame.display.update()

while instruction_lobby == True: # in the instruction lobby, depending on what mode the game is in displays the controls for that mode
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            instruction_lobby = False
        instructions() # calls the instruction screen lobby to blit the img
        if keys[pygame.K_SPACE]: # if space is pressed, the instruction lobby switches over to the choice lobby
            instruction_lobby = False
            choice_lobby = True
    pygame.display.update()

while choice_lobby == True:
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            choice_lobby = False
        if two_player == True: # if two player mode is on, then it calls the 2 player select function and creates the 2 players a second time
            player1_choice, player2_choice, chr_choice, chr_choice2 = character_choosing_screen_p2(player1_choice,player2_choice,chr_choice,chr_choice2)
            player1 = Player(WIDTH // 3, 300, chr_choice)  #
            player2 = Player(WIDTH // 3 - 20, 300, chr_choice2)  # creates the two player
        elif one_player == True: # if one player mode is on, it creates the first player and allows them to change their character multiple times
            chr_choice = character_choosing_screen_p1(chr_choice)
            player1 = Player(WIDTH // 3, 300, chr_choice)  #
        if keys[pygame.K_SPACE]: # when everyone is done selecting and space is pressed, you enter the music lobby and out of the choice lobby
            music_lobby = True
            choice_lobby = False
    pygame.display.update()

while music_lobby == True:  # with this loop you can choose the lobby music
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            choice_lobby = False
        music_choice = music_screen(music_choice)  # calling the function and taking music choice as a paramiter and setting it = to the call of the function
        if keys[pygame.K_SPACE]:
            inPlay = True
            music_lobby = False
            startTime = time.time()  # starts the time
        pygame.display.update()
music_choice.play(0) # this plays the ogg file that was selected during the time of the music lobby

while inPlay == True:  # this is the main game
    if score >= 500 and score < 1300: # depending on the score, the speed changes from the background
        BACKGROUND_SPEED = 8 #  all speeds have to be divisible by 800 so the redrawing of the tiles can work
    elif score >= 1300 and score < 2000:
        BACKGROUND_SPEED = 10
    elif score >= 2000:
        BACKGROUND_SPEED = 16
    redrawGameWindow(gameWindow) # calls the function to draw the players, background, tiles, and score
    clock.tick(FPS)
    pygame.event.clear()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]: # ends the program if esc is pressed
        inPlay = False
    player1.marioDir = "right" # sets the direction of the players
    if player1.y:
        player1.marioPicNum = player1.nextRightPic[player1.marioPicNum] # sets the picture number of the players
    player2.marioDir = "right"
    if player2.y:
        player2.marioPicNum = player2.nextRightPic[player2.marioPicNum]
    if one_player == True and (keys[pygame.K_UP] and isOnGround): # if one player mode is true then the controlls are just up arrows
        gravitysound.play(0) # plays the gravity switching sound every time the button is pressed
        player1.flip() # flips the img of the player
        GRAVITY *= -1 # flips the gravity
        player1.y += GRAVITY # adds gravity to the player
    if two_player == True: # if two player mode is true
        if (keys[pygame.K_p] and isOnGround): # player 1 flip gravity is p
            gravitysound.play(0)
            player1.flip()
            GRAVITY *= -1
            player1.y += GRAVITY
        if (keys[pygame.K_q] and isOnGround2): # player 2 flip gravity is q
            gravitysound.play(0)
            player2.flip()
            GRAVITY2 *= -1
            player2.y += GRAVITY2
    for tile in tiles[chosenTile]: # for each tile in the list of tiles
        isOnGround = player1.collide(tile) # sets the isOnGround variable to collision with each tile
        if isOnGround==True: # if the player is on the ground
            if(GRAVITY>0): # if the gravity is positive
                player1.y = tile.y - player1.h + 1  # regular collision with tiles
            elif(GRAVITY<0): # if it is negative
                player1.y = tile.y + tile.h - 1  # collision for upside down/inverted
            break
    if (not isOnGround): # if the player is not on the ground ( checks for collision in the air)
        for tile in tiles[nextChosenTile]: # checks for each tile in the next chosen tiles
            isOnGround = player1.collide(tile)
            if isOnGround == True:
                if (GRAVITY > 0):
                    player1.y = tile.y - player1.h + 1
                elif (GRAVITY < 0):
                    player1.y = tile.y + tile.h - 1
                break
    if (isOnGround == None):
        isOnGround = False
    if two_player == True:
        for tile in tiles[chosenTile]:
            isOnGround2 = player2.collide(tile)
            if isOnGround2==True:
                if(GRAVITY2>0):
                    player2.y = tile.y - player2.h + 1
                elif(GRAVITY2<0):
                    player2.y = tile.y + tile.h - 1
                break
        if (not isOnGround2):
            for tile in tiles[nextChosenTile]:
                isOnGround2 = player2.collide(tile)
                if isOnGround2 == True:
                    if (GRAVITY2 > 0):
                        player2.y = tile.y - player2.h + 1
                    elif (GRAVITY2 < 0):
                        player2.y = tile.y + tile.h - 1
                    break
        if (isOnGround2 == None):
            isOnGround2 = False
    for tile in tiles[chosenTile]:  # for each tile in the chosen tiles
        tile.move(BACKGROUND_SPEED) # the tiles move to the left by the background speen
        if pygame.Rect(player1.x, player1.y, player1.w, player1.h).colliderect(tile.x, tile.y + 7, tile.w + 10, tile.h - 14): # checks for collision with each tile
            player1.x -= BACKGROUND_SPEED # if they collide, the player is pushed back by the background speen
        if two_player == True:
            if pygame.Rect(player2.x, player2.y, player2.w, player2.h).colliderect(tile.x, tile.y + 7, tile.w + 10, tile.h - 14):
                player2.x -= BACKGROUND_SPEED
    for tile in tiles[nextChosenTile]: # checks for each tile in the next chosen tiles
        tile.move(BACKGROUND_SPEED)
        if pygame.Rect(player1.x, player1.y, player1.w, player1.h).colliderect(tile.x, tile.y + 7, tile.w + 10, tile.h - 14):
            player1.x -= BACKGROUND_SPEED
        if two_player == True:
            if pygame.Rect(player2.x, player2.y, player2.w, player2.h).colliderect(tile.x, tile.y + 7, tile.w + 10, tile.h - 14):
                player2.x -= BACKGROUND_SPEED
    if(tiles[chosenTile][0].x == -WIDTH): # if the lvl has passed, the score is + 50 for each segment
        score += 50
        for tile in tiles[chosenTile]: # each tile is + 800 A.K.A. Width as to spawn it in front creating an infinite effect
            tile.x += WIDTH
        chosenTile = random.randint(0, len(tiles) - 1) # chooses a new random lvl
        while (nextChosenTile == chosenTile):
            chosenTile = random.randint(0, len(tiles) - 1)
        for tile in tiles[chosenTile]:
            tile.x += WIDTH
    if (tiles[nextChosenTile][0].x == -WIDTH):
        score += 50
        for tile in tiles[nextChosenTile]:
            tile.x += WIDTH
        nextChosenTile = random.randint(0, len(tiles) - 1)
        while (nextChosenTile == chosenTile):
            nextChosenTile = random.randint(0, len(tiles) - 1)
        for tile in tiles[nextChosenTile]:
            tile.x += WIDTH
    if isOnGround: # if the player is on the ground the player velocity is 0
        player1.vy = 0
    else: # if they are not on the ground, gravity is added and the y changes based on the velocity
        player1.vy = player1.vy + GRAVITY
        player1.y = player1.y + player1.vy
    if two_player == True:
        if isOnGround2:
            player2.vy = 0
        else:
            player2.vy = player2.vy + GRAVITY2
            player2.y = player2.y + player2.vy
    background1.moveLeft(BACKGROUND_SPEED) # moves background1 to the left  #
    if background1.x < -background1.rect.width:                             #   this segment moves the background to create a loop effect
        background1.x = background2.rect.width - BACKGROUND_SPEED           #   so the background never ends
    background2.moveLeft(BACKGROUND_SPEED)# moves background2 to the left   #
    if background2.x < -background2.rect.width:                             #
        background2.x = background1.rect.width - BACKGROUND_SPEED           #
    if one_player == True:  # checks if one player mode is on
        if player1.x < 0-player1.w or player1.y >HEIGHT or player1.y < 0: # if the player is out of the screen, game over
            game_over = True
            inPlay = False
    if two_player == True: # if two player mode is on
        if player1.x < 0-player1.w or player1.y >HEIGHT or player1.y < 0:  # checks if the player 1 is off the screen and sets winner to player 2
            game_over = True
            inPlay = False
            player2_win = True
        if player2.x < 0-player2.w or player2.y >HEIGHT or player2.y < 0:# checks if the player 2 is off the screen and sets winner to player 1            game_over = True
            inPlay = False
            game_over = True
            player1_win = True
while game_over == True: # when the game is over
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]: # esc closes the program
            game_over = False
    end_screen() # calls the end screen funcion
# ---------------------------------------#
pygame.quit()