import pygame, sys 
from pygame.locals import QUIT 


pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption('Bouncing Ball Animation')

golcheezX = 10 
golcheezY = 200 
WHITE = (255, 255, 255)
BALLCOLOR = (255, 0, 0)
SPEEDX = 5
SPEEDY = 5

                                                             

clock = pygame.time.Clock()

while True:
    clock.tick(30)
    screen.fill(WHITE) 

    for event in pygame.event.get(): 
        if event.type == QUIT: 
            pygame.quit()
            sys.exit()
        
    
    

    pygame.draw.circle(screen, BALLCOLOR, (golcheezX, golcheezY), 10)
 
    golcheezX += SPEEDX 
    golcheezY += SPEEDY

    if golcheezX > 600 or golcheezX < 0: 
        SPEEDX *= -1 

    if golcheezY > 600 or golcheezY < 0: 
        SPEEDY *= -1

    pygame.display.update() 