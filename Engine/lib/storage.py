#  Copyright (c) 2022.
import sys
import pygame


class Swap:
    def __init__(self):
        # game var default
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


class Resource:
    def __init__(self, skin=None):
        self.skin = skin
        if not skin:
            try:
                # loading screen
                self.load_background = pygame.image.load("Engine/assets/loading/loading_background.png").convert()
                self.load_animation = [pygame.image.load("Engine/assets/loading/loading_0.png").convert_alpha(),
                                       pygame.image.load("Engine/assets/loading/loading_1.png").convert_alpha(),
                                       pygame.image.load("Engine/assets/loading/loading_2.png").convert_alpha(),
                                       pygame.image.load("Engine/assets/loading/loading_3.png").convert_alpha(),
                                       pygame.image.load("Engine/assets/loading/loading_4.png").convert_alpha()]
                # main menu
                self.menu_background = pygame.image.load("Engine/assets/main_menu/default.png").convert()
                self.btn_background = pygame.image.load("Engine/assets/main_menu/btn_ui.png").convert_alpha()
                # player
                self.player_walk_images = [pygame.image.load("Engine/assets/player/player_walk_0.png").convert_alpha(),
                                           pygame.image.load("Engine/assets/player/player_walk_1.png").convert_alpha(),
                                           pygame.image.load("Engine/assets/player/player_walk_2.png").convert_alpha(),
                                           pygame.image.load("Engine/assets/player/player_walk_3.png").convert_alpha()]
                self.player_weapon = pygame.image.load("Engine/assets/player/weapon_circle.png").convert_alpha()



                # Ui
                self.arrow_button_animation = [pygame.image.load("Engine/assets/ui/arrow_1.png").convert_alpha(),
                                               pygame.image.load("Engine/assets/ui/arrow_2.png").convert_alpha(),
                                               pygame.image.load("Engine/assets/ui/arrow_3.png").convert_alpha(),
                                               pygame.image.load("Engine/assets/ui/arrow_4.png").convert_alpha()]
            except FileNotFoundError:
                input("Verify Game Files!")
                pygame.quit()
                sys.exit()

