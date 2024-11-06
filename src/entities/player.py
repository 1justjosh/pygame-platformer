from src.engine.settings import *
from src.entities.entity import Entity

class Player(Entity):
    def __init__(self,pos,frames,group):
        super().__init__(pos,frames,group)


    def update(self,dt):
        self.animation(dt)