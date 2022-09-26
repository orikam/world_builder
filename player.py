
import pygame


class Player():
    def __init__(self, pygame, surface, database, map, x, y) -> None:
        self.pygame = pygame
        self.surface = surface
        self.map = map
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
        self.tile_size = database.tile_size
        self.window_size = (database.screen_width, database.screen_height)
        self.image =  pygame.image.load('img/player.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (290 // 4, 505 // 4))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.jump = False

    def update(self, dt):
        dx = 0
        self.dy += 1
        if self.dy >= 15:
            self.dy = 15
        keys = self.pygame.key.get_pressed()
        if keys[self.pygame.K_LEFT]:
            dx = -3 
        if keys[self.pygame.K_RIGHT]:
            dx = 3
        if keys[self.pygame.K_SPACE]:
            if self.jump == False:
                self.dy = -15
                self.jump = True

        for data in self.map.data:
            #check x direction
            res = data[3].colliderect((self.rect.x + dx, self.rect.y, self.rect.width, self.rect.height))
            if res:
                dx = 0
            #check y direction
            res = data[3].colliderect((self.rect.x, self.rect.y + self.dy, self.rect.width, self.rect.height))
            if res:
                self.dy = 0
                self.jump = False
           
        self.rect.move_ip(dx, self.dy)


    def draw(self, surface):
        surface.blit(self.image, self.rect)

        