import pygame


class Map:
    def __init__(self):
        self.map = pygame.rect.Rect(0, 0, 1000, 600)
        self.map_color = pygame.color.Color((0, 120, 255))
        self.field = Field()

    def draw(self, screen: pygame.Surface, is_show_hitbox=True):
        if is_show_hitbox:
            pygame.draw.rect(screen, self.map_color, self.map, width=2)


class Field:
    CELL_SIZE = 100
    def __init__(self):
        self.field_hitbox = pygame.rect.Rect(250, 30, 710, 525)
        self.field_color = pygame.color.Color((0, 0, 255))
        self.field = [[None] * 8 for _ in range(6)]

    def draw(self, screen: pygame.Surface, is_show_hitbox=True):
        if is_show_hitbox:
            pygame.draw.rect(screen, self.field_color, self.field_hitbox, width=2)

