from src.engine.settings import *
from src.engine.loader import *

class World:
    def __init__(self):
        self.win = pg.display.get_surface()

        self.img = load_tilemap("assets/images/Main Characters/Ninja Frog/Idle (32x32).png")

    def render(self):
        self.win.blit(self.img[0],(0,0))

    def update(self, dt):
        pass