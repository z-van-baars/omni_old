import pygame
import random
import colors

grass_image = pygame.Surface([2, 2])
grass_image.fill(colors.light_green)
forest_image = pygame.Surface([2, 2])
forest_image.fill(colors.dark_green)
terrain_images = {"Grass": grass_image,
                  "Forest": forest_image}


class GameMap(object):
    def __init__(self, x_tiles, y_tiles):
        self.tile_rows = []
        self.display_layer = pygame.Surface([x_tiles * 2, y_tiles * 2])
        self.display_layer.fill(colors.black)

        for y_value in range(y_tiles):
            this_row = []
            for x_value in range(x_tiles):
                new_tile = random.choice(terrain_types)(x_value, y_value)
                this_row.append(new_tile)
                self.display_layer.blit(terrain_images[this_row.terrain_type], [x_value * 2, y_value * 2])
            self.tile_rows.append(this_row)


class GameTile(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


class GrassTile(GameTile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.terrain_type = "Grass"


class ForestTile(GameTile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.terrain_type = "Forest"


terrain_types = [GrassTile, ForestTile]

