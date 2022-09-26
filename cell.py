import pygame

class Cell():
    def __init__(self) -> None:
        pass

    def __init__(self, id, type, size, image_name) -> None:
        self.id = id
        self.type = type
        self.image = pygame.image.load(image_name).convert_alpha()
        self.image = pygame.transform.scale(self.image, (size, size))

    
    def get_id(self):
        return self.id
    
    def get_image(self):
        return self.image
   