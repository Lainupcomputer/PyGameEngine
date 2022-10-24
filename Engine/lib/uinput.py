#  Copyright (c) 2022.
import pygame
import sys


class UInput:
    def __init__(self, swap):
        self.swap = swap
        # switches
        self.esc_quit = True
        self.keys_disabled = False
        self.enable_mouse_click = False
        # keys
        self.ctrl_key_up = pygame.K_w
        self.ctrl_key_down = pygame.K_s
        self.ctrl_key_left = pygame.K_a
        self.ctrl_key_right = pygame.K_d
        self.ctrl_key_strg = pygame.K_LCTRL
        # not implemented
        self.ctrl_key_jump = pygame.K_SPACE
        self.ctrl_key_action = pygame.K_f
        self.ctrl_key_action_2 = pygame.K_q
        self.ctrl_key_crouch = pygame.K_c
        self.ctrl_key_inventory = pygame.K_i

    def handle_window(self):
        for event in pygame.event.get():

            # x window top_right
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # quit with ESC
            if self.esc_quit:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

            # handle mouse_click
            if self.enable_mouse_click:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # reset
                    self.swap.mouse_left_click = False
                    self.swap.mouse_right_click = False

                    if event.button == 1:
                        self.swap.mouse_left_click = True
                    elif event.button == 3:
                        self.swap.mouse_right_click = True

            # handle console
            if self.swap.open_console:
                self.keys_disabled = True
                # delete (BACKSPACE)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        self.swap.console_input = self.swap.console_input[0:-1]

                    # submit (ENTER)
                    elif event.key == pygame.K_RETURN:
                        self.swap.console_submit = True

                    # redo last input (UP-ARROW)
                    elif event.key == pygame.K_UP:
                        self.swap.console_redo = True

                    # close with F1
                    elif event.key == pygame.K_F1:
                        self.keys_disabled = False
                        self.swap.open_console = False

                    # add keypress to input
                    else:
                        self.swap.console_input += event.unicode

            # check for keypress to enable console (F1)
            else:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_F1:
                        self.swap.open_console = True

    def reset_mouse(self):
        self.swap.mouse_left_click = False
        self.swap.mouse_right_click = False

    @staticmethod
    def get_mouse_pos():
        return pygame.mouse.get_pos()

    def handle_keys(self):
        if not self.keys_disabled:
            # get all pressed keys
            keys = pygame.key.get_pressed()
            # check for keys
            # move left
            if keys[self.ctrl_key_left]:
                self.swap.player_moving_left = True
                self.swap.camera_pos[0] += 5
            # move right
            if keys[self.ctrl_key_right]:
                self.swap.player_moving_right = True
                self.swap.camera_pos[0] -= 5
            # move up
            if keys[self.ctrl_key_up]:
                self.swap.camera_pos[1] += 5
            # move down
            if keys[self.ctrl_key_down]:
                self.swap.camera_pos[1] -= 5
            # if pressed draw indicator for aim
            if keys[self.ctrl_key_strg]:
                self.swap.aim_indicator = True





            if pygame.key.get_pressed()[self.ctrl_key_jump]:
                print("jump")
            if pygame.key.get_pressed()[self.ctrl_key_action]:
                print("action")
            if pygame.key.get_pressed()[self.ctrl_key_action_2]:
                print("action2")
            if pygame.key.get_pressed()[self.ctrl_key_crouch]:
                print("crouch")
            if pygame.key.get_pressed()[self.ctrl_key_inventory]:
                print("inventory")
