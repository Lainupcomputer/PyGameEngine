import pygame

# VARIABLES
SCREEN_SIZE = (1280, 720)
VSYNC = 1

WINDOW_TITLE = "l-engine"
WINDOW_ICON = pygame.image.load("Engine/assets/ico.ico")


# Function
def setup_screen():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE, VSYNC)
    pygame.display.set_caption(WINDOW_TITLE)
    pygame.display.set_icon(WINDOW_ICON)
    return screen
