import pygame
import time

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
    carSpeed = 0
    gameExit = False
    
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
                
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    xChange = 0
        
        x += xChange
            
        gameDisplay.fill(white)
        car(x, y)

        if x > displayWidth - carWidth or x < 0:
            crash()
    
        pygame.display.update()
        clock.tick(60)


gameLoop()
pygame.quit()
quit()