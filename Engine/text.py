# This File contains all methods to draw text onto game window
import pygame


class draw_text:
    def __init__(self, screen, pos, size=50):
        self.font = pygame.font.SysFont("comicsansms", size)
        self.screen = screen
        self.pos = pos

    def draw(self, draw_text):
        text = self.font.render(f"{draw_text}", True, (255, 0, 55))
        rect = text.get_rect()
        rect.topleft = self.pos  # place
        self.screen.blit(text, rect)


