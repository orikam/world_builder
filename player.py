
import pygame

from enemy import Enemy
from ki_ball import Ki_ball


class Player():
    def __init__(self, pygame, database, map, x, y) -> None:
        self.pygame = pygame
        self.surface = pygame.surface.Surface((2048, 600), flags = pygame.SRCALPHA)
        #self.surface.set_alpha(0)
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
        self.death = False
        self.ki_ball_image = pygame.image.load('img/ki_ball.png').convert_alpha()
        self.ki_ball_image = pygame.transform.scale(self.ki_ball_image, (25, 25))
        self.ki_ball = Ki_ball()

    def update(self, dt):
        if self.death:
            if self.rect.bottom > 0:
                self.dy = -(15 * dt) / 100
                self.rect.move_ip(0, self.dy)
                self.surface.fill((0,0,0,0))
                self.surface.blit(self.image, self.rect)
            return 2
        rects = []
        dx = 0
        self.dy += (15 * dt) / 100
        if self.dy >= (80 * dt) / 100:
            self.dy = (80 * dt) / 100
 
        keys = self.pygame.key.get_pressed()
        if keys[self.pygame.K_LEFT]:
            dx = -(20  * dt) / 100
        if keys[self.pygame.K_RIGHT]:
            dx = (20 * dt) / 100
        if keys[self.pygame.K_UP]:
            if self.jump == False:
                self.dy = -30 
                self.jump = True
        if keys[self.pygame.K_SPACE]:
            x = self.rect.x + self.rect.width
            y = self.rect.y + (self.rect.height / 2)
            shoot = Enemy(x, y, self.ki_ball_image, self.ki_ball, self.map.check_collision)
            self.map.add_shoot(shoot)
        rects.append(pygame.rect.Rect(self.rect.x + dx, self.rect.y, self.rect.width, self.rect.height))
        rects.append(pygame.rect.Rect(self.rect.x, self.rect.y + self.dy, self.rect.width, self.rect.height))
        #print(f'{dx}),{self.dy}')
        objects = self.map.check_collision(rects, ['wall', 'enemy'])
        if objects:
            for obj in objects:
                if obj[0] == 1: # wall
                    if obj[1] == 0:
                        dx = 0
                    else:
                        self.dy = 0
                        if obj[2][3]:
                            self.jump = False
                        else:
                            self.dy = (15 * dt) / 100
                target_obj = obj[4]
                if target_obj != None:
                    dir = 0
                    if obj[1] == 1:
                        dir = 1
                    
                    damage = target_obj.get_damage(dir)
                    if damage > 0:
                        self.death = True
                        self.image =  pygame.image.load('img/dragon_ball.png').convert_alpha()
                        self.image = pygame.transform.scale(self.image, (50, 50))
                    else:
                        target_obj.set_damage(dir, 0, 100)
                    return 1

     
        self.rect.move_ip(dx, self.dy)
        self.surface.fill((0,0,0,0))
        self.surface.blit(self.image, self.rect)
        return 0


    def draw(self, surface, offset):
        surface.blit(self.surface, (0, 0), offset)
        pass

    def get_offset(self):
        return self.rect.x

        