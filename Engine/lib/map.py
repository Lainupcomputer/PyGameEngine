#  Copyright (c) 2022.
import pygame
import logging

from Engine.lib.common import load_file, try_load_img


def grid_parser(tile_size, grid_pos):
    player_start = (400, 300)
    pox_x = int(player_start[0]) + int(tile_size) * int(grid_pos[0])
    pox_y = int(player_start[1]) + int(tile_size) * int(grid_pos[1])
    return pox_x, pox_y


class Tile:
    def __init__(self, screen, pos, gfx, animation, trespass, folder):
        self.screen = screen
        self.pos = pos
        self.gfx = gfx
        self.has_animation = animation
        self.trespass = trespass
        self.folder = folder
        self.image = None
        self.rect = None

    def draw(self, swap):
        if self.has_animation == "no":
            while self.image is None:
                self.image = try_load_img(f"Level/{self.folder}/{self.gfx}.png", convert=True, v=False)

            if self.image is not None:
                self.rect = pygame.Rect(self.pos[0] + swap.camera_pos[0], self.pos[1] + swap.camera_pos[1], 128, 128)
                self.screen.blit(pygame.transform.scale(self.image, (128, 128)), self.rect)

    def check(self, swap):
        if self.trespass == "yes":
            pass

        if self.trespass == "no":
            if self.rect.collidepoint(swap.player_pos):
                if swap.player_pos[0] > self.rect[0]:
                    # up/ down self.rect[1]
                    # r l self.rect[0] > rechts

                    print(self.rect[0])
                    print(swap.player_pos)
                    pygame.draw.rect(self.screen, (55, 255, 55), self.rect)


class Map:
    def __init__(self, screen, swap, map_folder):
        self.screen = screen
        self.swap = swap
        self.folder = map_folder
        self.tile_map = []

    def map_parser(self):
        file_data = None
        logging.info("-" * 10 + f"Map Parser started loading' {self.folder}'" + "-" * 10)
        try:
            file_data = load_file(f"Level/{self.folder}/{self.folder}.map")

        except FileNotFoundError:
            self.swap.game_status = 0
            logging.warning(f"map file: '{self.folder}'corrupted.")

        if file_data is not None:
            header = file_data[0].split(" ")
            tile_size_raw = header[0].split("=")
            tile_size = tile_size_raw[1]
            dimension_raw = header[1].split("=")
            dimension_raw_xy = dimension_raw[1].split(":")
            logging.info(f"got map:'{self.folder}', tile_size={tile_size}, "
                         f"dimension={dimension_raw_xy[0],dimension_raw_xy[1]}")
            # remove header line
            file_data.pop(0)

            for line in file_data:
                r_newline = line.replace("\n", "")
                tile_row = r_newline.split("<")
                # remove space
                tile_row.pop(0)

                print(tile_row)
                for piece in tile_row:
                    properties = piece.split(" ")
                    # grid system
                    raw_grid = properties[0].split("=")
                    grid_pos = raw_grid[1].split(":")
                    # gfx
                    raw_gfx = properties[1].split("=")
                    gfx = raw_gfx[1]
                    # animation
                    raw_animation = properties[2].split("=")
                    animation = raw_animation[1]
                    # trespass
                    raw_trespass = properties[3].split("=")
                    trespass = raw_trespass[1]
                    position = grid_parser(tile_size, grid_pos)

                    self.tile_map.append(Tile(self.screen, position, gfx, animation, trespass, self.folder))


                    print(position, gfx, animation, trespass)

            logging.info("-" * 10 + f"Map Parser done. loaded {len(self.tile_map)} tiles." + "-" * 10)

    def task(self):
        for tile in self.tile_map:
            tile.draw(self.swap)
            tile.check(self.swap)

