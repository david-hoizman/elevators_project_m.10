from Floor import Floor
from Elevator import Elevator
from Building import Building
import pygame
import sys
from constants import HEIGHT_SCREEN,WIDTH_SCREEN,WHITE,HEIGHT_FLOOR,WIDTH_FLOOR,HEIGHT_ELEVATOR,ELEVATOR_IMAGE

pygame.init()
pygame.display.set_caption("Elevator")
screen = pygame.display.set_mode((WIDTH_SCREEN, HEIGHT_SCREEN))

building = Building(screen)
building.start()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(WHITE)
    building.draw()
    pygame.display.flip()
pygame.quit()
sys.exit()

            
            
            
            
            
            
 
