from src.engine.settings import *

def load_tilemap(path,tilesize=(32,32),scale=(TILE_SIZE,TILE_SIZE)):
    base_image = pg.image.load(path)
    images = []

    for col in range(0,base_image.width // tilesize[0]):
        for row in range(0,base_image.height // tilesize[1]):
            img = base_image.subsurface(col*tilesize[0],row*tilesize[1],tilesize[0],tilesize[1])
            img = pg.transform.scale(img,scale)
            images.append(img)

    return images
