#  Copyright (c) 2022.
import pygame
from Engine.lib.common import load_file


# return positions on screen from grid
def position_grid(grid, offset_x=0, offset_y=0):
    tile_size = 64
    pos_x = int(grid[0]) * tile_size + offset_x
    pos_y = int(grid[1]) * tile_size + offset_y
    return pos_x, pos_y


class Tile:

    def __init__(self, screen, grid_position, tile_style, tile_type):
        self.screen = screen
        self.grid_position = grid_position
        #self.rect = pygame.rect.Rect(grid_position[0], grid_position[1], 64, 64)
        self.tile_style = tile_style

    def draw(self, swap):
        if self.tile_style == "plain":
            self.screen.blit(pygame.transform.scale(
                pygame.image.load(f"Level/{swap.game_status}/{self.tile_style}.png").convert(), (64, 64)),
                (self.grid_position[0] + swap.camera_pos[0], self.grid_position[1] + swap.camera_pos[1]))
            #pygame.draw.rect(self.screen, (55, 55, 55), self.rect)
        else:
            #pygame.draw.rect(self.screen, (55, 255, 55), self.rect)
            pass



class Level:

    def __init__(self, screen, swap):
        self.screen = screen
        self.swap = swap
        self.tile_maps = []

    def read_level_data(self, level_name):
        level_file = False
        data_lines = load_file(f"Level/{level_name}.lvl")
        # check if file is a valid map file
        for line in enumerate(data_lines):
            if "<PyGameEngine-Level>\n" in line:
                level_file = True
                break

            else:
                return "ERROR - LEVEL FILE INVALID"
        # file ok
        if level_file:
            tilemap_data = []
            data_lines.pop(0)
            # each line in file
            for line in data_lines:
                w_line_list = line.split("<")
                w_line_list.remove("")
                for tile in w_line_list:
                    # remove new line
                    try:
                        split_1 = tile.split("\n")
                        split_1.remove("")
                        split = split_1[0]
                    except ValueError:
                        split = tile
                    tilemap_data.append(split)
            # print(tilemap_data)
            for tile in tilemap_data:
                source = tile.split(" ")
                values = []
                # print(source)
                for data in source:
                    value = data.split("=")
                    values.append(value[1])
                # print(values)  # Grid Pos // tile
                # grid position
                grid_position = position_grid(values[0].split(":"))

                tile_style = values[1]
                try:
                    tile_type = values[2]
                except IndexError:
                    tile_type = "no_type"

                #print("grid_position:" + str(grid_position) + "tile_style:" + tile_style + "type:" + tile_type)
                self.tile_maps.append(Tile(self.screen, grid_position, tile_style, tile_type))
            print(self.tile_maps)
