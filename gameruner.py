from Building import Building
# import tkinter as tk
import sys
import threading
import pygame
# import pygame.thread
from constants import HEIGHT_SCREEN,WIDTH_SCREEN,WHITE,FPS,HEIGHT_FLOOR

pygame.init()
pygame.display.set_caption("Elevator")
screen = pygame.display.set_mode((WIDTH_SCREEN, HEIGHT_SCREEN))

building = Building(screen)
building.start()

# clock = pygame.time.Clock()
# dt =clock.tick(FPS) 

running = True

pygame.mixer.init()


screen.fill(WHITE)
building.draw()
pygame.display.flip()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            for floor in building.floors_array:
                distance = (( mouse_pos[0] - floor.btn_rect[0]) ** 2 + ( mouse_pos[1] - floor.btn_rect[1]) ** 2)  ** 0.5
                if distance <= floor.circle_radius:  
                   
                    # building.call_elevator(building.floors_array[floor.floor_number])
                  
                     # thread1 = threading.Thread(target=building.call_elevator, args=[floor])
                    #thread = threading.Thread(target=building.call_elevator, args=(floor,))
                    #thread.start()
                    thread = pygame.threads.Thread(target=building.call_elevator,args=(floor,))
                    thread.start()

                    break
                    
                    
                    # building.call_elevator(building.floors_array[floor.floor_number])                  
                   
                    

pygame.quit()
sys.exit()

            
            
            
            
            
 
