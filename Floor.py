import pygame
from constants import FLOOR_BACKGROUND,BLACK
from constants import HEIGHT_SCREEN,LINE_HEIGHT,HEIGHT_FLOOR,WIDTH_FLOOR,HEIGHT_IMAGE_FLOOR,WHITE
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
        """
        self.screen = screen 
        self.floor_number = floor_number 
        self.y = (HEIGHT_FLOOR * self.floor_number) 
        self.floor_number_txt_color = BLACK 
        self.timer = 0 
        self.timer_update_time = time.time() 
        self.is_timer_on = False 
        
    def draw(self):

        image = pygame.image.load(FLOOR_BACKGROUND)
        self.scaled_image  = pygame.transform.scale(image,(WIDTH_FLOOR,HEIGHT_IMAGE_FLOOR))
        self.rect = self.scaled_image.get_rect()
        self.rect.bottom = (HEIGHT_SCREEN-((self.floor_number)*HEIGHT_FLOOR))
        self.screen.blit(self.scaled_image, self.rect)
        
        self.circle_radius = 20
        self.btn_rect  = (self.rect.centerx,self.rect.centery)
        btn = pygame.draw.circle(self.screen, (255, 255, 255), self.btn_rect , self.circle_radius)
        
        self.font_size = int(self.circle_radius) 
        font = pygame.font.Font(None,self.font_size)
        self.btn_txt = font.render(str(self.floor_number),True,self.floor_number_txt_color)
        txt_position = (btn.centerx,btn.centery)
        self.btn_txt_rect = self.btn_txt.get_rect()
        self.btn_txt_rect.center = txt_position
        self.screen.blit(self.btn_txt, self.btn_txt_rect)
        
        y = HEIGHT_SCREEN-((self.floor_number-1)*HEIGHT_FLOOR+HEIGHT_IMAGE_FLOOR+LINE_HEIGHT/2)
        if self.floor_number != 0:
            black_line =pygame.draw.line(self.screen,BLACK,(0,y),(WIDTH_FLOOR-1,y),LINE_HEIGHT)
            
        if self.timer != 0:
            font1 = pygame.font.Font(None,28)
            self.btn_txt1 = font1.render(str(self.timer),True,BLACK)
            txt_position1 = (btn.centerx - 60,btn.centery)
            self.btn_txt_rect1 = self.btn_txt1.get_rect()
            self.btn_txt_rect1.center = txt_position1
            self.screen.blit(self.btn_txt1, self.btn_txt_rect1)
            


    def update(self):
        if self.is_timer_on and time.time()-self.timer_update_time>=0.5:
                self.dec()
                self.timer_update_time = time.time()
    def dec(self):
        if self.timer > 0:
            print("*")
            self.timer -= 0.5
            self.screen.fill(WHITE, self.rect) 
            self.screen.blit(self.scaled_image, self.rect)
            btn = pygame.draw.circle(self.screen, (255, 255, 255), self.btn_rect , self.circle_radius)
            self.screen.blit(self.btn_txt, self.btn_txt_rect)
            font = pygame.font.Font(None,self.font_size)
            btn_txt = font.render(str(self.floor_number),True,self.floor_number_txt_color)
            y = HEIGHT_SCREEN-((self.floor_number-1)*HEIGHT_FLOOR+HEIGHT_IMAGE_FLOOR+LINE_HEIGHT/2)
            if self.floor_number != 0:
                black_line =pygame.draw.line(self.screen,BLACK,(0,y),(WIDTH_FLOOR-1,y),LINE_HEIGHT)
            font1 = pygame.font.Font(None,28)
            self.btn_txt1 = font1.render(str(self.timer),True,BLACK)
            self.screen.blit(self.btn_txt1, self.btn_txt_rect1)
                
        else:
            print("done")
            self.is_timer_on = False