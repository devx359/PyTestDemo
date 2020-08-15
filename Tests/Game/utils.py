import pygame

black = (0, 0, 0)


"""
msg: What do you want the button to say on it.
x: The x location of the top left coordinate of the button box.
y: The y location of the top left coordinate of the button box.
w: Button width.
h: Button height.
ic: Inactive color (when a mouse is not hovering).
ac: Active color (when a mouse is hovering).
"""
def button(gameDisplay,msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos() #get mouse position x,y
    click = pygame.mouse.get_pressed() #which mouse button was clicked
    #print("*",click)
    if x + w > mouse[0] > x and y + h > mouse[1] > y: #if mouse curson within boxes x,y
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        #if left clicked
        if click[0]==1 and action != None :
            doaction(action)
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    gameDisplay.blit(textSurf, textRect)

