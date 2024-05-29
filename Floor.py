import pygame
from constants import FLOOR_BACKGROUND,BLACK
from constants import HEIGHT_SCREEN,LINE_HEIGHT
class Floor:
    def __init__(self, screen, floor_number ,width , height):
        self.screen = screen
        self.floor_number = floor_number
        self.width = width
        self.height = height
        
    def draw(self):
        image = pygame.image.load(FLOOR_BACKGROUND)
        scaled_image  = pygame.transform.scale(image,(self.width,self.height))
        image_rect = scaled_image.get_rect()
        image_rect.bottom = (HEIGHT_SCREEN-((self.floor_number)*self.height))
        self.screen.blit(scaled_image, image_rect)
        circle_radius = float(self.height//2.5)
        circle_position = (image_rect.centerx,image_rect.centery)
        btn = pygame.draw.circle(self.screen, (255, 255, 255), circle_position, circle_radius)
        font_size = int(circle_radius) 
        font = pygame.font.Font(None,font_size)
        btn_txt = font.render(str(self.floor_number),True,BLACK)
        txt_position = (btn.centerx,btn.centery)
        btn_txt_rect = btn_txt.get_rect()
        btn_txt_rect.center = txt_position
        self.screen.blit(btn_txt, btn_txt_rect)
        y = HEIGHT_SCREEN-(self.floor_number*self.height)
        if self.floor_number != 0:
            black_line =pygame.draw.line(self.screen,BLACK,(0,y),(self.width-1,y),LINE_HEIGHT)
