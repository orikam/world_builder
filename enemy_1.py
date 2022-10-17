class Enemy_1:
    def __init__(self) -> None:
        self.dx = 20
        self.dy = 20
        self.damage = 100
    
    def get_damage(self) -> int:
        return self.damage
    
    def get_dx(self):
        return self.dx
    
    def get_dy(self):
        return self.dy

    def collide(self, dir):
        if dir == 0:
            self.dx = -1 * self.dx
