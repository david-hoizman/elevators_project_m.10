from Building import Building
import pygame
import sys
from constants import HEIGHT_SCREEN,WIDTH_SCREEN,WHITE,FPS,HEIGHT_FLOOR

pygame.init()
pygame.display.set_caption("Elevator")
screen = pygame.display.set_mode((WIDTH_SCREEN, HEIGHT_SCREEN))

building = Building(screen)
building.start()

# clock = pygame.time.Clock()
# dt =clock.tick(FPS) 
   
running = True
while running:
    screen.fill(WHITE)
    building.draw()
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            for floor in building.floors_array:
                distance = (( mouse_pos[0] - floor.btn_rect[0]) ** 2 + ( mouse_pos[1] - floor.btn_rect[1]) ** 2)  ** 0.5
                if distance <= floor.circle_radius:
                    print(HEIGHT_SCREEN-floor.floor_number*HEIGHT_FLOOR)
                    building.get_elevator(0,floor.floor_number)
                    break

pygame.quit()
sys.exit()

            
            
            
            
            
            
 
