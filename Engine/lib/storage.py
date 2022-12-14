#  Copyright (c) 2022.
import sys
import pygame
import logging
from Engine.lib.common import try_load_img


class Swap:
    def __init__(self):
        # game var default
        self.local_version = "0.0.1.1"
        # - 1 // Entrypoint
        self.game_status = -1
        # # # # # # #  CONSOLE
        self.open_console = False
        # console user input storage
        self.console_input = ""
        # true if user pressed submit (ENTER)
        self.console_submit = False
        # redo last command
        self.console_redo = False
        # history
        self.console_history = []
        # # # # # # # INPUTS
        self.mouse_left_click = False
        self.mouse_right_click = False
        self.player_moving_right = False
        self.player_moving_left = False
        self.aim_indicator = False
        # camera
        self.camera_pos = [0, 0]
        # player
        self.player_alive = False
        self.player_pos = (400, 300)


class Resource:
    def __init__(self, skin=None):
        self.skin = skin
        logging.info("-" * 10 + "Asset-Loader started. skin=" + str(self.skin) + "-" * 10)
        if not skin:
            try:
                asset_root = "Engine/assets"
                # loading screen
                self.load_background = try_load_img(f"{asset_root}/loading/loading_bg.png", convert=True)
                self.load_animation = [try_load_img(f"{asset_root}/loading/loading_0.png", convert_a=True),
                                       try_load_img(f"{asset_root}/loading/loading_1.png", convert_a=True),
                                       try_load_img(f"{asset_root}/loading/loading_2.png", convert_a=True),
                                       try_load_img(f"{asset_root}/loading/loading_3.png", convert_a=True),
                                       try_load_img(f"{asset_root}/loading/loading_4.png", convert_a=True)]
                # main menu
                self.menu_background = try_load_img(f"{asset_root}/main_menu/default.png", convert=True)
                self.btn_background = try_load_img(f"{asset_root}/main_menu/btn_ui.png", convert_a=True)
                # player
                self.player_walk_images = [try_load_img(f"{asset_root}/player/player_walk_0.png", convert_a=True),
                                           try_load_img(f"{asset_root}/player/player_walk_1.png", convert_a=True),
                                           try_load_img(f"{asset_root}/player/player_walk_2.png", convert_a=True),
                                           try_load_img(f"{asset_root}/player/player_walk_3.png", convert_a=True)]
                self.player_weapon = try_load_img(f"{asset_root}/player/weapon_circle.png", convert_a=True)
                # Ui
                self.arrow_button_animation = [try_load_img(f"{asset_root}/ui/arrow_1.png", convert_a=True),
                                               try_load_img(f"{asset_root}/ui/arrow_2.png", convert_a=True),
                                               try_load_img(f"{asset_root}/ui/arrow_3.png", convert_a=True),
                                               try_load_img(f"{asset_root}/ui/arrow_4.png", convert_a=True)]
            except FileNotFoundError:
                input("Verify Game Files!")
                pygame.quit()
                sys.exit()
        logging.info("-" * 10 + "Asset-Loader done." + "-" * 10)


