import random
import time

import pygame


class GameBoy:


    pygame.init()
    #Set game display
    display_width = 800
    display_height = 600
    # Defining colors
    black = (0, 0, 0)
    white = (255, 255, 255)
    red = (255, 0, 0)
    green = (97, 212, 55)
    deepgreen=(53, 166, 12)
    deepred = (209, 79, 31)
    pause = False
    car_width = 73
    fps =60
    crash_sound = pygame.mixer.Sound("src/sounds/punch.wav")
    pygame.display.set_caption('UFO Crash')




    def __init__(self, display_width=None, display_height=None):


        self.gameDisplay = pygame.display.set_mode((GameBoy.display_width, GameBoy.display_height))

        self.clock = pygame.time.Clock()  # Initialze clock

        self.carImg = pygame.image.load('src/images/sc1.png')  # load car sprite
        self.carImg = pygame.transform.scale(self.carImg,(85,75))
        gameIcon = pygame.image.load('src/images/carIcon.jpg')  # sets game icon
        pygame.display.set_icon(gameIcon)
    def background(self,x,y):
        bgImg = pygame.image.load('src/images/bg1.jpg')
        bgImg = pygame.transform.scale(bgImg, (800, 600))
        self.gameDisplay.blit(bgImg,(x,y))

    def car(self,x, y ):
       self.gameDisplay.blit(self.carImg, (x, y)) #displays car sprite at x,y cordinates
    def thing(self,x, y, width, height, color):
        ship2 = pygame.image.load('src/images/sc2.png')
        ship2 = pygame.transform.scale(ship2, (95, 75))
        self.gameDisplay.blit(ship2, (x, y))

       # pygame.draw.rect(self.gameDisplay,color,[x,y,width,height]) #draws rectangle
    def things_dodged(self,count):
        font = pygame.font.SysFont("comicsansms", 25)
        text = font.render("Score: "+str(count), True, self.black)
        self.gameDisplay.blit(text,(0,0))
    def text_objects(self,text, font):
        textSurface = font.render(text, True, GameBoy.black)
        return textSurface, textSurface.get_rect()
    def message_display(self,text):
        largeText = pygame.font.Font('freesansbold.ttf', 115) #font object
        TextSurf, TextRect = self.text_objects(text, largeText) #gets font object and text rectangle object
        TextRect.center = ((GameBoy.display_width / 2), (GameBoy.display_height / 2))
        GameBoy.gameDisplay.blit(TextSurf, TextRect) # diplays the text at desired rectangle

        pygame.display.update()
        time.sleep(2)

    """
    msg: What do you want the button to say on it.
    x: The x location of the top left coordinate of the button box.
    y: The y location of the top left coordinate of the button box.
    w: Button width.
    h: Button height.
    ic: Inactive color (when a mouse is not hovering).
    ac: Active color (when a mouse is hovering).
    """
    def button(self,msg, x, y, w, h, ic, ac, action=None):
        mouse = pygame.mouse.get_pos() #get mouse position x,y
        click = pygame.mouse.get_pressed() #which mouse button was clicked
        #print("*",click)
        if x + w > mouse[0] > x and y + h > mouse[1] > y: #if mouse curson within boxes x,y
            pygame.draw.rect(self.gameDisplay, ac, (x, y, w, h))
            #if left clicked
            if click[0]==1 and action != None :
                self.doaction(action)
        else:
            pygame.draw.rect(self.gameDisplay, ic, (x, y, w, h))

        smallText = pygame.font.SysFont("comicsansms", 20)
        textSurf, textRect = self.text_objects(msg, smallText)
        textRect.center = ((x + (w / 2)), (y + (h / 2)))
        self.gameDisplay.blit(textSurf, textRect)
    def crash(self):

        pygame.mixer.Sound.play(GameBoy.crash_sound)
        pygame.mixer.music.stop()

        largeText = pygame.font.SysFont("comicsansms", 115)
        TextSurf, TextRect = self.text_objects("You Crashed", largeText)
        TextRect.center = ((GameBoy.display_width / 2), (GameBoy.display_height / 2))
        self.gameDisplay.blit(TextSurf, TextRect)

        while True:
            for event in pygame.event.get():
                # print(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            # gameDisplay.fill(white)

            self.button("Play Again", 150, 450, 100, 50, GameBoy.green, GameBoy.deepgreen, "game_loop")
            self.button("Quit", 550, 450, 100, 50, GameBoy.red, GameBoy.deepred, "quitgame")

            pygame.display.update()
            self.clock.tick(15)
    def doaction(self,type):
        if type == "game_loop" :
            self.game_loop()
        if type =="quitgame" :
            pygame.quit()
            quit()
        if type == "unpause":
            pygame.mixer.music.unpause()
            self.game_loop()
    def paused(self):
        pygame.mixer.music.pause() #pause music

        largeText = pygame.font.SysFont("comicsansms", 115)
        TextSurf, TextRect = self.text_objects("Paused", largeText)
        TextRect.center = ((GameBoy.display_width / 2), (GameBoy.display_height / 2))
        self.gameDisplay.blit(TextSurf, TextRect)

        while pause:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            # gameDisplay.fill(white)

            self.button("Continue", 150, 450, 100, 50, GameBoy.green, GameBoy.deepgreen, "unpause")
            self.button("Quit", 550, 450, 100, 50, GameBoy.red, GameBoy.deepred, "quitgame")

            pygame.display.update()
            self.clock.tick(15)
    def game_intro(self):
        intro = True

        while intro:
            for event in pygame.event.get():
                #print(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            #fill white screen
            self.gameDisplay.fill(GameBoy.white)
            #print text
            largeText = pygame.font.SysFont("comicsansms", 115)
            TextSurf, TextRect = self.text_objects("UFO Crash", largeText)
            TextRect.center = ((GameBoy.display_width / 2), (GameBoy.display_height / 2))
            self.gameDisplay.blit(TextSurf, TextRect)

            smalltext = pygame.font.SysFont("comicsansms", 40)
            TextSurf, TextRect = self.text_objects("Debapriyos", smalltext)
            TextRect.center = ((GameBoy.display_width / 2), (GameBoy.display_height / 3))
            self.gameDisplay.blit(TextSurf, TextRect)
            #Create buttons
            self.button("GO!",150,450,100,50,GameBoy.green,GameBoy.deepgreen,"game_loop")
            self.button("Quit", 550, 450, 100, 50, GameBoy.red, GameBoy.deepred,"quitgame")


            #update screen
            pygame.display.update()
            self.clock.tick(15)
    #game loop--------------------------------------------------------
    def game_loop(self):
        global pause
        pause = False
        pygame.mixer.music.load("src/sounds/ambient.mp3")
        pygame.mixer.music.play(-1)
        gameExit = False
        x_change = 0
        x = (GameBoy.display_width * 0.45)
        y = (GameBoy.display_height * 0.8)
        thing_startx = random.randrange(0,GameBoy.display_width)
        thing_starty = -600
        thing_speed = 4
        thing_width =80
        thing_height = 60
        thingCount =1
        dodged = 0

        h=600
        x2 = 0
        y2 = 0

        x1 = 0
        y1 = -h



        while not gameExit:

            for event in pygame.event.get():
                print(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x_change = -5
                    if event.key == pygame.K_RIGHT:
                        x_change = 5
                    if event.key == pygame.K_ESCAPE :
                        print("escape pressed")
                        pause = True
                        self.paused()

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        x_change = 0

            x += x_change # mouse changes
            #background scrolling---
            y1 += 5
            y2 += 5
            self.background(x2,y2)
            self.background(x1,y1)
            if y2 > h:
                y2 = -h
            if y1 > h:
                y1 = -h
            #---------------------------

            self.thing(thing_startx,thing_starty,thing_width,thing_height,(97, 212, 55)) #create enemy
            thing_starty += thing_speed #add speed 7pixel to Y
            #print(thing_startx ,thing_starty ,thing_speed)
            self.car(x, y) #display car
            self.things_dodged(dodged) #score update
            #crashes if character gets out of screen--------------------
            if x > self.display_width - self.car_width or x < 0:
                self.crash()
            #when the enemy block crosses the screen *******************
            if(thing_starty>self.display_height):  #if block reaches the end of screen regenerate new block at new postion
                thing_starty = 0 - thing_height # reset y to some negative value so that it gives player some time
                thing_startx = random.randrange(0,(self.display_width-100)) # generate random starting postion
                dodged = dodged + 1 # add to score
                thing_speed = thing_speed +1 # more speed
                #thing_width = thing_width + (dodged * 1.2) #make block wider

            #collison
            if y < thing_starty + thing_height:
                print('y crossover')

                if x > thing_startx and x < thing_startx + thing_width or x + GameBoy.car_width > thing_startx and x + GameBoy.car_width < thing_startx + thing_width:
                    print('x crossover')
                    self.crash()

            pygame.display.flip()
            pygame.display.update()
            self.clock.tick(GameBoy.fps)


#---------------MAIN--------------------------------------------------------------------------######
obj = GameBoy()
obj.game_intro()
obj.game_loop()
pygame.quit()
quit()