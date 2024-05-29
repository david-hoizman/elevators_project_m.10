import pygame
from constants import ELEVATOR_IMAGE,HEIGHT_SCREEN,WIDTH_SCREEN,WIDTH_FLOOR
class Elevator:
    def __init__(self, screen, elv_id, width , height):
        self.screen = screen
        self.elv_id = elv_id
        self.width = width
        self.height = height
        
    def draw(self):
        el_image = pygame.image.load(ELEVATOR_IMAGE)
        scaled_el_image  = pygame.transform.scale(el_image,(self.width,self.height))
        el_image_rect = scaled_el_image.get_rect()
        # el_image_rect.bottomleft = (WIDTH_FLOOR,HEIGHT_SCREEN)
        el_image_rect.bottomleft = (WIDTH_FLOOR + self.elv_id * self.width,HEIGHT_SCREEN)
        # el_image_rect.left = (WIDTH_FLOOR)
        self.screen.blit(scaled_el_image, el_image_rect)