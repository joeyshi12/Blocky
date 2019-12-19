class Block:
    x: float
    y: float
    vx: float
    vy: float
    height: int
    width: int
    colour: tuple

    def __init__(self, pos: tuple, width: int, height: int, colour: tuple):
        self.x, self.y = pos
        self.vx, self.vy = (0, 0)
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
