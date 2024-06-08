import pygame
from constants import FLOOR_BACKGROUND,BLACK
from constants import HEIGHT_SCREEN,CIRCLE_RADIUS,LINE_HEIGHT,HEIGHT_FLOOR,WIDTH_FLOOR,HEIGHT_IMAGE_FLOOR,WHITE,RED
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
            is_disable (bool): Flag indicating whether the floor object is disabled.
        """
        self.screen = screen 
        self.floor_number = floor_number 
        # self.y = (HEIGHT_FLOOR * self.floor_number) 
        self.floor_number_txt_color = BLACK 
        self.timer = 0 
        self.timer_update_time = time.time() 
        self.is_timer_on = False 
        self.is_disable = False
        
    def create_floor_image(self):
        """
        Create the floor image.

        This method loads the floor image file, scales the image to the required size, and place it on the game window to the appropriate position.
        """
        image = pygame.image.load(FLOOR_BACKGROUND)
        self.scaled_image  = pygame.transform.scale(image,(WIDTH_FLOOR,HEIGHT_IMAGE_FLOOR))
        self.rect = self.scaled_image.get_rect()
        self.rect.bottom = (HEIGHT_SCREEN-((self.floor_number)*HEIGHT_FLOOR))
        
    def create_round_controller(self):
        """
        Create the round controller button.

        This method sets up the parameters for a round controller button, such as the circle radius and the position of the button .
        """
        self.circle_radius = CIRCLE_RADIUS
        self.controller_rect  = (self.rect.centerx,self.rect.centery)
        self.controller = pygame.draw.circle(self.screen, (WHITE), self.controller_rect , self.circle_radius)
       
    def create_floor_number_text(self):
        """
        Create the text displaying the floor number.

        This method sets up the parameters for the text displaying the floor number, such as the font size, font color, and text position.
        """
        self.font_size = int(self.circle_radius) 
        self.font_floor_number = pygame.font.Font(None,self.font_size)
        self.controller_txt = self.font_floor_number.render(str(self.floor_number),True,self.floor_number_txt_color)
        controller_txt_position = (self.controller.centerx,self.controller.centery)
        self.controller_txt_rect = self.controller_txt.get_rect()
        self.controller_txt_rect.center = controller_txt_position
        
    def create_black_line_separates(self):
        """
        Create the black line separating floors.

        This method draws a black line to visually separate each floor from the one above it.
        """
        y = HEIGHT_SCREEN-((self.floor_number-1)*HEIGHT_FLOOR+HEIGHT_IMAGE_FLOOR+LINE_HEIGHT/2)
        black_line = pygame.draw.line(self.screen,BLACK,(0,y),(WIDTH_FLOOR-1,y),LINE_HEIGHT)
         
    def create_timer_block(self):
        """
        Create the timer block.

        This method sets up the parameters for the timer block, such as the block position and color .
        """
        block_x = self.rect.x + 20  
        block_y = self.rect.centery - 20 // 2
        pygame.draw.rect(self.screen, BLACK, (block_x, block_y, 47, 27))  
          
    def create_timer_text(self):
        """
        Create the text displaying the timer value.

        This method sets up the parameters for the text displaying the timer value, such as the font size, font color, and text position.
        """
        self.font_timer = pygame.font.Font('DS-DIGI.TTF', 28)  # Replace 'path/to/your_font.ttf' with the path to your font file
        self.timer_txt = self.font_timer.render(str(self.timer),True,RED)
        timer_txt_position = (self.rect.x + 45,self.rect.centery+2)
        self.timer_txt_rect = self.timer_txt.get_rect()
        self.timer_txt_rect.center = timer_txt_position
 
    def display_elements(self):
        """
        Display all elements associated with the floor.

        This method blits the scaled image of the floor, draws the round controller button, and displays the floor number and timer text (if timer>0) on the game screen.
        """
        self.screen.blit(self.scaled_image, self.rect)
        self.controller = pygame.draw.circle(self.screen, (255, 255, 255), self.controller_rect , self.circle_radius)
        self.controller_txt = self.font_floor_number.render(str(self.floor_number),True,self.floor_number_txt_color)
        self.screen.blit(self.controller_txt, self.controller_txt_rect)
        if self.timer != 0:
            self.create_timer_block()
            self.timer_txt = self.font_timer.render(str(self.timer),True,RED)
            self.screen.blit(self.timer_txt, self.timer_txt_rect)
        if self.floor_number != 0:
            self.create_black_line_separates()
  
    def draw(self):
        """
        Draw the floor on the game screen.

        This method coordinates the creation and display of all elements associated with the floor, including the floor image, round controller button, floor number text, black line separating floors (if floor_number>0), and timer text.
        """
        self.create_floor_image()
        self.create_round_controller()
        self.create_floor_number_text()
        if self.floor_number != 0:
            self.create_black_line_separates()
        self.create_timer_text()
        self.display_elements()
    
    def update_timer(self):
        """
        Update the timer value.

        This method updates the timer value if the timer is running and if the elapsed time since the last update is equal to or greater than 0.5 seconds.
        """
        if self.is_timer_on and time.time() - self.timer_update_time >= 0.5:
                self.decrement_timer()
                self.timer_update_time = time.time()
    
    def decrement_timer(self):
        """
        Decrement the timer value.

        This method decrements the timer value by 0.5 if the timer value is greater than 0 and updates the game screen.
        """
        if self.timer > 0:
            self.timer -= 0.5
            self.screen.fill(WHITE, self.rect) 
            self.display_elements()                
        else:
            self.is_timer_on = False