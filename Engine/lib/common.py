#  Copyright (c) 2022.

import pygame
from datetime import datetime
import logging
import sys

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


# load a file into list
def load_file(file_name):
    with open(file_name, "r")as f:
        return f.readlines()


# return date_time_now_formated
def get_time_now(raw=True):
    now = datetime.now()
    date_time = now.strftime("%d/%m/%Y, %H:%M:%S")
    if raw:
        return date_time


# return length of string
def get_string_len(string):
    return len(string)


def try_load_img(path, convert=False, convert_a=False):
    try:
        logging.info(f"loading asset:'{path}'")
        if convert_a:
            img = pygame.image.load(path).convert_alpha()
        elif convert:
            img = pygame.image.load(path).convert()
        else:
            img = pygame.image.load(path)

        logging.info(f"asset:'{path}' loaded.")
        return img
    except FileNotFoundError:
        logging.critical(f"'{path}', resource not found")
        sys.exit(f"'{path}', resource not found")

