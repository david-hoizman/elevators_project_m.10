import pygame
from constants import *
import time
class Floor:
    
    def __init__(self, screen, floor_number):
        """
        Initialize the Floor object.

        Args:
            screen (pygame.Surface): The game screen surface.
            floor_number (int): The floor number.

        Attributes:
            screen (pygame.Surface): The game screen surface to which the floor object belongs.
            floor_number (int): The floor number.
            y (int): The vertical position of the floor object on the screen.
            floor_number_txt_color (tuple): The color of the floor number text.
            timer (float): The timer value.
            timer_update_time (float): The last time the timer was updated.
            is_timer_on (bool): Flag indicating whether the timer is running.
            is_disable (bool): Flag indicating whether the floor object is disabled (is she clicking).
        """
        self._screen = screen 
        self._floor_number = floor_number 
        self._floor_number_txt_color = BLACK 
        self._timer = 0 
        self._timer_update_time = time.time() 
        self._is_timer_on = False 
        self._is_disable = False
        self.start_timer = time.time()
        
    def create_floor_image(self):
        """
        Create the floor image.

        This method loads the floor image file, scales the image to the required size, and place it on the game window to the appropriate position.
        """
        image = pygame.image.load(FLOOR_BACKGROUND)  # Load the floor image file
        self._scaled_image  = pygame.transform.scale(image, (WIDTH_FLOOR, HEIGHT_IMAGE_FLOOR))  # Scale the image to the required size
        self._rect = self._scaled_image.get_rect()  # Get the rectangle of the scaled image
        self._rect.bottom = (HEIGHT_SCREEN - ((self._floor_number) * HEIGHT_FLOOR))  # Set the bottom position of the floor image




        
    def create_round_controller(self):
        """
        Create the round controller button.

        This method sets up the parameters for a round controller button, such as the circle radius and the position of the button .
        """
        self._circle_radius = CIRCLE_RADIUS  # Set the circle radius for the round controller button
        self._controller_rect  = (self._rect.centerx, self._rect.centery)  # Set the position of the button
        self._controller = pygame.draw.circle(self._screen, (WHITE), self._controller_rect , self._circle_radius)  # Draw the round controller button



       
    def create_floor_number_text(self):
        """
        Create the text displaying the floor number.

        This method sets up the parameters for the text displaying the floor number, such as the font size, font color, and text position.
        """
        self._font_size = int(self._circle_radius)  # Set the font size for the floor number text
        self._font_floor_number = pygame.font.Font(None, self._font_size)  # Set the font for the floor number text
        self._controller_txt = self._font_floor_number.render(str(self._floor_number), True,  self._floor_number_txt_color)  # Render the floor number text
        controller_txt_position = (self._controller.centerx, self._controller.centery)  # Set the position of the floor number text
        self._controller_txt_rect = self._controller_txt.get_rect()  # Get the rectangle of the rendered text
        self._controller_txt_rect.center = controller_txt_position  # Set the center position of the rendered text
        
    def create_black_line_separates(self):
        """
        Create the black line separating floors.

        This method draws a black line to visually separate each floor from the one above it.
        """
        y = HEIGHT_SCREEN - ((self._floor_number - 1) * HEIGHT_FLOOR + HEIGHT_IMAGE_FLOOR + LINE_HEIGHT / 2)  # Calculate the y-coordinate for the black line
        black_line = pygame.draw.line(self._screen, BLACK, (0, y), (WIDTH_FLOOR - 1, y), LINE_HEIGHT)  # Draw the black line on the screen



         
    def create_timer_block(self):
        """
        Create the timer block.

        This method sets up the parameters for the timer block, such as the block position and color .
        """
        block_x = self._rect.x + CIRCLE_RADIUS  # Calculate the x-coordinate for the timer block
        block_y = self._rect.centery - CIRCLE_RADIUS // 2  # Calculate the y-coordinate for the timer block
        pygame.draw.rect(self._screen, BLACK, (block_x, block_y, BLOCK_SIZE_X, BLOCK_SIZE_Y))  # Draw the timer block on the screen
          
    def create_timer_text(self):
        """
        Create the text displaying the timer value.

        This method sets up the parameters for the text displaying the timer value, such as the font size, font color, and text position.
        """
        self._font_timer = pygame.font.Font('DS-DIGI.TTF', FONT_TIMER_TEXT)  # Load the font for the timer text
        self._timer_txt = self._font_timer.render(str(round(self._timer, 1)), True, RED)  # Render the timer text
        timer_txt_position = (self._rect.x + 35, self._rect.centery + 2)  # Calculate the position of the timer text
        self._timer_txt_rect = self._timer_txt.get_rect()  # Get the rectangle of the rendered text
        self._timer_txt_rect.center = timer_txt_position  # Set the center position of the rendered text
 
    def display_elements(self):
        """
        Display all elements associated with the floor.

        This method blits the scaled image of the floor, draws the round controller button, and displays the floor number and timer text (if timer>0) on the game screen.
        """
        self._screen.blit(self._scaled_image, self._rect)  # Blit the scaled image of the floor on the screen
        self._controller = pygame.draw.circle(self._screen, (WHITE), self._controller_rect , self._circle_radius)  # Draw the round controller button
        self._controller_txt = self._font_floor_number.render(str(self._floor_number),True,self._floor_number_txt_color)  # Render the floor number text
        self._screen.blit(self._controller_txt, self._controller_txt_rect)  # Blit the floor number text on the screen
        if self._is_timer_on and self._timer >= 0:
            self.create_timer_block()  # Create the timer block
            self._timer_txt = self._font_timer.render(str(round(self._timer,1)),True,RED)  # Render the timer text
            self._screen.blit(self._timer_txt, self._timer_txt_rect)  # Blit the timer text on the screen
        if self._floor_number != 0:
            self.create_black_line_separates()  # Create the black line separating floors
  
    def draw(self):
        """
        Draw the floor on the game screen.

        This method coordinates the creation and display of all elements associated with the floor, including the floor image, round controller button, floor number text, black line separating floors (if floor_number>0), and timer text.
        """
        self.create_floor_image()  # Create the floor image
        self.create_round_controller()  # Create the round controller button
        self.create_floor_number_text()  # Create the floor number text
        if self._floor_number != 0:
            self.create_black_line_separates()  # Create the black line separating floors
        self.create_timer_text()  # Create the timer text
        self.display_elements()  # Display all elements associated with the floor
    
    def update_timer(self):
        """
        Update the timer value.

        This method updates the timer value if the timer is running and if the time elapsed since the last update is greater than 0.
        """
        diff = time.time() - self.start_timer  # Calculate the time difference since the last timer update
        if diff > 0 and self._is_timer_on:  # Check if the timer is running and the time difference is positive
            self._timer -= diff  # Update the timer value
            self.start_timer = time.time()  # Update the start time for the timer
            self._screen.fill(WHITE, self._rect)  # Fill the floor area with white color
            self.display_elements()  # Display all elements associated with the floor
    
        
    def change_floor_number_txt_color(self, color):
        """
        Change the color of the button of the floor.

        This method updates the color of the button text of the floor and redraws the floor to reflect the color change on the game screen.

        Args:
            color (tuple): The RGB color tuple representing the new color.
        """
        self._floor_number_txt_color = color  # Update the color of the floor number text
        self.display_elements()  # Redraw the floor to reflect the color change on the game screen
        pygame.display.flip()  # Update the display
        
        
    def get_controller_rect(self):
        return self._controller_rect  

    def get_circle_radius(self):
        return self._circle_radius  

    def get_floor_number(self):
        return self._floor_number  

    def set_timer_update_time(self, time):
        self._timer_update_time = time  

    def set_is_timer_on(self, is_timer_on):
        self._is_timer_on = is_timer_on
        self.display_elements()
        
    def set_is_disable(self, is_disable):
        self._is_disable = is_disable  
    
    def get_is_disable(self):
        return self._is_disable  
        
    def set_floor_number_txt_color(self, color):
        self._floor_number_txt_color = color  
        
    def set_timer(self, time):
        self._timer = time  
        
    def get_timer(self):
        return self._timer  
