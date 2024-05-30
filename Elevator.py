import pygame
from constants import ELEVATOR_IMAGE,HEIGHT_SCREEN,WIDTH_SCREEN,WIDTH_FLOOR,HEIGHT_ELEVATOR,WIDTH_ELEVATOR,SPEED_ELEVATOR
class Elevator:
    def __init__(self, screen, elv_id):
        self.screen = screen
        self.elv_id = elv_id
        self.passengers = []
        self.rect = None
        self.y = HEIGHT_SCREEN
     
    def draw(self):
        el_image = pygame.image.load(ELEVATOR_IMAGE)
        scaled_el_image  = pygame.transform.scale(el_image,(WIDTH_ELEVATOR, HEIGHT_ELEVATOR))
        self.rect = scaled_el_image.get_rect()
        self.rect.bottomleft = (WIDTH_FLOOR + self.elv_id * WIDTH_ELEVATOR ,self.y)
        self.screen.blit(scaled_el_image, self.rect)
 
