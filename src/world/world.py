from src.engine.settings import *
from src.engine.loader import *
from src.entities.player import Player

class World:
    def __init__(self):
        self.win = pg.display.get_surface()

        self.player_type = "Ninja Frog"
        self.load_assets()
        self.visible_sprites = pg.sprite.Group()

        self.entity = Player((100,100),self.assets["player"],self.visible_sprites)

    def load_assets(self):
        self.assets = {
            "player":{
                "idle": load_tilemap(os.path.join(IMAGE_PATH,"Main Characters",self.player_type,"Idle (32x32).png")),
                "run": load_tilemap(os.path.join(IMAGE_PATH, "Main Characters", self.player_type, "Run (32x32).png"))
            }
        }

    def render(self):
        self.visible_sprites.draw(self.win)

    def update(self, dt):
        self.visible_sprites.update(dt)