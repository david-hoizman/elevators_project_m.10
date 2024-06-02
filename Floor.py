import pygame
from constants import FLOOR_BACKGROUND,BLACK
from constants import HEIGHT_SCREEN,LINE_HEIGHT,HEIGHT_FLOOR,WIDTH_FLOOR
class Floor:
    
    def __init__(self, screen, floor_number):
        self.screen = screen
        self.floor_number = floor_number
        self.rect = None #מיקום התמונה
        self.btn_rect = None #מיקום הפקד
        self.circle_radius = None #רדיוס הפקד
        self.y = (HEIGHT_FLOOR * self.floor_number) 
        self.txt_color = BLACK
        
    def draw(self):
        #create floor
        image = pygame.image.load(FLOOR_BACKGROUND)
        scaled_image  = pygame.transform.scale(image,(WIDTH_FLOOR,HEIGHT_FLOOR-LINE_HEIGHT+3))
        self.rect = scaled_image.get_rect()
        self.rect.bottom = (HEIGHT_SCREEN-((self.floor_number)*HEIGHT_FLOOR))
        self.screen.blit(scaled_image, self.rect)
        
        # create controller - circle button
        self.circle_radius = 20
        self.btn_rect  = (self.rect.centerx,self.rect.centery)
        btn = pygame.draw.circle(self.screen, (255, 255, 255), self.btn_rect , self.circle_radius)
        
        # create floor number - text
        font_size = int(self.circle_radius) 
        font = pygame.font.Font(None,font_size)
        btn_txt = font.render(str(self.floor_number),True,self.txt_color)
        txt_position = (btn.centerx,btn.centery)
        btn_txt_rect = btn_txt.get_rect()
        btn_txt_rect.center = txt_position
        self.screen.blit(btn_txt, btn_txt_rect)
        
        #create divider - black line
        y = HEIGHT_SCREEN-(self.floor_number*HEIGHT_FLOOR)
        if self.floor_number != 0:
            black_line =pygame.draw.line(self.screen,BLACK,(0,y),(WIDTH_FLOOR-1,y),LINE_HEIGHT)
        