import pygame
import json
from enemy import Enemy
from enemy_1 import Enemy_1
import lava

from lava import Lava

class Game_map():
    GAME_TYPE_WALL = 1
    GAME_TYPE_ENEMY = 2
    def __init__(self, pygame, surface, window_size, tile_size, pos, database) -> None:
        self.pygame = pygame
        self.window_size = window_size
        self.tile_size = tile_size
        self.surface = surface
        self.pos = pos
        self.nb_tiles_width = database.nb_tiles_width
        self.nb_tiles_hight = database.nb_tiles_hight
        self.walls = []
        self.enemies = pygame.sprite.Group()
        self.lava = Lava()
        self.enemy_1 = Enemy_1()


    def update(self, dt):
        self.enemies.update(dt)

    def draw(self, surface: pygame.Surface):
        surface.fill((0, 0, 0))
        surface.blit(self.surface, (0, 0))
        self.enemies.draw(surface)
    
    def set(self, database, map_name):
        map = []
        with open(map_name, 'r') as openfile:
            # Reading from json file
            json_object = json.load(openfile)
            map = json_object['map']
        for index, item in enumerate(map):
            if item == '1':
                cell = database.cells[str(item)]
                img = cell.image
                rect = img.get_rect()
                rect.x = (index % self.nb_tiles_width) * self.tile_size
                rect.y = (index // self.nb_tiles_width) * self.tile_size
                self.walls.append((index, cell, img, rect, None))
            if item == '2':
                cell = database.cells[str(item)]
                img = cell.image
                rect = img.get_rect()
                rect.x = (index % self.nb_tiles_width) * self.tile_size
                rect.y = (index // self.nb_tiles_width) * self.tile_size
                self.walls.append((index, cell, img, rect, self.lava))
            if item == '3':
                cell = database.cells[str(item)]
                img = cell.image
                rect = img.get_rect()
                rect.x = (index % self.nb_tiles_width) * self.tile_size
                rect.y = (index // self.nb_tiles_width) * self.tile_size
                #self.walls.append((index, cell, img, rect, self.lava))
                enemy = Enemy(rect.x, rect.y, img, self.enemy_1, self.check_collision)
                self.enemies.add(enemy)
        for cell in self.walls:
            self.surface.blit(cell[2], cell[3])    

    def check_collision(self, rects, targets) -> type:
        res = []
        for target in targets:
            if target == 'wall':
                for data in self.walls:
                    for index, rect in enumerate(rects):
                        if data[3].colliderect(rect):
                            dir = [None] * 4
                            if rect.left >= data[3].left:
                                dir[0] = True # left
                            if rect.top >= data[3].top:
                                dir[1] = True # top
                            if rect.left <= data[3].left:
                                dir[2] = True # right
                            if rect.top <= data[3].top:
                                dir[3] = True
                            #print(f'{str(rect)} + {str(data[3])}')
                            res.append((Game_map.GAME_TYPE_WALL, index, dir, data[3], data[4]))
            if target == 'enemy':
                for enemy in self.enemies:
                    for index, rect in enumerate(rects):
                        if enemy.rect.colliderect(rect):
                            dir = [None] * 4
                            if rect.left >= enemy.rect.left:
                                dir[0] = True # left
                            if rect.top >= enemy.rect.top:
                                dir[1] = True # top
                            if rect.left <= enemy.rect.left:
                                dir[2] = True # right
                            if rect.top <= enemy.rect.top:
                                dir[3] = True
                            #print(f'{str(rect)} + {str(data[3])}')
                            res.append((Game_map.GAME_TYPE_ENEMY, index, dir, enemy.rect, enemy))
        if len(res):
            return res
        return None

    