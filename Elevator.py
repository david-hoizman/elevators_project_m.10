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
            current_floor (Floor): The current floor where the elevator is located.
            is_in_delay (bool): Flag indicating whether the elevator is in a delay state.
        """
        self.screen = screen 
        self.elv_id = elv_id 
        self.passengers_queue = [] 
        self.rect = None 
        self.elv_color = WHITE
        self.y = HEIGHT_SCREEN 
        self.dest_y = self.y 
        self.is_available = True 
        self.current_floor = current_floor 
        self.is_in_delay = False 

    def create_elevator_image(self):
        """
        Create the elevator image.

        Loads the elevator image file, scales the image to the required size, and sets the position of the elevator image on the game window according to the elevator ID.
        """
        el_image = pygame.image.load(ELEVATOR_IMAGE) 
        self.scaled_el_image  = pygame.transform.scale(el_image,(WIDTH_ELEVATOR, HEIGHT_ELEVATOR)) 
        self.rect = self.scaled_el_image.get_rect() 
        self.rect.bottomleft = (WIDTH_FLOOR + self.elv_id * WIDTH_ELEVATOR ,self.y)
     
    def display_element(self):
        """
        Display the elevator image on the game screen.

        This method blits the scaled elevator image onto the game screen at the specified position.
        """
        pygame.draw.rect(self.screen, self.elv_color, self.rect.inflate(0, 0), border_radius=2)
        self.screen.blit(self.scaled_el_image, self.rect) 
        
        
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
        direction = -1 if self.y > self.dest_y else 1 

        # Check if the elevator is not yet at its destination
        if self.y != self.dest_y:
            self.screen.fill(WHITE, self.rect) 
            self.rect.y += direction * 4
            self.y = self.rect.y
            
        # If the elevator reaches its destination and is not available and not in delay state
        elif self.y == self.dest_y and self.is_available == False and self.is_in_delay == False:
            # Play sound and initiate delay after arrival
            self.play_sound() 
            self.change_btn_color(self.current_floor,BLACK) 
            self.elv_color = RED
            self.is_in_delay = True 
            timer = threading.Timer(2.0, self.after_delay) 
            timer.start() 
            
        # If the elevator is available, handle passenger requests
        elif self.is_available == True:
            self.check_queue() 

    def after_delay(self):
        """
        Perform actions after the delay period following elevator arrival.

        This method removes the first passenger from the elevator's queue, sets the elevator as available, resets the delay state, and checks for any remaining passenger requests.
        """
        self.passengers_queue.pop(0) 
        self.elv_color = WHITE
        self.is_available = True 
        self.is_in_delay = False 
        self.check_queue() 
        
    def get_elevator(self, floor):
        """
        Initiate elevator movement to a specified floor.

        This method sets the elevator as unavailable, updates the current floor, and calculates the destination vertical position based on the specified floor.

        Args:
            floor (Floor): The target floor to which the elevator should move.
        """
        self.is_available = False 
        self.elv_color = GREEN
        self.current_floor = floor 
        self.dest_y = HEIGHT_SCREEN - (floor.floor_number+1)  * HEIGHT_FLOOR 
   
    def enqueue(self, floor):
        """
        Add a floor to the elevator's passenger queue and initiate elevator movement.

        This method appends the specified floor to the elevator's passenger queue, changes the button color to green, and initiates elevator movement to handle the request.

        Args:
            floor (Floor): The floor to be added to the elevator's passenger queue.
        """
        self.passengers_queue.append(floor) 
        self.change_btn_color(floor, GREEN) 
        self.check_queue() 
        floor.timer_update_time = time.time()  
        floor.is_timer_on = True
 
    def check_queue(self):
        """
        Check the elevator's passenger queue and initiate elevator movement if available.

        This method checks if the elevator is available and if there are any pending requests in the passenger queue. If both conditions are met, it initiates elevator movement to handle the first request in the queue.
        """
        if self.is_available == True and len(self.passengers_queue) != 0:  
            self.current_floor.is_disable = False
            self.get_elevator(self.passengers_queue[0]) 
            
    def change_btn_color(self, floor, color):
        """
        Change the color of the button associated with a floor.

        This method updates the color of the button text associated with the specified floor and redraws the floor to reflect the color change on the game screen.

        Args:
            floor (Floor): The floor whose button color should be changed.
            color (tuple): The RGB color tuple representing the new color.
        """
        floor.floor_number_txt_color = color 
        floor.draw() 
        pygame.display.flip() 
    
    def play_sound(self):
        """
        Play a sound effect.

        This method load and plays a sound to indicate the arrival of an elevator.
        """
        sound = pygame.mixer.Sound('ding.mp3') 
        sound.play() 
        
