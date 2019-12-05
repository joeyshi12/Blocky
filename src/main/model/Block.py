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

    def add_x(self, amount):
        self.x = self.x + amount

    def add_y(self, amount):
        self.y = self.y + amount

    def set_vx(self, vx):
        self.vx = vx

    def set_vy(self, vy):
        self.vy = vy

    # EFFECTS: updates block
    def update_block(self):
        self.add_x(self.vx)
        self.add_y(self.vy)
