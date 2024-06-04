import pygame
import threading
from constants import ELEVATOR_IMAGE,HEIGHT_SCREEN,BLACK,WIDTH_FLOOR,HEIGHT_ELEVATOR,WIDTH_ELEVATOR,HEIGHT_FLOOR,WHITE,GREEN,DING_SOUND
class Elevator:
    
    def __init__(self, screen, elv_id):
        self.screen = screen
        self.elv_id = elv_id
        self.passengers_queue = []
        self.rect = None # מיקום המעלית
        self.y = HEIGHT_SCREEN # Y-מיקום המעלית בציר ה
        self.available = True #האם המעלית זמינה כעת
        self.current_floor = 0
        
    def __str__(self) -> str:
        return f"{self.elv_id}"
    
    
    
    
    
    def draw(self):
        el_image = pygame.image.load(ELEVATOR_IMAGE)
        scaled_el_image  = pygame.transform.scale(el_image,(WIDTH_ELEVATOR, HEIGHT_ELEVATOR))
        self.rect = scaled_el_image.get_rect()
        self.rect.bottomleft = (WIDTH_FLOOR + self.elv_id * WIDTH_ELEVATOR ,self.y)
        self.screen.blit(scaled_el_image, self.rect)
 
    def get_elevator(self, floor):
        self.available = False
        # print(self.passengers_queue[len(self.passengers_queue)-1])
        self.move_elevator(HEIGHT_SCREEN - floor.floor_number  * HEIGHT_FLOOR)
        self.change_btn_color(floor, BLACK)
        # self.play_sound()
        self.current_floor = floor.floor_number
        pygame.time.delay(2000)
        self.passengers_queue.pop(0)

        self.available = True
        self.check_queue()
        # elve.check_queue(self.passengers_queue[0])
        
    def enqueue(self, floor):
        self.passengers_queue.append(floor)
        self.change_btn_color(floor, GREEN)
        thread = threading.Thread(target=floor.countDown)
        thread.start()
        self.check_queue()
        
    def check_queue(self):
        if self.available == True and len(self.passengers_queue) != 0:  
            self.get_elevator(self.passengers_queue[0])
            
    def move_elevator(self, new_y):
        print(new_y)
        a = -1 if self.y > new_y else 1 
        while self.y != new_y:
            self.y += a * HEIGHT_FLOOR
            pygame.time.delay(500)
            self.clear()
            self.draw()
            pygame.display.flip()
        # self.current_floor = (HEIGHT_SCREEN - new_y)/HEIGHT_ELEVATOR
        print(f"=={self.current_floor}")
    
    
    def change_btn_color(self, floor, color):
        floor.txt_color = color
        floor.draw()
        pygame.display.flip()
    
    def clear(self):
        square_color = WHITE 
        square_width = WIDTH_ELEVATOR
        square_height = HEIGHT_SCREEN
        square_x = (WIDTH_FLOOR + self.elv_id * WIDTH_ELEVATOR) 
        square_y = (0)                        
        pygame.draw.rect(self.screen, square_color, (square_x, square_y, square_width, square_height))
     
    def play_sound(self):
        sound = pygame.mixer.Sound(DING_SOUND)
        sound.play()