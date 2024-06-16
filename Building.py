from Floor import Floor
from Elevator import Elevator
from constants import *
import json
import time

with open("settings.json", "r") as json_file:
    data = json.load(json_file)


class Building:
    
    def __init__(self, screen):
        """
        Initialize the Building object.

        Args:
            screen (pygame.Surface): The game screen surface.
 
        Attributes:
            screen (pygame.Surface): The game screen surface to which the elevator object belongs.
            floors_array (list): A list to store information about the floors in the building.
            elevators_array (list): A list to store information about the elevators in the building.
            len_floors_array (int): The length of the floors_array, indicating the total number of floors in the building.
            len_elevators_array (int): The length of the elevators_array, indicating the total number of elevators in the building.
    
        """
        self._screen = screen 
        self._floors_array = [] 
        self._elevators_array = [] 
        self._len_floors_array =  data["number_of_floors"]
        self._len_elevators_array = data["number_of_elevators"]
  
    def draw(self):
        """
        Draws the floors and elevators on the screen.

        This method creates a Floor object for each floor,
        and then draws it on the screen. Similarly, she creates 
        elevator object for each elevator, then draws it on the screen.
        """
        
        # Drawing floors
        for i in range(self._len_floors_array + EXTRA_FLOOR):
            self._floors_array.append(Floor(self._screen, i)) 
            self._floors_array[i].draw() 
        # Drawing elevators
        for i in range(self._len_elevators_array):
            self._elevators_array.append(Elevator(self._screen, i,self._floors_array[0])) 
            self._elevators_array[i].draw() 
    
    def choose_elevator(self, floor):
        """
        Choose the optimal elevator to respond to a request from a certain floor.

        This method iterates over the elevators in the building and calculates the time it would take
        for each elevator to respond to the request from the given floor. It considers factors like the 
        waiting time of the last passenger in the elevator and the distance from the elevator's current 
        position to the requested floor. The elevator with the shortest total response time is selected.

        Args:
            floor (Floor): The floor from which the request is made.

        Returns:
            Elevator : The optimal elevator to respond to the request.
        """
        min_time = float('inf') # Initialize the minimum time to infinity
        min_elv = None # Initialize the optimal elevator to None

        for elevator in self._elevators_array:
            # Calculates the waiting time until the elevator is available and the floor from which the elevator will leave
            if len(elevator.get_passengers_queue()) == 0:
                waiting_time = 0
                exit_floor = elevator.get_current_floor().get_floor_number()
            else:
                if len(elevator.get_passengers_queue()) == 1:
                    delay = DELAY_DURATION - (time.time() - elevator.get_delay_time()) 
                    final_delay = delay if delay >= 0 else DELAY_DURATION
                else:
                    final_delay = DELAY_DURATION
                waiting_time = elevator.get_passengers_queue()[-1].get_timer() + final_delay
                exit_floor = elevator.get_passengers_queue()[-1].get_floor_number()
                
            # Calculate the total time for the elevator to respond to the request
            final_time = waiting_time + abs(floor.get_floor_number() - exit_floor) * FLOOR_LENGTH_TIME 

            # Update the minimum time and optimal elevator if necessary
            if final_time < min_time:
                min_time = final_time 
                min_elv = elevator 
        
        # Assign the calculated time as the timer for the floor
        floor.set_timer(min_time)
        floor.start_timer = time.time()
        return min_elv 
    
    def call_elevator(self, floor):
        """
        Calls an elevator to respond to a request from a certain floor.

        This method selects the optimal elevator to respond to the request using the choose_elevator method,
        then enqueues the floor request into the selected elevator's queue.

        Args:
            floor (Floor): The floor from which the request is made.
        """
        floor.set_is_disable(True)  # Disable the floor button to prevent multiple requests
        elevator = self.choose_elevator(floor)  # Select the optimal elevator to respond to the request
        elevator.enqueue(floor)  # Enqueue the floor request into the selected elevator's queue


 
    
    def updateAll(self):
        """
        Update all elevators and floors in the building.

        This method iterates over all elevators in the building, updates each elevator's state,
        and draws the updated elevator image on the screen. It then iterates over all floors in 
        the building and updates their timers.
        """
        
        # Update all elevators in the building
        for elevator in self._elevators_array:
            elevator.update_elevator() 
            elevator.display_element()
    
        # Update timers for all floors in the building
        for floor in self._floors_array:
            floor.update_timer()

    def get_floors_array(self):
        return self._floors_array  

    
    
    def num_elv_in_floor(self,floor):
        """
        Returns the number of elevators currently on the specified floor.

        Parameters:
            self (Building): The building object.
            floor (Floor): The floor object to check.

        Returns:
            int: The number of elevators on the specified floor.
        """
        count = 0
        for elv in self._elevators_array:
            if elv.get_current_floor().get_floor_number() == floor.get_floor_number():
                count+=1
        return count
     