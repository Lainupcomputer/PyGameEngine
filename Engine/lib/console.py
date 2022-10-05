#  Copyright (c) 2022.
import sys
import pygame
from Engine.lib.common import get_time_now


class Console:
    def __init__(self, screen, swap):
        self.user_text = ""
        self.fnt = pygame.font.Font(None, 32)
        self.screen = screen
        self.swap = swap

    def render(self, user_input):
        history_offset = 5
        # pop first item if list to long
        if len(self.swap.console_history) > 5:
            self.swap.console_history.pop(0)

        # draw history
        for entry in self.swap.console_history:
            pygame.draw.rect(self.screen, (51, 251, 51), (5, history_offset, 600, 30))
            h_text = self.fnt.render(entry, True, (155, 155, 155))
            self.screen.blit(h_text, (10, 5 + history_offset))
            history_offset += 30
        # draw input field
        pygame.draw.rect(self.screen, (51, 51, 51), (5, history_offset, 600, 30))
        c_text = self.fnt.render(">:", True, (255, 255, 255))
        self.screen.blit(c_text, (10, 5 + history_offset))
        u_text = self.fnt.render(user_input, True, (255, 0, 0))
        self.screen.blit(u_text, (30, 6 + history_offset))

    def main_loop(self):
        # console loop
        if self.swap.open_console:
            self.render(self.swap.console_input)

            # arrow_up = redo last command
            if self.swap.console_redo:
                self.swap.console_input = self.swap.console_history[len(self.swap.console_history) - 1]
                self.swap.console_redo = False

            # enter = Submit
            if self.swap.console_submit:
                self.process_input(self.swap.console_input)
                self.swap.console_input = ""
                self.swap.console_submit = False

    def process_input(self, ipt):
        user_input = ipt.split(" ")
        # static
        # clear command
        if user_input[0] == "clear":
            self.swap.console_history.clear()
            return True
        # exit console command
        if user_input[0] == "exit":
            self.swap.open_console = False
            return True
        # quit engine
        if user_input[0] == "quit":
            pygame.quit()
            sys.exit()
        # kill player
        if user_input[0] == "kill":
            self.swap.player_alive = False
            self.swap.console_history.append(f"{get_time_now()}> Player killed.")
            return True

        # methods with 1 argument
        if user_input[0] == "gs":
            try:
                self.swap.game_status = int(user_input[1])
                self.swap.console_history.append(f"{get_time_now()}> switched scene to {int(user_input[1])}.")

            except IndexError:
                self.swap.console_history.append(f"{get_time_now()}> Error: Index Error.")

            finally:
                return True

        # no command registerd
        else:
            self.swap.console_history.append(f"{get_time_now()}> Error: command not found.")

