#  Copyright (c) 2022.
import pygame


class Player:
    def __init__(self, screen, swap, resource, x, y, width, height):
        self.screen = screen
        self.resource = resource
        self.swap = swap
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.animation_count = 0
        self.moving_right = False
        self.moving_left = False
        self.scale = (32, 42)

    def mainloop(self):
        # animation
        if self.animation_count + 1 >= 16:
            self.animation_count = 0
        self.animation_count += 1

        if self.moving_right:
            self.screen.blit(pygame.transform.scale(self.resource.player_walk_images[self.animation_count//4],
                                                    self.scale), (self.x, self.y))

        elif self.moving_left:
            self.screen.blit(pygame.transform.scale(pygame.transform.flip(
                self.resource.player_walk_images[self.animation_count//4], True, False), self.scale), (self.x, self.y))
        else:
            self.screen.blit(pygame.transform.scale(self.resource.player_walk_images[0], self.scale), (self.x, self.y))

        self.moving_right = False
        self.moving_left = False


