import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, img, type, collision):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.type = type
        self.collision = collision
        self.life = self.type.base_life
    
    def update(self, *args, **kwargs) -> None:
        dx = (self.type.get_dx() * args[0]) / 100
        dy = (self.type.get_dy() * args[0]) / 100
        rects = []
        rects.append(pygame.rect.Rect(self.rect.x + dx, self.rect.y, self.rect.width, self.rect.height))
        rects.append(pygame.rect.Rect(self.rect.x, self.rect.y + dy, self.rect.width, self.rect.height))
        collision_list = self.type.get_collision_list()
        objects = self.collision(rects, collision_list)
        if objects:
            for obj in objects:
                dir = 0
                if obj[0] == 1: # wall
                    if obj[1] == 0:
                        dx = 0
                    else:
                        dir = 1
                        dy = 0
                res = self.type.collide(dir, obj[4])
                if res == 1:
                    self.kill()
        self.rect.move_ip(dx, dy)
    
    def get_damage(self, dir):
        return self.type.get_damage(dir)
    
    def set_damage(self, dir, type, value):
        res = self.type.set_damage(dir, type, value)
        self.life = self.life - res
        if self.life <= 0:
            self.kill()