import pygame
from constants import ELEVATOR_IMAGE, HEIGHT_SCREEN, WIDTH_SCREEN, WIDTH_FLOOR, HEIGHT_ELEVATOR, HEIGHT_FLOOR,WHITE,WIDTH_ELEVATOR,GREEN,BLACK
from Floor import Floor
from Elevator import Elevator
class Building:
    
    def __init__(self, screen):
        self.screen = screen
        self.floors_array = []
        self.len_floors_array = 0
        
        self.elevators_array = []
        self.len_elevators_array = 0
        self.requests_array = []
        
    def start(self):
        self.len_floors_array = int(input("enter number of floors: ")) 
        self.len_elevators_array = int(input("enter number of elevators: "))
        
    def draw(self):
        for i in range(self.len_floors_array):
            self.floors_array.append(Floor(self.screen, i))
            self.floors_array[i].draw()
        for i in range(self.len_elevators_array):
            self.elevators_array.append(Elevator(self.screen, i))
            self.elevators_array[i].draw()
       
    def get_elevator(self,elv_id,floor_num):
        new_y = HEIGHT_SCREEN-floor_num*HEIGHT_FLOOR    
        elevator = self.elevators_array[elv_id]
        floor = self.floors_array[floor_num]
        floor.txt_color = GREEN
        self.move_elevator(elevator,new_y)
        floor.txt_color = BLACK   
               
    def move_elevator(self, elevator, new_y):
        a=-1 if elevator.y>new_y else 1 
        while elevator.y != new_y :
            elevator.y += a * HEIGHT_FLOOR/10
            pygame.time.delay(50)
            self.screen.fill(WHITE)
            self.draw()
            pygame.display.flip()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

     
     
     
     
     
     
     

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    