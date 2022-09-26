#  Copyright (c) 2022.
import pygame

from Engine.lib.common import get_string_len


# draw version Information
class version_information:

    def __init__(self, screen, version):
        position = (20, 700)
        self.screen = screen
        self.font = pygame.font.Font("Engine/assets/3Dventure.ttf", 16).render(f"version : {version}", True, (55, 55, 55))
        rect = self.font.get_rect()
        # place
        rect.topleft = position
        self.screen.blit(self.font, rect)


# draw text
class Text:
    def __init__(self, screen, position):
        self.position = position
        self.screen = screen
        self.font = None

    def render(self, text, size, color, font=None):
        # if no font is set put default
        if font is None:
            self.font = pygame.font.Font("Engine/assets/3Dventure.ttf", size)
        else:
            self.font = pygame.font.Font(f"{font}", size)

        text_obj = self.font.render(f"{text}", True, color)
        rect = text_obj.get_rect()
        rect.topleft = self.position
        self.screen.blit(text_obj, rect)


class Button:

    def __init__(self, screen, resource, x, y, text, text_size=50, color=(55, 55, 55),
                 text_center=True, font=None):
        rect = resource.get_rect()
        self.rect = pygame.Rect(rect[0] + x, rect[1] + y, rect[2], rect[3])
        resource_size = resource.get_size()
        print(resource_size)

        # blit button_image
        screen.blit(resource, (x, y))
        # calculate position
        padding_x = 10
        if text_center:
            # x
            px_text = get_string_len(text) * text_size / 2
            xc = (resource_size[0] - px_text) / 2
            x += padding_x
            x += xc

            # y
            half = resource_size[1] / 2 - text_size / 2
            y += half
        # draw text on top of background img
        Text(screen, (x, y)).render(text, text_size, color, font)

    def check_collision(self, mouse):
        if self.rect.collidepoint(mouse):
            return True
        else:
            return False




# Animation Base Class
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


class Arrow_Button(Animation):
    def __init__(self, screen, resource):
        super().__init__(screen, resource)

    def draw(self, pos=(0, 0), angle=0, scale=(64, 64)):
        if self.frame < len(self.animation):
            rotate = pygame.transform.rotate(self.animation[self.frame], angle)
            self.screen.blit(pygame.transform.scale(rotate, scale), pos)

        if self.frame >= len(self.animation):
            self.frame = -1


class Toggle_Button:

    def __init__(self, screen):
        self.screen = screen

