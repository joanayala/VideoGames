#Date: 20-sept-2021
'''
    Description: Este es nuestro primer script python con Python.
    Este script genera una ventana en Pygame con el título ¡Hello world!.
'''
#1. Importar librerías / paquetes
import pygame
import sys

#2. Inicializar Pygame
pygame.init()
#3. Dimenzionar (w x h) el tamaño de la ventana del video juego
#Configuraciones generales de la ventana (WxH, title, Color)
width = 800
height = 400
myWindow = pygame.display.set_mode(( width, height ))
pygame.display.set_caption('Number race v 1.0')
#Setear colores R (Red) G (Green) B (Blue) => HxD
#RGB => 0-255
white = pygame.Color(255,255,255)
red = pygame.Color(255,0,0)
red = (255,0,0)
green = pygame.Color(0,255,0)
blue = pygame.Color(0,0,255)
x = pygame.Color(140,217,150)
y = pygame.Color(255, 229, 143)
bgColor = (140,217,150)
#Figures
##Rectangle:
rect1 = pygame.Rect(150,300,150,50)   #x,y,w,h
rect2 = pygame.Rect(350,230,150,50)   #x,y,w,h

rect1.center = (width // 2, height // 2)

print(rect2.x)
print(rect2.y)
##Circle

##Square

#4. Mantener visible/abierta la ventana en pantalla
while True:
    for event in pygame.event.get():
       if event.type == pygame.QUIT : # valida si usuario presionó cerrar X
           pygame.quit() # Cierra la ventana
           sys.exit() #Cierra o destruye todos los procesos
    myWindow.fill(bgColor)
    pygame.draw.rect(myWindow,red,rect1) # ctx, color, rect
    pygame.draw.rect(myWindow,blue,rect2) # ctx, color, rect

    pygame.draw.rect(myWindow, green, (50, 50, 50, 50))
    pygame.draw.line(myWindow, red, (10,10), (300,10), 5)
    pygame.draw.circle(myWindow, y, (400,200), 100)
    pygame.draw.polygon(myWindow, blue, ((0, 300), (100, 200), (200,300)))

    pygame.display.update()