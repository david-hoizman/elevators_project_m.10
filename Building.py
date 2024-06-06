from Floor import Floor
from Elevator import Elevator
import pygame


class Building:
    
    def __init__(self, screen):
        self.screen = screen 
        self.floors_array = [] 
        self.elevators_array = [] 

    def start(self):
        self.len_floors_array = int(input("enter number of floors: ")) 
        self.len_elevators_array = int(input("enter number of elevators: ")) 
        
    def draw(self):
        for i in range(self.len_floors_array + 1):
            self.floors_array.append(Floor(self.screen, i)) 
            self.floors_array[i].draw() 
        for i in range(self.len_elevators_array):
            self.elevators_array.append(Elevator(self.screen, i,self.floors_array[0])) 
            self.elevators_array[i].draw() 
    
    def choose_elevator(self, floor):
        min_time = float('inf') 
        min_elv = None 

        for elevator in self.elevators_array:
            if len(elevator.passengers_queue) ==0:
                waiting_time = 0
                exit_floor = elevator.current_floor.floor_number 
            else:
                waiting_time = elevator.passengers_queue[-1].timer +2 
                exit_floor = elevator.passengers_queue[-1].floor_number 

            final_time = waiting_time + abs(floor.floor_number - exit_floor) * 0.5 

            print("elevator",elevator.elv_id)
            print("waiting_time",waiting_time)
            print("exit_floor",exit_floor)
            print("final_time",final_time)

            if final_time < min_time:
                min_time = final_time 
                min_elv = elevator 
        print("=====================================")
        floor.timer = min_time 
        return min_elv 
    
    def call_elevator(self, floor):
        elev = self.choose_elevator(floor) 
        elev.enqueue(floor) 
    
    def updateAll(self):
        for elevator in self.elevators_array:
            elevator.update() 
            self.screen.blit(elevator.scaled_el_image, elevator.rect) 
        for floor in self.floors_array:
            floor.update()

    
    
    

     