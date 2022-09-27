#  Copyright (c) 2022.

import pygame


class Resource:
    def __init__(self, skin=None):
        self.skin = skin
        if not skin:
            # loading screen
            self.load_background = pygame.image.load("Engine/assets/loading/default.png").convert()
            self.load_animation = [pygame.image.load("Engine/assets/loading/1.png").convert_alpha(),
                                   pygame.image.load("Engine/assets/loading/2.png").convert_alpha(),
                                   pygame.image.load("Engine/assets/loading/3.png").convert_alpha()]
            # main menu
            self.menu_background = pygame.image.load("Engine/assets/main_menu/default.png").convert()
            self.btn_background = pygame.image.load("Engine/assets/main_menu/btn_ui.png").convert_alpha()
            # player
            self.player_walk_images = [pygame.image.load("Engine/assets/player/player_walk_0.png").convert_alpha(),
                                       pygame.image.load("Engine/assets/player/player_walk_1.png").convert_alpha(),
                                       pygame.image.load("Engine/assets/player/player_walk_2.png").convert_alpha(),
                                       pygame.image.load("Engine/assets/player/player_walk_3.png").convert_alpha()]
            self.player_weapon = pygame.image.load("Engine/assets/player/player_weapon.png").convert_alpha()



            # Ui
            self.arrow_button_animation = [pygame.image.load("Engine/assets/ui/arrow_1.png").convert_alpha(),
                                           pygame.image.load("Engine/assets/ui/arrow_2.png").convert_alpha(),
                                           pygame.image.load("Engine/assets/ui/arrow_3.png").convert_alpha(),
                                           pygame.image.load("Engine/assets/ui/arrow_4.png").convert_alpha()]
