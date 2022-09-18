import pygame
import sys


class Controls:
    def __init__(self):
        # switches
        self.esc_quit = True#
        self.keys_disabled = False#
        # console
        self.open_console = False##
        self.console_input = ""
        self.console_submit = False
        self.console_redo = False
        # game var default- 1
        self.game_status = -1##
        # mouse
        self.enable_mouse_click = False#
        self.mouse_left_click = False#
        self.mouse_right_click = False#

        # keys
        self.ctrl_key_up = pygame.K_w
        self.ctrl_key_down = pygame.K_s
        self.ctrl_key_left = pygame.K_a
        self.ctrl_key_right = pygame.K_d
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
                # reset
                self.mouse_left_click = False
                self.mouse_right_click = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.mouse_left_click = True
                    elif event.button == 3:
                        self.mouse_right_click = True

            # handle console if open
            if self.open_console:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        self.console_input = self.console_input[0:-1]
                    elif event.key == pygame.K_RETURN:
                        self.console_submit = True
                        #resp
                        user_input = self.console_input
                        print(user_input)
                        # close &reset
                    elif event.key == pygame.K_UP:
                        self.console_redo = True

                    # close with F1
                    elif event.key == pygame.K_F1:
                        self.open_console = False
                    else:
                        self.console_input += event.unicode

            else:
                # check for F1 -> Console
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_F1:
                        self.open_console = True

    def handle_keys(self):
        if not self.keys_disabled:
            if pygame.key.get_pressed()[self.ctrl_key_up]:
                print("up")
            if pygame.key.get_pressed()[self.ctrl_key_down]:
                print("down")
            if pygame.key.get_pressed()[self.ctrl_key_left]:
                print("left")
            if pygame.key.get_pressed()[self.ctrl_key_right]:
                print("right")
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

