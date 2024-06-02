import pygame
from constants import ELEVATOR_IMAGE,HEIGHT_SCREEN,WIDTH_SCREEN,WIDTH_FLOOR,HEIGHT_ELEVATOR,WIDTH_ELEVATOR,HEIGHT_FLOOR,WHITE,GREEN
class Elevator:
    
    def __init__(self, screen, elv_id):
        self.screen = screen
        self.elv_id = elv_id
        self.passengers_queue = [2,5,0]
        self.rect = None # מיקום המעלית
        self.y = HEIGHT_SCREEN # Y-מיקום המעלית בציר ה
        self.available = True #האם המעלית זמינה כעת

    def draw(self):
        el_image = pygame.image.load(ELEVATOR_IMAGE)
        scaled_el_image  = pygame.transform.scale(el_image,(WIDTH_ELEVATOR, HEIGHT_ELEVATOR))
        self.rect = scaled_el_image.get_rect()
        self.rect.bottomleft = (WIDTH_FLOOR + self.elv_id * WIDTH_ELEVATOR ,self.y)
        self.screen.blit(scaled_el_image, self.rect)
 

    def move_elevator(self, new_y):
      
        a = -1 if self.y > new_y else 1 
        while self.y != new_y :
            self.y += a * HEIGHT_FLOOR/10
            pygame.time.delay(50)
            self.clear()
            self.draw()
            pygame.display.flip()
       
        
    def clear(self):
        square_color = WHITE 
        square_width = WIDTH_ELEVATOR
        square_height = HEIGHT_SCREEN
        square_x = (WIDTH_FLOOR + self.elv_id * WIDTH_ELEVATOR) 
        square_y = (0)                        
        pygame.draw.rect(self.screen, square_color, (square_x, square_y, square_width, square_height))
     
        