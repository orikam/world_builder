import pygame
import json

class Game_map():
    def __init__(self, pygame, surface, window_size, tile_size, pos, database) -> None:
        self.pygame = pygame
        self.window_size = window_size
        self.tile_size = tile_size
        self.surface = surface
        self.pos = pos
        self.nb_tiles_width = database.nb_tiles_width
        self.nb_tiles_hight = database.nb_tiles_hight
        self.data = []


    def draw(self, surface: pygame.Surface):
        surface.blit(self.surface, (0, 0))
    
    def set(self, database, map_name):
        map = []
        with open(map_name, 'r') as openfile:
            # Reading from json file
            json_object = json.load(openfile)
            map = json_object['map']
        for index, item in enumerate(map):
            if item != 0:
                cell = database.cells[str(item)]
                img = cell.image
                rect = img.get_rect()
                rect.x = (index % self.nb_tiles_width) * self.tile_size
                rect.y = (index // self.nb_tiles_width) * self.tile_size
                self.data.append((index, cell, img, rect))
        for cell in self.data:
            self.surface.blit(cell[2], cell[3])    

    