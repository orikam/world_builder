import pygame
import json

class Game_map():
    GAME_TYPE_WALL = 1
    def __init__(self, pygame, surface, window_size, tile_size, pos, database) -> None:
        self.pygame = pygame
        self.window_size = window_size
        self.tile_size = tile_size
        self.surface = surface
        self.pos = pos
        self.nb_tiles_width = database.nb_tiles_width
        self.nb_tiles_hight = database.nb_tiles_hight
        self.walls = []


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
                self.walls.append((index, cell, img, rect))
        for cell in self.walls:
            self.surface.blit(cell[2], cell[3])    

    def check_collision(self, rects) -> type:
        res = []
        
        for data in self.walls:
            for index, rect in enumerate(rects):
                if data[3].colliderect(rect):
                    dir = [None] * 4
                    if rect.left > data[3].left:
                        dir[0] = True # left
                    if rect.top > data[3].top:
                        dir[1] = True # top
                    if rect.left > data[3].left:
                        dir[2] = True # right
                    if rect.top < data[3].top:
                        dir[3] = True
                    print(f'{str(dir)} + {str(rect)} + {str(data[3])} ')
                    res.append((Game_map.GAME_TYPE_WALL, index, dir, None))
        if len(res):
            return res
        return None

    