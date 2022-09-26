import pygame

class Grid():
    def __init__(self, pygame, window_size, tile_size, pos) -> None:
        self.pygame = pygame
        self.window_size = window_size
        self.tile_size = tile_size
        self.pos = pos
        self.surf = pygame.surface.Surface(window_size)
        self.cols = window_size[0] // tile_size
        self.cells = [None] * ((window_size[0] // tile_size) * self.cols)

    def build_grid(self):
        for y in range(0, self.window_size[1], self.tile_size):
            self.pygame.draw.line(self.surf, (255, 255, 255), (0, y), (self.window_size[0], y)) 
        for x in range(0, self.window_size[0], self.tile_size):
            self.pygame.draw.line(self.surf, (255, 255, 255), (x, 0), (x,self. window_size[1]))
    
    def draw(self, surface: pygame.Surface):
        surface.blit(self.surf, self.pos)

    def get_cell(self, loc):
        if (loc[0] >= self.pos[0]) and (loc[0] <= self.pos[0] + self.window_size[0]):
            if (loc[1] > self.pos[1]) and (loc[1] < self.pos[1] + self.window_size[1]):
                x = (loc[0] - self.pos[0]) // self.tile_size
                y = (loc[1] - self.pos[1]) // self.tile_size
                return (x + (y * self.cols))
        return None
