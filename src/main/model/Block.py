class Block:
    x: int
    y: int
    vx: int
    vy: int
    height: int
    width: int

    def __init__(self, x, y, vx, vy, width, height, colour):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.width = width
        self.height = height
        self.colour = colour

    def set_vx(self, vx: int):
        self.vx = vx

    def set_vy(self, vy: int):
        self.vy = vy

    def update(self):
        """updates block position by adding vx to x and vy to y"""
        self.x += self.vx
        self.y += self.vy
