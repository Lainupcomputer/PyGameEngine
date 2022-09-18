#  Copyright (c) 2022.
class Swap:
    def __init__(self):
        # game var default- 1 // Entrypoint
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

