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
        self.timer = 0
        
    def __str__(self) -> str:
        return f"{self.floor_number}"
    
    
    
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

        font1 = pygame.font.Font(None,28)
        btn_txt1 = font1.render(str(self.timer),True,BLACK)
        txt_position1 = (btn.centerx - 60,btn.centery)
        btn_txt_rect1 = btn_txt1.get_rect()
        btn_txt_rect1.center = txt_position1
        if self.timer>0:
            self.screen.blit(btn_txt1, btn_txt_rect1)
        
        
    def countDown(self):
        while self.timer>0.0:
            print(f"f: {self.floor_number} t: {self.timer}")
            self.draw()
            pygame.display.flip()
            self.timer -= 0.5
            pygame.time.delay(500)

        