# This File contains all methods to draw onto game window
import pygame
from Engine import text

class Menu_Button:
    def __init__(self, screen, x, y, txt, resource_pack, offset_x=10):
        self.btn_background = resource_pack.btn_background
        rect = self.btn_background.get_rect()
        self.btn_rect = pygame.Rect(rect[0] + x, rect[1] + y, rect[2], rect[3])
        screen.blit(self.btn_background, (x, y))
        text.draw_text(screen, (x + offset_x, y + 10)).draw(txt)

    def check_collision(self, mouse):
        if self.btn_rect.collidepoint(mouse):
            return True
        else:
            return False
