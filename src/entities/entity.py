from src.engine.settings import *

class Entity(pg.sprite.Sprite):
    def __init__(self,pos,frames,group):
        super().__init__(group)

        self.frames = frames
        self.index = 0
        self.anim_speed = 12
        self.status = "idle"
        self.flipped = False

        self.direction = pg.math.Vector2()
        self.speed = 500

        self.image = pg.Surface((100,100))
        self.rect = self.image.get_rect(center=pos)
        self.hitbox = self.rect.copy()

    def animation(self,dt):
        self.index += self.anim_speed * dt

        if self.index >= len(self.frames[self.status]):
            self.index = 0

        self.image = pg.transform.flip(self.frames[self.status][int(self.index)],self.flipped,False)

    def get_status(self):
        if self.direction.magnitude() != 0:
            self.status = "run"
        else:
            self.status = "idle"

    def move(self,dt):
        self.hitbox.x += self.direction.x * self.speed * dt

        self.rect.center = self.hitbox.center