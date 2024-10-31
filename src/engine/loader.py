from src.engine.settings import *

def load_tilemap(path,tilesize=(32,32)):
    base_image = pg.image.load(path)
    images = []

    for col in range(0,base_image.width // tilesize[0]):
        for row in range(0,base_image.height // tilesize[1]):
            images.append(base_image.subsurface(col*tilesize[0],row*tilesize[1],tilesize[0],tilesize[1]))

    return images
