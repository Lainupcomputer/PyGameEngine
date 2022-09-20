import sys
import pygame


from Engine.ui import Menu_Button


from Engine.lib.common import setup_screen
from Engine.lib.storage import Swap
from Engine.lib.uinput import UInput
from Engine.lib.console import Console
from Engine.lib.resource import Resource
from Engine.lib.interface import animation_no_collision, version_information
from Engine.lib.player import Player

from Level.level import Level


class Engine:
    def __init__(self):
        self.screen = setup_screen()
        if pygame.get_init():
            # create Swap space -> Global Variables
            self.engine_swap = Swap()
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
            self.splash()
        # main menu
        if self.engine_swap.game_status == 0:
            self.control_set.keys_disabled = True
            self.control_set.esc_quit = True
            self.control_set.enable_mouse_click = True
            self.main_menu()
        # sandbox game
        if self.engine_swap.game_status == 1337:
            self.control_set.keys_disabled = True
            self.control_set.esc_quit = True
            self.control_set.enable_mouse_click = True
            self.sandbox()

        else:
            self.engine_swap.game_status = 0
            self.control_set.keys_disabled = True
            self.control_set.esc_quit = True
            self.control_set.enable_mouse_click = True
            self.main_menu()

        pygame.display.flip()
        self.clock.tick(10)

    # loading/splash screen == game_status -1
    def splash(self):
        loading_indicator = animation_no_collision(self.screen, self.resource_pack.load_animation)
        jobs = 5
        while True:
            self.screen.blit(self.resource_pack.load_background, (0, 0))
            version_information(self.screen, "1.01")
            self.control_set.handle_window()
            loading_indicator.draw((500, 640))
            loading_indicator.tick()
            jobs -= 1
            if jobs < 0:
                self.engine_swap.game_status = 0
                break

            pygame.display.flip()
            self.clock.tick(1)

    # main_menu screen == game_status 0
    def main_menu(self):
        while True:
            self.control_set.handle_window()
            self.screen.blit(self.resource_pack.menu_background, (0, 0))
            version_information(self.screen, "1.01")

            # menu buttons
            btn_play = Menu_Button(self.screen, 426, 120, "Play", self.resource_pack, 160)
            if btn_play.check_collision(pygame.mouse.get_pos()):
                if self.engine_swap.mouse_left_click:
                    print("collide play")
                    self.control_set.reset_mouse()

            btn_player_saves = Menu_Button(self.screen, 426, 240, "Player & Saves", self.resource_pack, 40)
            if btn_player_saves.check_collision(pygame.mouse.get_pos()):
                if self.engine_swap.mouse_left_click:
                    print("collide player_saves")
                    self.control_set.reset_mouse()

            btn_settings = Menu_Button(self.screen, 426, 360, "Settings", self.resource_pack, 100)
            if btn_settings.check_collision(pygame.mouse.get_pos()):
                if self.engine_swap.mouse_left_click:
                    print("collide settings")
                    self.control_set.reset_mouse()

            btn_quit = Menu_Button(self.screen, 426, 480, "QUIT", self.resource_pack, 140)
            if btn_quit.check_collision(pygame.mouse.get_pos()):
                if self.engine_swap.mouse_left_click:
                    pygame.quit()
                    sys.exit()

            self.engine_console.main_loop()

            if self.engine_swap.game_status != 0:
                break
            # update
            pygame.display.flip()
            self.clock.tick(30)

    # sandbox == game_status 1337
    def sandbox(self):
        lvl = Level(self.screen, self.engine_swap)
        lvl.read_level_data("demo")
        player = Player(self.screen, self.engine_swap, self.resource_pack,  400, 300, 32, 32)
        while True:
            self.control_set.handle_window()
            self.screen.blit(self.resource_pack.menu_background, (0, 0))
            version_information(self.screen, "1.01")
            # draw map
            for tile in lvl.tile_maps:
                tile.draw()
            # draw player
            player.mainloop()

            self.engine_console.main_loop()
            if self.engine_swap.game_status != 1337:
                break
            # update
            pygame.display.flip()
            self.clock.tick(60)

