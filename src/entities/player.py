from src.engine.settings import *
from src.entities.entity import Entity

class Player(Entity):
    def __init__(self,pos,frames,group):
        super().__init__(pos,frames,group)

    def input(self):
        key = pg.key.get_pressed()

        if key[pg.K_d]:
            self.direction.x = 1
            self.flipped = False
        elif key[pg.K_a]:
            self.direction.x = -1
            self.flipped = True
        else:
            self.direction.x = 0


    def update(self,dt):
        self.input()
        self.move(dt)

        self.get_status()
        self.animation(dt)
