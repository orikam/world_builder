import pygame
import json
import grid

class Map(grid.Grid):
    def __init__(self, pygame, window_size, tile_size, pos) -> None:
        super().__init__(pygame, window_size, tile_size, pos)
        self.rects = []
        self.indexs = []
    
    def set_cell(self, index, data):
        self.cells[index] = data
    
    def draw(self, surface: pygame.Surface):
        super().draw(surface)
        for ind, cell in enumerate(self.cells):
            if cell:
                x = (ind % self.cols) * self.tile_size
                y = (ind // self.cols) * self.tile_size
                surface.blit(cell.get_image(), (x, y))
    
    def set(self, database, map_name):
        map = []
        with open(map_name, 'r') as openfile:
            # Reading from json file
            json_object = json.load(openfile)
            map = json_object['map']
        for index, item in enumerate(map):
            if item != 0:
                self.cells[index] = database.cells[str(item)]

    def export(self):
        id_list = []
        for ind, cell in enumerate(self.cells):
            if cell:
                id_list.append(cell.get_id())
            else:
                id_list.append(0)
        return id_list
