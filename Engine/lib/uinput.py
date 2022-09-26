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
