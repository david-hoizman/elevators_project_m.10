import pygame
from constants import ELEVATOR_IMAGE, HEIGHT_SCREEN, WIDTH_SCREEN, WIDTH_FLOOR, HEIGHT_ELEVATOR, HEIGHT_FLOOR,WHITE,WIDTH_ELEVATOR,GREEN,BLACK
from Floor import Floor
from Elevator import Elevator
import random
import threading

class Building:
    
    def __init__(self, screen):
        self.screen = screen
        self.floors_array = []
        self.elevators_array = []
        self.available_array = []
        
 
    
    
    
    
    def start(self):
        self.len_floors_array = 5 # int(input("enter number of floors: ")) 
        self.len_elevators_array = 5 # int(input("enter number of elevators: "))
        
    def draw(self):
        for i in range(self.len_floors_array + 1):
            self.floors_array.append(Floor(self.screen, i))
            self.floors_array[i].draw()
        for i in range(self.len_elevators_array):
            self.elevators_array.append(Elevator(self.screen, i))
            self.elevators_array[i].draw()
    
    def choose_elevator(self, floor):
        min_time = float('inf')
        min_elv = None
        for elevator in self.elevators_array:
            if len(elevator.passengers_queue) ==0:
                waiting_time = 0
                exit_floor = elevator.current_floor
            else:
                waiting_time = elevator.passengers_queue[-1].timer +2
                print("fff:",waiting_time)

                exit_floor = elevator.passengers_queue[-1].floor_number
            final_time = waiting_time + abs(floor.floor_number - exit_floor) * 0.5
            if final_time < min_time:
                min_time = final_time
                min_elv = elevator
        floor.timer = min_time
        return min_elv
            
        
    
    def call_elevator(self, floor):
        elev = self.choose_elevator(floor)
        elev.enqueue(floor)
    
    def change_btn_color(self, floor, color):
        floor.txt_color = color
        floor.draw()
        pygame.display.flip()
    
    def play_sound(self):
        sound = pygame.mixer.Sound('ding.mp3')
        sound.play()
    
            
  
    
    
    
    
    
    
    

     
     
     
     
     
     
     

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    