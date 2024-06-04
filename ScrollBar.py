class ScrollBar:

    def __init__(self, total_height):
        self.total_height = total_height  # גובה תוכן הניתן לגלילה
        self.height = HEIGHT_SCREEN - 100  # גובה גלגל הגלילה
        self.y_axis = 0  # מיקום גלגל הגלילה (0 למעלה)
        self.scroll_bar_rect = pygame.Rect(WIDTH_SCREEN - 20, 0, 20, self.height)

    def draw(self, screen):
        pygame.draw.rect(screen, BLACK, self.scroll_bar_rect)
        thumb_height = (self.height * (HEIGHT_SCREEN - 100)) / self.total_height
        thumb_pos = int(self.y_axis * ((HEIGHT_SCREEN - 100) - thumb_height) / self.total_height)
        thumb_rect = pygame.Rect(self.scroll_bar_rect.left, thumb_pos, self.scroll_bar_rect.width, thumb_height)
        pygame.draw.rect(screen, WHITE, thumb_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.pos[0] in range(self.scroll_bar_rect.left, self.scroll_bar_rect.right):
            self.mouse_down_y = event.pos[1]
            self.mouse_down_scroll_pos = self.y_axis

        if event.type == pygame.MOUSEMOTION and self.mouse_down_y is not None:
            mouse_y = event.pos[1]
            delta = mouse_y - self.mouse_down_y
            self.y_axis = max(0, min(self.y_axis + delta, self.total_height - (HEIGHT_SCREEN - 100)))

        if event.type == pygame.MOUSEBUTTONUP:
            self.mouse_down_y = None
