from Floor import Floor
from Elevator import Elevator
import pygame
import sys
from constants import HEIGHT_SCREEN,WIDTH_SCREEN,WHITE,HEIGHT_FLOOR,WIDTH_FLOOR,HEIGHT_ELEVATOR 
number_of_floors = int(input("enter number of floors: "))
number_of_elev = int(input("enter number of elevators: "))
pygame.init()
pygame.display.set_caption("Background Image Example")
screen = pygame.display.set_mode((WIDTH_SCREEN, HEIGHT_SCREEN))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(WHITE)
    floors_array = []
    elevators_array = []
    for i in range(number_of_floors):
        floors_array.append(Floor(screen,i,WIDTH_FLOOR,(HEIGHT_FLOOR)))
        floors_array[i].draw() 
    for i in range(number_of_elev):
        elevators_array.append(Elevator(screen,i,WIDTH_FLOOR//4, HEIGHT_ELEVATOR)) 
        elevators_array[i].draw() 
    pygame.display.flip()
pygame.quit()
sys.exit()

            
            
            
            
            
            
            
            
# number_of_floors = int(input("הזן את מספר הקומות: "))
# floor_height = WINDOW_HEIGHT // number_of_floors
# floor_y = 0
# for i in range(number_of_floors):
#     # ציור קומה
#     pygame.draw.rect(screen, (0, 0, 255), (0, floor_y, SCREEN_WIDTH, floor_height))

#     # ציור פס שחור
#     pygame.draw.rect(screen, (0, 0, 0), (0, floor_y + floor_height - BLACK_STRIPE_HEIGHT, SCREEN_WIDTH, BLACK_STRIPE_HEIGHT))

#     floor_y += floor_height
