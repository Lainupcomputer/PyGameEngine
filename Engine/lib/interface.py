#  Copyright (c) 2022.
import pygame


class version_information:

    def __init__(self, screen, version):
        self.screen = screen
        self.font = pygame.font.SysFont("comicsansms", 12).render(f"Version:{version}", True, (55, 55, 55))
        rect = self.font.get_rect()
        rect.topleft = (20, 700)  # place
        self.screen.blit(self.font, rect)


class Animation:
    def __init__(self, screen, resource):
        self.screen = screen
        # get preloaded Animation images as list
        self.animation = resource
        # decides index of self.animation
        self.frame = 0

    def tick(self):
        self.frame += 1


class animation_no_collision(Animation):

    def __init__(self, screen, resource):
        super().__init__(screen, resource)

    def draw(self, pos=(0, 0)):
        if self.frame < len(self.animation):
            self.screen.blit(self.animation[self.frame], pos)
        if self.frame >= len(self.animation):
            self.frame = -1

    def tick(self):
        self.frame += 1


class version_information:

    def __init__(self, screen, version):
        self.screen = screen
        self.font = pygame.font.SysFont("comicsansms", 12).render(f"Version:{version}", True, (55, 55, 55))
        rect = self.font.get_rect()
        rect.topleft = (20, 700)  # place
        self.screen.blit(self.font, rect)
