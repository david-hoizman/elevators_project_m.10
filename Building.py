import pygame
from constants import ELEVATOR_IMAGE, HEIGHT_SCREEN, WIDTH_SCREEN, WIDTH_FLOOR, HEIGHT_ELEVATOR, HEIGHT_FLOOR,WHITE,WIDTH_ELEVATOR,GREEN,BLACK
from Floor import Floor
from Elevator import Elevator



class Building:
    
    def __init__(self, screen):
        self.screen = screen
        self.floors_array = []
        self.elevators_array = []
        self.available_array = []
        
    def start(self):
        self.len_floors_array = int(input("enter number of floors: ")) 
        self.len_elevators_array = int(input("enter number of elevators: "))
        
    def draw(self):
        for i in range(self.len_floors_array + 1):
            self.floors_array.append(Floor(self.screen, i))
            self.floors_array[i].draw()
        for i in range(self.len_elevators_array):
            self.elevators_array.append(Elevator(self.screen, i))
            self.elevators_array[i].draw()
    
    def chios_elevator(self, floor):
        return self.elevators_array[0]
        # return self.elevators_array[floor]
    
    def get_elevator(self, floor):
        self.change_btn_color(floor, GREEN)
        elev = self.chios_elevator(floor.floor_number)
        elev.move_elevator(HEIGHT_SCREEN - floor.floor_number  * HEIGHT_FLOOR)
        self.change_btn_color(floor, BLACK)
        self.play_sound()
    
    def change_btn_color(self, floor, color):
        floor.txt_color = color
        floor.draw()
        pygame.display.flip()
    
    def play_sound(self):
        sound = pygame.mixer.Sound('ding.mp3')
        sound.play()
    
            
  
    
    
    
    
    
    
    

     
     
     
     
     
     
     

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    