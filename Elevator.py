import pygame
from constants import *
import time
import threading
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
        self._y = HEIGHT_SCREEN + LINE_HEIGHT
        self._dest_y = self._y - HEIGHT_FLOOR
        self._is_available = True 
        self._current_floor = current_floor 
        self._is_in_delay = False 
        self._delay_time = time.time()
        self._current_time = time.time()
        self._start_move = None
        self._move_duration = None
        self.start = time.time()
        self.dir = 0

    def create_elevator_image(self):
        """
        Create the elevator image.

        Loads the elevator image file, scales the image to the required size, and sets the position of the elevator image on the game window according to the elevator ID.
        """
        el_image = pygame.image.load(ELEVATOR_IMAGE)  # Load the elevator image from file
        self._scaled_el_image = pygame.transform.scale(el_image, (WIDTH_ELEVATOR, HEIGHT_ELEVATOR - LINE_HEIGHT))  # Scale the image to the required size
        self._rect = self._scaled_el_image.get_rect()  # Get the rectangle of the scaled image
        self._rect.bottomleft = (WIDTH_FLOOR + self._elv_id * WIDTH_ELEVATOR, self._y)  # Set the position of the elevator image based on the elevator ID
     
    def display_element(self):
        """
        Display the elevator image on the game screen.

        This method blits the scaled elevator image onto the game screen at the specified position.
        """
        pygame.draw.rect(self._screen, self._elv_color, self._rect.inflate(0, 0), border_radius=2)  # Draw a rectangle around the elevator image
        self._screen.blit(self._scaled_el_image, self._rect)  # Blit the scaled elevator image onto the game screen
        
        
    def draw(self):
        """
        Draw the elevator on the game screen.

        This method coordinates the creation and display of the elevator image on the game screen.
        """
        self.create_elevator_image()
        self.display_element()
    
    def update_elevator(self):
        """
        Update the elevator position and state.

        This method is responsible for updating the position and state of the elevator. It handles various aspects of the elevator's behavior, including movement, arrival at destination, delay after arrival, and handling passenger requests.

        If the elevator is not yet moving, it initializes the movement by calculating the duration of the trip based on the distance to the destination floor and the speed of the elevator.

        During the movement, it continuously updates the position of the elevator until it reaches its destination floor. It ensures smooth movement by adjusting the position based on the elapsed time since the movement started.

        Upon reaching the destination floor, it triggers the completion of the trip, initiating actions such as playing a sound, updating the floor and elevator colors, and scheduling a delay period.

        If the elevator is available, it handles passenger requests by initiating movement to the requested floor.
        """
        # Check if the elevator is not yet moving
        if self._start_move == None:
            # Initialize start_move and move_duration for movement calculation
            self._start_move = pygame.time.get_ticks()
            self._move_duration = abs(self._dest_y - self._rect.y) / HEIGHT_FLOOR * 500 
            self.dir = DOWN if self._rect.y > self._dest_y else UP
           
           
        # Check if the elevator is not yet at its destination
        dir = DOWN if self._rect.y > self._dest_y else UP

        # Check if the elevator is still en route to its destination
        if abs(self._rect.y - self._dest_y) >= 1:
            # Clear the elevator's current position on the screen
            self._screen.fill(WHITE, self._rect) 
            # Calculate the elapsed time since movement started
            elapsed_time = pygame.time.get_ticks() - self._start_move
            remaining_duration = self._move_duration - elapsed_time 
            
            #Checking that the direction of the elevator has not changed
            if dir == self.dir: 
                self._rect.y =  self._dest_y + dir * (remaining_duration / 500) * HEIGHT_FLOOR 
            else:
                self._rect.y =  self._dest_y
                
        # If the elevator reaches its destination and is not available and not in delay state
        elif abs(self._rect.y - self._dest_y) < 1 and self._is_available == False and self._is_in_delay == False:
            self.trip_complete()
            
        # If the elevator is available, handle passenger requests
        elif self._is_available == True:
            self._start_move = None
            self.check_queue() 

    def trip_complete(self):
        self.play_sound()  # Play a sound effect indicating trip completion
        self._current_floor.change_floor_number_txt_color(BLACK)  # Change the floor button color to black
        self._elv_color = RED  # Change the elevator color to red to indicate it's in delay state
        self._is_in_delay = True  # Set the elevator in delay state
        self._current_floor.set_is_timer_on(False)  # Stop the floor timer
        self._current_floor.display_elements()  # Redraw the floor elements to reflect changes
        self._delay_time = time.time()  # Record the start time of the delay
        # Schedule actions to be performed after the delay duration
        timer = threading.Timer(DELAY_DURATION, self.after_delay)
        timer.start()
        
    def after_delay(self):
        """
        Perform actions after the delay period following elevator arrival.

        This method removes the first passenger from the elevator's queue, sets the elevator as available, resets the delay state, and checks for any remaining passenger requests.
        """
        self._start_move = None  # Reset the start_move variable to None to indicate the end of delay
        self._passengers_queue.pop(0)  # Remove the first passenger from the elevator's queue
        self._elv_color = WHITE  # Change the elevator color back to white
        self._is_available = True  # Set the elevator as available
        self._is_in_delay = False  # Reset the delay state
        self.check_queue()  # Check for any remaining passenger requests in the queue
        
    def get_elevator(self, floor):
        """
        Initiate elevator movement to a specified floor.

        This method sets the elevator as unavailable, updates the current floor, and calculates the destination vertical position based on the specified floor.

        Args:
            floor (Floor): The target floor to which the elevator should move.
        """
        self._is_available = False  # Set the elevator as unavailable
        self._elv_color = GREEN  # Change the elevator color to green to indicate movement
        self._current_floor = floor  # Update the current floor
        # Calculate the destination vertical position based on the specified floor
        self._dest_y = HEIGHT_SCREEN - (floor.get_floor_number() + EXTRA_FLOOR) * HEIGHT_FLOOR + LINE_HEIGHT
   
    def enqueue(self, floor):
        """
        Add a floor to the elevator's passenger queue and initiate elevator movement.

        This method appends the specified floor to the elevator's passenger queue, changes the button color to green, and initiates elevator movement to handle the request.

        Args:
            floor (Floor): The floor to be added to the elevator's passenger queue.
        """
        self._passengers_queue.append(floor)  # Add the specified floor to the elevator's passenger queue
        floor.change_floor_number_txt_color(GREEN)  # Change the button color to green to indicate request
        self.check_queue()  # Initiate elevator movement to handle the request
        floor.set_timer_update_time(time.time())  # Update the timer for the floor
        floor.set_is_timer_on(True)  # Start the floor timer
 
    def check_queue(self):
        """
        Check the elevator's passenger queue and initiate elevator movement if available.

        This method checks if the elevator is available and if there are any pending requests in the passenger queue. If both conditions are met, it initiates elevator movement to handle the first request in the queue.
        """
        if self._is_available == True and len(self._passengers_queue) != 0:
            # If the elevator is available and there are pending requests in the queue
            self._current_floor.set_is_disable(False)  # Enable the floor button
            self.get_elevator(self._passengers_queue[0])  # Initiate elevator movement for the first request in the queue
            
    def play_sound(self):
        """
        Play a sound effect.

        This method load and plays a sound to indicate the arrival of an elevator.
        """
        sound = pygame.mixer.Sound('ding.mp3')  # Load the sound effect
        sound.play()  # Play the loaded sound effect
        
    def get_passengers_queue(self):
        return self._passengers_queue  
    
    def get_current_floor(self):
        return self._current_floor  

    def get_delay_time(self):
        return self._delay_time
      

