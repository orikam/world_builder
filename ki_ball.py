class Ki_ball:
    def __init__(self) -> None:
        self.dx = 20
        self.dy = 0
        self.damage = 100
        self.base_life = 0
    
    def get_damage(self) -> int:
        return self.damage
    
    def get_dx(self):
        return self.dx
    
    def get_dy(self):
        return self.dy

    def collide(self, dir, target = None):
        if target:
            target.set_damage(dir, 1, 100)
        return 1
    
    def get_damage(self, dir):
        return self.damage
    
    def set_damage(self, dir, type, value):
        return 100

    def get_collision_list(self):
        return ['wall', 'enemy']
