from src.engine.settings import *

class Entity(pg.sprite.Sprite):
    def __init__(self,pos,frames,group):
        super().__init__(group)

        self.frames = frames
        self.index = 0
        self.anim_speed = 12
        self.status = "run"

        self.image = pg.Surface((100,100))
        self.rect = self.image.get_rect(center=pos)

    def animation(self,dt):
        self.index += self.anim_speed * dt

        if self.index >= len(self.frames[self.status]):
            self.index = 0

        self.image = self.frames[self.status][int(self.index)]