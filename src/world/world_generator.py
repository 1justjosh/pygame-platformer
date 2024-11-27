from src.engine.settings import *
from pytmx.util_pygame import load_pygame
from src.tiles.tile import Tile

class WorldGenerator:
    def __init__(self,visible_group):
        self.win = pg.display.get_surface()

        self.visible_group = visible_group

        self.current_map = "test-world"

        self.map = load_pygame(os.path.join("maps","worlds",self.current_map+".tmx"))

        self.load_all()

    def load_all(self):
        self.load_tile("","floor")

    def load_tile(self,name,layer):
        for x,y,img in self.map.get_layer_by_name(layer).tiles():
            x = int(x * 32)
            y = int(y * 32)

            Tile((x,y),img,self.visible_group)