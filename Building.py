import pygame
from constants import ELEVATOR_IMAGE, HEIGHT_SCREEN, WIDTH_SCREEN, WIDTH_FLOOR, HEIGHT_ELEVATOR, HEIGHT_FLOOR
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
        self.len_floors_array = int(input("enter number of floors: ")) + 1
        self.len_elevators_array = int(input("enter number of elevators: "))
        
    def draw(self):
        for i in range(self.len_floors_array):
            self.floors_array.append(Floor(self.screen, i))
            self.floors_array[i].draw()
        for i in range(self.len_elevators_array):
            self.elevators_array.append(Elevator(self.screen, i))
            self.elevators_array[i].draw()
        


