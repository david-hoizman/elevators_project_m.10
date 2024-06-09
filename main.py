from Building import Building
import pygame
import sys
from constants import HEIGHT_SCREEN,WIDTH_SCREEN,WHITE

# Initializing pygame
pygame.init() 
pygame.display.set_caption("Elevator") 
screen = pygame.display.set_mode((WIDTH_SCREEN, HEIGHT_SCREEN)) 

# Creating a building object
building = Building(screen) 

# Setting up the main loop
running = True 

screen.fill(WHITE) 
building.draw() 
pygame.display.flip() 

# Main game loop
while running:
    
    # Handling events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 

        # Handling mouse button down event
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos() 

            # Checking if the mouse click is within a floor's button range
            for floor in building.get_floors_array():
                distance = (( mouse_pos[0] - floor.get_controller_rect()[0]) ** 2 + ( mouse_pos[1] - floor.get_controller_rect()[1]) ** 2)  ** 0.5 
                if distance <= floor.get_circle_radius() and not floor.get_is_disable():   

                    # Calling the elevator to the clicked floor
                    building.call_elevator(floor) 

    # Setting the frame rate
    pygame.time.Clock().tick(30)

    # Updating all elements in the building
    building.updateAll()     
    
    # Updating the display                   
    pygame.display.flip()
    
# Exiting pygame and the program
pygame.quit()
sys.exit() 

            
            