class Block:
    x: int
    y: int
    vx: int
    vy: int
    height: int
    width: int

    def __init__(self, x, y, vx, vy, height, width, colour):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.height = height
        self.width = width
        self.colour = colour

    def set_vx(self, vx: int):
        self.vx = vx

    def set_vy(self, vy: int):
        self.vy = vy

    def update_block(self):
        """updates block position by adding vx to x and vy to y"""
        self.x += self.vx
        self.y += self.vy
