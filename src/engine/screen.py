from src.engine.settings import *

from src.world.world import World

class Screen:
    def __init__(self):
        self.win = pg.display.get_surface()

        self.world = World()

    def render(self):
        self.world.render()

    def update(self,dt):
        self.world.update(dt)