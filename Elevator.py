import pygame
from constants import ELEVATOR_IMAGE,HEIGHT_SCREEN,WIDTH_SCREEN,WIDTH_FLOOR,HEIGHT_ELEVATOR,WIDTH_ELEVATOR
class Elevator:
    def __init__(self, screen, elv_id):
        self.screen = screen
        self.elv_id = elv_id
        self.passengers = []
        self.position = None
        
    def draw(self):
        el_image = pygame.image.load(ELEVATOR_IMAGE)
        scaled_el_image  = pygame.transform.scale(el_image,(WIDTH_ELEVATOR,HEIGHT_ELEVATOR))
        el_image_rect = scaled_el_image.get_rect()
        el_image_rect.bottomleft = (WIDTH_FLOOR + self.elv_id * WIDTH_ELEVATOR,HEIGHT_SCREEN)
        self.position = el_image_rect
        self.screen.blit(scaled_el_image, el_image_rect)
  
  
  
  
    
   