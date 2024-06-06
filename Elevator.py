import pygame
from constants import ELEVATOR_IMAGE,HEIGHT_SCREEN,BLACK,WIDTH_FLOOR,HEIGHT_ELEVATOR,WIDTH_ELEVATOR,HEIGHT_FLOOR,WHITE,GREEN,HEIGHT_IMAGE_FLOOR
import threading
import time
class Elevator:
    
    def __init__(self, screen, elv_id , current_floor):
        self.screen = screen 
        self.elv_id = elv_id 
        self.passengers_queue = [] 
        self.rect = None 
        self.y = HEIGHT_SCREEN 
        self.dest_y = self.y 
        self.available = True 
        self.current_floor = current_floor 
        self.is_in_delay = False 
     
    def draw(self):
        el_image = pygame.image.load(ELEVATOR_IMAGE) 
        self.scaled_el_image  = pygame.transform.scale(el_image,(WIDTH_ELEVATOR, HEIGHT_ELEVATOR)) 
        self.rect = self.scaled_el_image.get_rect() 
        self.rect.bottomleft = (WIDTH_FLOOR + self.elv_id * WIDTH_ELEVATOR ,self.y)
        self.screen.blit(self.scaled_el_image, self.rect) 
    
    def update(self):

        a = -1 if self.y > self.dest_y else 1 

    
        if self.y != self.dest_y:
            self.screen.fill(WHITE, self.rect) 
            self.rect.y += a * 4
            self.y = self.rect.y
            print("y: ",self.y)
           
        elif self.y == self.dest_y and self.available == False and self.is_in_delay == False:
            self.play_sound() 
            self.change_btn_color(self.current_floor,BLACK)
            self.is_in_delay = True 
            print("before delay")
            timer = threading.Timer(2.0, self.after_delay) 
            print("after delay")
            timer.start() 
        

        elif self.available == True:
            self.check_queue() 

    def after_delay(self):
        self.passengers_queue.pop(0) 
        self.available = True 
        self.is_in_delay = False 
        self.check_queue() 
        
    def get_elevator(self, floor):
        self.available = False 
        self.current_floor = floor 
        self.dest_y = HEIGHT_SCREEN - (floor.floor_number+1)  * HEIGHT_FLOOR 
        print("dest_y: ",self.dest_y)
        
    def enqueue(self, floor):
        self.passengers_queue.append(floor) 
        self.change_btn_color(floor, GREEN) 
        self.check_queue() 
        floor.timer_update_time = time.time()  
        floor.is_timer_on = True
    
    def check_queue(self):
        if self.available == True and len(self.passengers_queue) != 0:  
            self.get_elevator(self.passengers_queue[0]) 
        
    def change_btn_color(self, floor, color):
        floor.floor_number_txt_color = color 
        floor.draw() 
        pygame.display.flip() 
    
    def play_sound(self):
        sound = pygame.mixer.Sound('ding.mp3') 
        sound.play() 