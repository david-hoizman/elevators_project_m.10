import pygame
from constants import FLOOR_BACKGROUND,BLACK
from constants import HEIGHT_SCREEN,CIRCLE_RADIUS,LINE_HEIGHT,HEIGHT_FLOOR,WIDTH_FLOOR,HEIGHT_IMAGE_FLOOR,WHITE,RED
import time
import threading
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
        
    def create_floor_image(self):
        """
        Create the floor image.

        This method loads the floor image file, scales the image to the required size, and place it on the game window to the appropriate position.
        """
        image = pygame.image.load(FLOOR_BACKGROUND)
        self._scaled_image  = pygame.transform.scale(image,(WIDTH_FLOOR,HEIGHT_IMAGE_FLOOR))
        self._rect = self._scaled_image.get_rect()
        self._rect.bottom = (HEIGHT_SCREEN-((self._floor_number)*HEIGHT_FLOOR))
        
    def create_round_controller(self):
        """
        Create the round controller button.

        This method sets up the parameters for a round controller button, such as the circle radius and the position of the button .
        """
        self._circle_radius = CIRCLE_RADIUS
        self._controller_rect  = (self._rect.centerx,self._rect.centery)
        self._controller = pygame.draw.circle(self._screen, (WHITE), self._controller_rect , self._circle_radius)
       
    def create_floor_number_text(self):
        """
        Create the text displaying the floor number.

        This method sets up the parameters for the text displaying the floor number, such as the font size, font color, and text position.
        """
        self._font_size = int(self._circle_radius) 
        self._font_floor_number = pygame.font.Font(None,self._font_size)
        self._controller_txt = self._font_floor_number.render(str(self._floor_number),True,self._floor_number_txt_color)
        controller_txt_position = (self._controller.centerx,self._controller.centery)
        self._controller_txt_rect = self._controller_txt.get_rect()
        self._controller_txt_rect.center = controller_txt_position
        
    def create_black_line_separates(self):
        """
        Create the black line separating floors.

        This method draws a black line to visually separate each floor from the one above it.
        """
        y = HEIGHT_SCREEN-((self._floor_number-1)*HEIGHT_FLOOR+HEIGHT_IMAGE_FLOOR+LINE_HEIGHT/2)
        black_line = pygame.draw.line(self._screen,BLACK,(0,y),(WIDTH_FLOOR-1,y),LINE_HEIGHT)
         
    def create_timer_block(self):
        """
        Create the timer block.

        This method sets up the parameters for the timer block, such as the block position and color .
        """
        block_x = self._rect.x + 20  
        block_y = self._rect.centery - 20 // 2
        pygame.draw.rect(self._screen, BLACK, (block_x, block_y, 47, 27))  
          
    def create_timer_text(self):
        """
        Create the text displaying the timer value.

        This method sets up the parameters for the text displaying the timer value, such as the font size, font color, and text position.
        """
        self._font_timer = pygame.font.Font('DS-DIGI.TTF', 28)  # Replace 'path/to/your_font.ttf' with the path to your font file
        self._timer_txt = self._font_timer.render(str(round(self._timer,1)),True,RED)
        timer_txt_position = (self._rect.x + 35,self._rect.centery+2)
        self._timer_txt_rect = self._timer_txt.get_rect()
        self._timer_txt_rect.center = timer_txt_position
 
    def display_elements(self):
        """
        Display all elements associated with the floor.

        This method blits the scaled image of the floor, draws the round controller button, and displays the floor number and timer text (if timer>0) on the game screen.
        """
        self._screen.blit(self._scaled_image, self._rect)
        self._controller = pygame.draw.circle(self._screen, (255, 255, 255), self._controller_rect , self._circle_radius)
        self._controller_txt = self._font_floor_number.render(str(self._floor_number),True,self._floor_number_txt_color)
        self._screen.blit(self._controller_txt, self._controller_txt_rect)
        if self._is_timer_on and self._timer >= 0:
            self.create_timer_block()
            self._timer_txt = self._font_timer.render(str(round(self._timer,1)),True,RED)
            self._screen.blit(self._timer_txt, self._timer_txt_rect)
        if self._floor_number != 0:
            self.create_black_line_separates()
  
    def draw(self):
        """
        Draw the floor on the game screen.

        This method coordinates the creation and display of all elements associated with the floor, including the floor image, round controller button, floor number text, black line separating floors (if floor_number>0), and timer text.
        """
        self.create_floor_image()
        self.create_round_controller()
        self.create_floor_number_text()
        if self._floor_number != 0:
            self.create_black_line_separates()
        self.create_timer_text()
        self.display_elements()
    
    def update_timer(self):
        """
        Update the timer value.

        This method updates the timer value if the timer is running and if the elapsed time since the last update is equal to or greater than 0.5 seconds.
        """
        if self._is_timer_on and time.time() - self._timer_update_time >= 0.1:
                self.decrement_timer()
                self._timer_update_time = time.time()
    
    def decrement_timer(self):
        """
        Decrement the timer value.

        This method decrements the timer value by 0.5 if the timer value is greater than 0 and updates the game screen.
        """
        if self._timer > 0:
            self._timer -= 0.1
            self._screen.fill(WHITE, self._rect) 
            self.display_elements()                
        
    def change_floor_number_txt_color(self, color):
        """
        Change the color of the button of the floor.

        This method updates the color of the button text of the floor and redraws the floor to reflect the color change on the game screen.

        Args:
            color (tuple): The RGB color tuple representing the new color.
        """
        self._floor_number_txt_color = color 
        self.display_elements() 
        pygame.display.flip() 
        
        
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
