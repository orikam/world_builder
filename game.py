import pygame
from  game_map import Game_map
from cell import Cell
from database import Database
from player import Player    


window_size = (800, 600)
builder_size = (window_size[0], window_size[1])

tile_size = 50

pygame.init()
print (pygame.display.Info())
window = pygame.display.set_mode(builder_size)
database = Database('database.json') 

map = Game_map(pygame, window_size, tile_size, (0,0), database)
map.set(database, 'map.json')

player = Player(pygame, database, map, 100, 100)
run = 1 # normal run
clock = pygame.time.Clock()

while run:
    dt = clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = 0
   
    #print(f'{str(dt)}')
    res = player.update(dt)
    if res == 1:
        run = 2 # death run
    offset = player.get_offset()
    if offset > 200:
        offset -= 200
    else:
        offset = 0
    map.update(dt)    
    map.draw(window, (offset, 0, window_size[0], window_size[1]))
    player.draw(window, (offset, 0, window_size[0], window_size[1]))
    pygame.display.update()

pygame.quit()
exit()