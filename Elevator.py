import pygame
from constants import ELEVATOR_IMAGE,HEIGHT_SCREEN,BLACK,WIDTH_FLOOR,HEIGHT_ELEVATOR,WIDTH_ELEVATOR,HEIGHT_FLOOR,WHITE,GREEN,RED
import threading
import time
class Elevator:
    
    def __init__(self, screen, elv_id , current_floor):
        """
        Initialize the Elevator object.

        Args:
            screen (pygame.Surface): The game screen surface.
            elv_id (int): The elevator ID.
            current_floor (Floor): The current floor where the elevator is located.

        Attributes:
            screen (pygame.Surface): The game screen surface to which the elevator object belongs.
            elv_id (int): The elevator ID.
            passengers_queue (list): The queue of passengers waiting for the elevator.
            rect (pygame.Rect or None): representing the elevator's position on the screen, initialized to None.
            y (int): The vertical position of the elevator on the screen, initialized to the height of the screen.
            dest_y (int): The destination vertical position of the elevator, initialized to the current position.
            is_available (bool): Flag indicating whether the elevator is available for use.
            current_floor (Floor): The current floor where the elevator is located (While moving, holds the floor to which the elevator travels).
            is_in_delay (bool): Flag indicating whether the elevator is in a delay state.
            delay_time (float): The timestamp indicating the time at which the elevator entered the delay state.
        """
        self._screen = screen 
        self._elv_id = elv_id 
        self._passengers_queue = [] 
        self._rect = None 
        self._elv_color = WHITE
        self._y = HEIGHT_SCREEN 
        self._dest_y = self._y 
        self._is_available = True 
        self._current_floor = current_floor 
        self._is_in_delay = False 
        self._delay_time = time.time()

    def create_elevator_image(self):
        """
        Create the elevator image.

        Loads the elevator image file, scales the image to the required size, and sets the position of the elevator image on the game window according to the elevator ID.
        """
        el_image = pygame.image.load(ELEVATOR_IMAGE) 
        self._scaled_el_image  = pygame.transform.scale(el_image,(WIDTH_ELEVATOR, HEIGHT_ELEVATOR)) 
        self._rect = self._scaled_el_image.get_rect() 
        self._rect.bottomleft = (WIDTH_FLOOR + self._elv_id * WIDTH_ELEVATOR ,self._y)
     
    def display_element(self):
        """
        Display the elevator image on the game screen.

        This method blits the scaled elevator image onto the game screen at the specified position.
        """
        pygame.draw.rect(self._screen, self._elv_color, self._rect.inflate(0, 0), border_radius=2)
        self._screen.blit(self._scaled_el_image, self._rect) 
        
        
    def draw(self):
        """
        Draw the elevator on the game screen.

        This method coordinates the creation and display of the elevator image on the game screen.
        """
        self.create_elevator_image()
        self.display_element()
    
    def update_elevator(self):
        """
        Update the elevator position.

        This method updates the position of the elevator based on its destination and handles various states such as moving, arrival at destination, delay after arrival, and handling passenger requests.
        """
        # Determine the direction of movement based on the destination positions
        direction = -1 if self._y > self._dest_y else 1 

        # Check if the elevator is not yet at its destination
        if self._y != self._dest_y:
            self._screen.fill(WHITE, self._rect) 
            self._rect.y += direction * 4
            self._y = self._rect.y
            
        # If the elevator reaches its destination and is not available and not in delay state
        elif self._y == self._dest_y and self._is_available == False and self._is_in_delay == False:
            # Play sound and initiate delay after arrival
            self.play_sound() 
            self._current_floor.change_floor_number_txt_color(BLACK)
            self._elv_color = RED
            self._is_in_delay = True 
            self._current_floor.set_is_timer_on(False)
            self._current_floor.display_elements()
            self._delay_time = time.time()
            timer = threading.Timer(2.0, self.after_delay) 
            timer.start() 
            
        # If the elevator is available, handle passenger requests
        elif self._is_available == True:
            self.check_queue() 

    def after_delay(self):
        """
        Perform actions after the delay period following elevator arrival.

        This method removes the first passenger from the elevator's queue, sets the elevator as available, resets the delay state, and checks for any remaining passenger requests.
        """
        self._passengers_queue.pop(0) 
        self._elv_color = WHITE
        self._is_available = True 
        self._is_in_delay = False 
        self.check_queue() 
        
    def get_elevator(self, floor):
        """
        Initiate elevator movement to a specified floor.

        This method sets the elevator as unavailable, updates the current floor, and calculates the destination vertical position based on the specified floor.

        Args:
            floor (Floor): The target floor to which the elevator should move.
        """
        self._is_available = False 
        self._elv_color = GREEN
        self._current_floor = floor 
        self._dest_y = HEIGHT_SCREEN - (floor.get_floor_number() + 1)  * HEIGHT_FLOOR 
   
    def enqueue(self, floor):
        """
        Add a floor to the elevator's passenger queue and initiate elevator movement.

        This method appends the specified floor to the elevator's passenger queue, changes the button color to green, and initiates elevator movement to handle the request.

        Args:
            floor (Floor): The floor to be added to the elevator's passenger queue.
        """
        self._passengers_queue.append(floor) 
        floor.change_floor_number_txt_color(GREEN)
        self.check_queue() 
        floor.set_timer_update_time(time.time())
        floor.set_is_timer_on(True)
 
    def check_queue(self):
        """
        Check the elevator's passenger queue and initiate elevator movement if available.

        This method checks if the elevator is available and if there are any pending requests in the passenger queue. If both conditions are met, it initiates elevator movement to handle the first request in the queue.
        """
        if self._is_available == True and len(self._passengers_queue) != 0:  
            self._current_floor.set_is_disable(False)
            self.get_elevator(self._passengers_queue[0]) 
            
    
    def play_sound(self):
        """
        Play a sound effect.

        This method load and plays a sound to indicate the arrival of an elevator.
        """
        sound = pygame.mixer.Sound('ding.mp3') 
        sound.play() 
        
    def get_passengers_queue(self):
        return self._passengers_queue  
    
    def get_current_floor(self):
        return self._current_floor  

    def get_delay_time(self):
        return self._delay_time
      

