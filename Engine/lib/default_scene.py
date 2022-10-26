#  Copyright (c) 2022.

from Engine.lib.interface import animation_no_collision, version_information, Button, Text
from Engine.lib.player import Player
from Engine.lib.map import Map
import pygame
import sys


# loading/splash screen == game_status -1
def splash(screen, resource_pack, control_set, swap, clk):
    loading_indicator = animation_no_collision(screen, resource_pack.load_animation)
    jobs = 5
    while True:
        screen.blit(pygame.transform.scale(resource_pack.load_background, (1280, 720)), (0, 0))
        Text(screen, (400, 300)).render(text="Tile Walker", size=100, color=(200, 20, 20), font="alagard")
        version_information(screen, swap.local_version)
        control_set.handle_window()
        loading_indicator.draw((490, 540))
        loading_indicator.tick()
        jobs -= 1
        if jobs < 0:
            swap.game_status = 0
            break

        pygame.display.flip()
        clk.tick(1)


# main_menu screen == game_status 0
def main_menu(screen, resource_pack, control_set, swap, console, clk):
    # overwrite font
    font = "alagard"
    while True:

        control_set.handle_window()
        screen.blit(resource_pack.menu_background, (0, 0))
        version_information(screen, swap.local_version)

        # button play game
        b_play = Button(screen, resource_pack.btn_background, 426, 120, "Play", text_center=True, font=font)
        if b_play.check_collision(control_set.get_mouse_pos()):
            if swap.mouse_left_click:
                swap.game_status = 1337
                control_set.reset_mouse()
        # button player & saves
        b_pl_sv = Button(screen, resource_pack.btn_background, 426, 240, "Player & Saves", text_center=True, font=font)
        if b_pl_sv.check_collision(control_set.get_mouse_pos()):
            if swap.mouse_left_click:
                control_set.reset_mouse()
        # button settings
        b_settings = Button(screen, resource_pack.btn_background, 426, 360, "Settings", text_center=True, font=font)
        if b_settings.check_collision(control_set.get_mouse_pos()):
            if swap.mouse_left_click:
                control_set.reset_mouse()
        # button quit game
        b_quit = Button(screen, resource_pack.btn_background, 426, 480, "Quit", text_center=True, font=font)
        if b_quit.check_collision(control_set.get_mouse_pos()):
            if swap.mouse_left_click:
                pygame.quit()
                sys.exit()

        # console loop
        console.main_loop()

        if swap.game_status != 0:
            break

        # update
        pygame.display.flip()
        clk.tick(30)


# endless mode == game_status 1
def endless_mode(screen, resource_pack, control_set, swap, console, clk):
    map = Map(screen, swap, "endless")
    map.map_parser()
    player = Player(screen, swap, resource_pack, control_set)
    # set player alive
    swap.player_alive = True

    while True:
        control_set.handle_window()
        control_set.handle_keys()
        screen.blit(resource_pack.menu_background, (0, 0))
        version_information(screen, swap.local_version)
        map.task()
        # draw player
        player.mainloop()
        console.main_loop()
        if swap.game_status != 1:
            swap.game_status = 0

        pygame.display.flip()
        clk.tick(60)