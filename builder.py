import pygame
import os
import json
 

class Cell():
    def __init__(self) -> None:
        pass

    def __init__(self, id, image) -> None:
        self.id = id
        self.image = image
    
    def get_id(self):
        return self.id
    
    def get_image(self):
        return self.image
        

class Database():
    def __init__(self, file_name) -> None:
        with open(file_name, 'r') as openfile:
            # Reading from json file
            json_object = json.load(openfile)
        if not json_object:
            return
        self.cells = []
        self.nb_tiles_width = json_object['nb_tiles_width']
        self.nb_tiles_hight = json_object['nb_tiles_hight']
        self.tile_size = json_object['tile_size']
        self.screen_width = json_object['screen_width']
        self.screen_height = json_object['screen_height']
        for cell in json_object['objects']:
            pass


 


window_size = (800, 600)
side_bar_size = (100, 600)
builder_size = (window_size[0] + side_bar_size[0], window_size[1])

tile_size = 50



pygame.init()
print (pygame.display.Info())
window = pygame.display.set_mode(builder_size)

grass = pygame.image.load('img/grass.png')
grass = pygame.transform.scale(grass, (tile_size, tile_size))






class Grid():
    def __init__(self, window_size, tile_size, pos) -> None:
        self.window_size = window_size
        self.tile_size = tile_size
        self.pos = pos
        self.surf = pygame.surface.Surface(window_size)
        self.cols = window_size[0] // tile_size
        self.cells = [None] * ((window_size[0] // tile_size) * self.cols)

    def build_grid(self):
        for y in range(0, self.window_size[1], self.tile_size):
            pygame.draw.line(self.surf, (255, 255, 255), (0, y), (self.window_size[0], y)) 
        for x in range(0, window_size[0], tile_size):
            pygame.draw.line(self.surf, (255, 255, 255), (x, 0), (x,self. window_size[1]))
    
    def draw(self, surface: pygame.Surface):
        surface.blit(self.surf, self.pos)

    def get_cell(self, loc):
        if (loc[0] >= self.pos[0]) and (loc[0] <= self.pos[0] + self.window_size[0]):
            if (loc[1] > self.pos[1]) and (loc[1] < self.pos[1] + self.window_size[1]):
                x = (loc[0] - self.pos[0]) // self.tile_size
                y = (loc[1] - self.pos[1]) // self.tile_size
                return (x + (y * self.cols))
        return None

class Map(Grid):
    def __init__(self, window_size, tile_size, pos) -> None:
        super().__init__(window_size, tile_size, pos)
    
    def set_cell(self, index, data):
        self.cells[index] = data
    
    def draw(self, surface: pygame.Surface):
        super().draw(surface)
        for ind, cell in enumerate(self.cells):
            if cell:
                x = (ind % self.cols) * self.tile_size
                y = (ind // self.cols) * self.tile_size
                surface.blit(cell.get_image(), (x, y))
    

class Side_bar(Grid):
    def __init__(self, window_size, tile_size, pos) -> None:
        super().__init__(window_size, tile_size, pos)
        for index, filename in enumerate(os.listdir('img')):
            img = pygame.image.load('img/grass.png')
            img = pygame.transform.scale(img, (tile_size, tile_size))
            self.cells[index] = Cell(index + 1, img)
    
    
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
map = Map(window_size, tile_size, (0,0))
map.build_grid()
side_bar= Side_bar(side_bar_size, tile_size, (window_size[0], 0))
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


    #if pygame.mouse.get_pressed()[0] == True:
    #    print (str(pygame.mouse.get_pos()))
    #sprite1.rect.center = pygame.mouse.get_pos()
    #collide = pygame.sprite.spritecollide(sprite1, test_group, False)

    map.draw(window)
    side_bar.draw(window)

    pygame.display.update()

pygame.quit()
exit()