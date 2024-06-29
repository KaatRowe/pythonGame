import pygame
import time
import random

pygame.init()

displayWidth = 800
displayHeight = 600

gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption('Race Game')

black = (0,0,0)
white = (255,255,255)
red = (255, 0 ,0)

carWidth = 73

carImg = pygame.image.load('racecar.png')
clock = pygame.time.Clock()

def obsDodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: "+str(count), True, black)
    gameDisplay.blit(text,(0, 0))

def obstacles(obsX, obsY, obsW, obsH, color):
    pygame.draw.rect(gameDisplay, color, [obsX, obsY, obsW, obsH])

def car(x, y):
    gameDisplay.blit(carImg, (x, y))

def textObjects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def messageDisplay(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = textObjects(text, largeText)
    TextRect.center = ((displayWidth/2), (displayHeight/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)
    gameLoop()

def crash():
    messageDisplay('You Crashed')

def gameLoop():
    x = (displayWidth * 0.45)
    y = (displayHeight * 0.45)
    
    xChange = 0
    yChange = 0
    gameExit = False


    obstacleStartX = random.randrange(0, displayWidth)
    obstacleStartY = -600
    obstacleSpeed = 7
    obstacleWidth = 100
    obstacleHeight = 100

    obsCount = 1
    dodged = 0
    
    while not gameExit:
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    xChange = -5
                elif event.key == pygame.K_RIGHT:
                    xChange = 5
                elif event.key == pygame.K_UP:
                    yChange = -5
                elif event.key == pygame.K_DOWN:
                    yChange = 5
                
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    xChange = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    yChange = 0
        
        x += xChange
        y += yChange

        gameDisplay.fill(white)

        obstacles(obstacleStartX, obstacleStartY, obstacleWidth, obstacleHeight, black)
        obstacleStartY += obstacleSpeed
        car(x, y)
        obsDodged(dodged)

        if x > displayWidth - carWidth or x < 0:
            crash()
    
        if obstacleStartY > displayHeight:
            obstacleStartY = 0- obstacleHeight
            obstacleStartX = random.randrange(0, displayWidth)
            dodged += 1
            obstacleSpeed += 1
            obstacleWidth += (dodged * 1.2)

        if y < obstacleStartY+obstacleHeight:
            if x > obstacleStartX and x < obstacleStartX+obstacleWidth or x+carWidth > obstacleStartX and x+carWidth< obstacleStartX+obstacleWidth:
                crash()

        pygame.display.update()
        clock.tick(60)


gameLoop()
pygame.quit()
quit()