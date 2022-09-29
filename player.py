
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
        self.image = pygame.transform.scale(self.image, (290 // 6, 505 // 6))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.jump = False

    def update(self, dt):
        rects = []
        dx = 0
        self.dy += (15 * dt) / 100 
        if self.dy >= (80 * dt) / 100:
            self.dy = (80 * dt) / 100
        self.dy
        keys = self.pygame.key.get_pressed()
        if keys[self.pygame.K_LEFT]:
            dx = -(20  * dt) / 100
        if keys[self.pygame.K_RIGHT]:
            dx = (20 * dt) / 100
        if keys[self.pygame.K_SPACE]:
            if self.jump == False:
                self.dy = -30 
                self.jump = True

        rects.append(pygame.rect.Rect(self.rect.x + dx, self.rect.y, self.rect.width, self.rect.height))
        rects.append(pygame.rect.Rect(self.rect.x, self.rect.y + self.dy, self.rect.width, self.rect.height))
        res = self.map.check_collision(rects)
        if res:
            for r in res:
                if r[0] == 1: # wall
                    if r[1] == 0:
                        dx = 0
                    else:
                        self.dy = 0
                        if r[2][3]:
                            self.jump = False
                            print('-----')
     
        self.rect.move_ip(dx, self.dy)


    def draw(self, surface):
        surface.blit(self.image, self.rect)

        