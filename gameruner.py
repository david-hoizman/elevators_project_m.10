from Building import Building
import pygame
import sys
from constants import HEIGHT_SCREEN,WIDTH_SCREEN,WHITE

pygame.init() 
pygame.display.set_caption("Elevator") 
screen = pygame.display.set_mode((WIDTH_SCREEN, HEIGHT_SCREEN)) 

building = Building(screen) 
building.start() 

running = True 

screen.fill(WHITE) 
building.draw() 
pygame.display.flip() 

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 

        
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos() 

            # מעבר על כל הקומות
            for floor in building.floors_array:
                distance = (( mouse_pos[0] - floor.btn_rect[0]) ** 2 + ( mouse_pos[1] - floor.btn_rect[1]) ** 2)  ** 0.5 # מרחק בין נקודת הלחיצה לבין הפקד
                # אם המרחק קטן מהרדיוס של הפקד
                if distance <= floor.circle_radius:  
                    # בדיקה האם יש מעלית בקומה
                    for elevator in building.elevators_array:
                        # אם יש מעלית בקומה
                        if elevator.current_floor == floor.floor_number:
                            break # יציאה מהלולאה
                   
                    building.call_elevator(floor) 

    pygame.time.Clock().tick(30)

    building.updateAll()                        
    pygame.display.flip()

pygame.quit()
sys.exit() 

            
            