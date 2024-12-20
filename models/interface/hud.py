import pygame


class HUD:
    def __init__(self):
        self.menu_hitbox = pygame.rect.Rect(0, 0, 130, 600)
        self.menu_color = pygame.color.Color((153, 255, 51))

    def draw(self, screen: pygame.Surface, is_show_hitbox=True):
        if is_show_hitbox:
            pygame.draw.rect(screen, self.menu_color, self.menu_hitbox, width=2)