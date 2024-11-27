from src.engine.settings import *

class Tile(pg.sprite.Sprite):
    def __init__(self,pos,image,group,*args,**kwargs):
        super().__init__(group)

        self.image = pg.transform.scale(image,(32,32))
        self.rect = self.image.get_rect(topleft=pos)

