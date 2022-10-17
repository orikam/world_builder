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
    
    def update(self, *args, **kwargs) -> None:
        dx = (self.type.get_dx() * args[0]) / 100
        dy = (self.type.get_dy() * args[0]) / 100
        rects = []
        rects.append(pygame.rect.Rect(self.rect.x + dx, self.rect.y, self.rect.width, self.rect.height))
        rects.append(pygame.rect.Rect(self.rect.x, self.rect.y + dy, self.rect.width, self.rect.height))
        objects = self.collision(rects)
        if objects:
            for obj in objects:
                if obj[0] == 1: # wall
                    if obj[1] == 0:
                        dx = 0
                        self.type.collide(0)
                    else:
                        dy = 0
                        self.type.collide(1)
        self.rect.move_ip(dx, dy)