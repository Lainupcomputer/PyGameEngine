#  Copyright (c) 2022.
import pygame
import math


class Player:
    def __init__(self, screen, swap, resource, control):
        self.screen = screen
        self.resource = resource
        self.swap = swap
        self.control = control
        # position on screen
        self.pos = swap.player_pos
        # animation frame
        self.frame = 0
        # image scale
        self.scale = (32, 42)

    def handle_weapon(self):
        # get mouse pos
        mouse_x, mouse_y = self.control.get_mouse_pos()
        # get relative positions
        rel_x, rel_y = mouse_x - self.swap.player_pos[0], mouse_y - self.swap.player_pos[1]
        # get angle
        angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)
        # weapon image
        player_weapon = pygame.transform.rotate(self.resource.player_weapon, angle)
        # blit image
        self.screen.blit(player_weapon, (self.swap.player_pos[0] + 15 - int(player_weapon.get_width() / 2),
                                         self.swap.player_pos[1] + 25 - int(player_weapon.get_height() / 2)))
        # draw aim line if "ctrl key pressed"
        if self.swap.aim_indicator:
            x, y = self.scale[0] / 2, self.scale[1] / 2
            pygame.draw.line(self.screen, (255, 55, 55), (self.swap.player_pos[0] + x, self.swap.player_pos[0] + y),
                             (mouse_x, mouse_y))

    def mainloop(self):
        # animation
        if self.frame + 1 >= 16:
            self.frame = 0
        self.frame += 1

        # player is moving to right side of screen
        if self.swap.player_moving_right:
            # blit player image based on frame to screen // scale it
            self.screen.blit(pygame.transform.scale(self.resource.player_walk_images[self.frame//4],
                                                    self.scale), (self.swap.player_pos[0], self.swap.player_pos[1]))

        # player is moving to left side of screen
        elif self.swap.player_moving_left:
            # blit player image based on frame and flipped on x to screen // scale it
            self.screen.blit(pygame.transform.scale(pygame.transform.flip(
                self.resource.player_walk_images[self.frame//4], True, False), self.scale),
                (self.swap.player_pos[0], self.swap.player_pos[1]))

        # player is idling
        else:
            # blit first img of player to screen
            self.screen.blit(pygame.transform.scale(self.resource.player_walk_images[0], self.scale),
                             (self.swap.player_pos[0], self.swap.player_pos[1]))

        # Jobs // set moving variables false
        self.handle_weapon()
        self.swap.player_moving_right = False
        self.swap.player_moving_left = False
        self.swap.aim_indicator = False
