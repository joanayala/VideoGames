'''
    Developer: jayala
    Date: 30-sept-2021
    Description:
    Desarrollo de la versión 1.0 de un video juego de atari.
'''

#Importar librerias
import sys
import pygame

pygame.init()

#Classes
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.img_ball = pygame.image.load('images/bolita.png')
        self.rect = self.img_ball.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.centery = HEIGHT / 2
        self.speed = [5, 5] # []
    
    def pibot(self):
        #Validate Y !¡
        if self.rect.bottom >= HEIGHT or self.rect.top <=0:
            self.speed[1] = -self.speed[1]
        #Validate X <- X ->
        elif self.rect.right >= WIDTH or self.rect.left <=0:
            self.speed[0] = -self.speed[0]

        self.rect.move_ip(self.speed)   

#General settings
WIDTH = 640
HEIGHT = 480
BG_COLOR = (4, 152, 231) # (Red, Green, Blue)

screen = pygame.display.set_mode( (WIDTH,  HEIGHT) )
pygame.display.set_caption('Atari')
icon = pygame.image.load('images/main_icon.png')
pygame.display.set_icon(icon)

game_clock = pygame.time.Clock()
ball = Ball()

#Loop (Revisión cíclica de los eventos) => Listener
while True:
    game_clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #Call pibot
    ball.pibot()        
    #Set background color
    screen.fill(BG_COLOR)        
    #Draw de la ball
    screen.blit(ball.img_ball, ball.rect)        
    #Refresh de elementos en screen
    pygame.display.flip()