import imp
import pygame
import os
import json

import grid 
import map
from cell import Cell
from database import Database     

database = Database('database.json') 


window_size = (800, 600)
side_bar_size = (100, 600)
builder_size = (window_size[0] + side_bar_size[0], window_size[1])

tile_size = 50



pygame.init()
print (pygame.display.Info())
window = pygame.display.set_mode(builder_size)




class Side_bar(grid.Grid):
    def __init__(self, pygame, window_size, tile_size, pos, data) -> None:
        super().__init__(pygame, window_size, tile_size, pos)
        ind = 0
        for item in data.cells.items():
            self.cells[ind] = item[1]
            ind += 1
    
    
    def set_cell(self, index, data):
        self.cells[index] = data
    
    def draw(self, surface: pygame.Surface):
        super().draw(surface)
        pygame.draw.rect(surface, (255, 0, 0), (self.pos[0], self.pos[1], self.window_size[0], self.window_size[1]), 2)
        for ind, cell in enumerate(self.cells):
            if cell:
                x = (ind % self.cols) * self.tile_size
                y = (ind // self.cols) * self.tile_size
                surface.blit(cell.get_image(), (self.pos[0] + x, self.pos[1] +y))  


run = True
map = map.Map(pygame, window_size, tile_size, (0,0))
map.build_grid()
side_bar= Side_bar(pygame, side_bar_size, tile_size, (window_size[0], 0), database)
side_bar.build_grid()

cell = None
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            print (map.get_cell((x,y)))
            cell_ind = map.get_cell((x,y))
            if cell_ind != None:
                 map.set_cell(cell_ind, cell)
            cell_ind = side_bar.get_cell((x,y))
            if cell_ind != None:
                 cell = side_bar.cells[cell_ind]
        if event.type == pygame.KEYDOWN:
           if event.unicode == 's':
                l = map.export()
                dic = {}
                dic['map'] = l
                with open("map.json", "w") as outfile:
                    json.dump(dic, outfile)

    #if pygame.mouse.get_pressed()[0] == True:
    #    print (str(pygame.mouse.get_pos()))
    #sprite1.rect.center = pygame.mouse.get_pos()
    #collide = pygame.sprite.spritecollide(sprite1, test_group, False)

    map.draw(window)
    side_bar.draw(window)

    pygame.display.update()

pygame.quit()
exit()