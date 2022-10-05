#  Copyright (c) 2022.

import pygame

from Engine.lib.common import setup_screen
from Engine.lib.storage import Swap, Resource
from Engine.lib.uinput import UInput
from Engine.lib.console import Console
from Engine.lib.interface import version_information, Arrow_Button
from Engine.lib.player import Player

from Level.level import Level

from Engine.lib.default_scene import splash, main_menu


class Engine:
    def __init__(self, swap):
        self.screen = setup_screen()
        if pygame.get_init():
            # get Swap space -> Global Variables
            self.engine_swap = swap
            # create Control Object -> all functions for user input
            self.control_set = UInput(self.engine_swap)
            # init console Object -> all console functions !default "F1"
            self.engine_console = Console(self.screen, self.engine_swap)
            # get Resource pack -> all preloaded assets
            self.resource_pack = Resource(skin=None)
            # init clock
            self.clock = pygame.time.Clock()

    # Engine main loop // scene handler
    def main_loop(self):
        self.screen.fill((155, 155, 155))
        # read game status -> redirect to game state function
        # loading
        if self.engine_swap.game_status == -1:
            self.control_set.keys_disabled = True
            self.control_set.esc_quit = False
            self.control_set.enable_mouse_click = False
            splash(self.screen, self.resource_pack, self.control_set, self.engine_swap, self.clock)
        # main menu
        if self.engine_swap.game_status == 0:
            self.control_set.keys_disabled = True
            self.control_set.esc_quit = True
            self.control_set.enable_mouse_click = True
            main_menu(self.screen, self.resource_pack, self.control_set, self.engine_swap,
                      self.engine_console, self.clock)
        # sandbox game
        if self.engine_swap.game_status == 1337:
            self.control_set.keys_disabled = False
            self.control_set.esc_quit = True
            self.control_set.enable_mouse_click = True
            self.sandbox()

        else:
            self.engine_swap.game_status = 0
            self.control_set.keys_disabled = True
            self.control_set.esc_quit = True
            self.control_set.enable_mouse_click = True
            main_menu(self.screen, self.resource_pack, self.control_set, self.engine_swap,
                      self.engine_console, self.clock)

        pygame.display.flip()
        self.clock.tick(10)



    # sandbox == game_status 1337
    def sandbox(self):
        lvl = Level(self.screen, self.engine_swap)
        lvl.read_level_data("demo")
        player = Player(self.screen, self.engine_swap, self.resource_pack, self.control_set,  400, 300)
        btn_test = Arrow_Button(self.screen, self.resource_pack.arrow_button_animation)
        # set player alive
        self.engine_swap.player_alive = True

        while True:
            self.control_set.handle_window()
            self.control_set.handle_keys()
            self.screen.blit(self.resource_pack.menu_background, (0, 0))
            version_information(self.screen, self.engine_swap.local_version)
            # draw map
            for tile in lvl.tile_maps:
                tile.draw(self.engine_swap)
            # draw player
            player.mainloop()

            self.engine_console.main_loop()
            if self.engine_swap.game_status != 1337:
                break
            # update
            # tests
            btn_test.draw((100, 100), 90)
            btn_test.tick()
            pygame.display.flip()
            self.clock.tick(60)

