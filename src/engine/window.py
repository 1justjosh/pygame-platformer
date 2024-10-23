import sys

from src.engine.settings import *

class Window:
    def __init__(self):
        self.win = pg.display.set_mode(RES)
        pg.display.set_caption(TITLE)

    def event_handler(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

    def render(self):
        pg.display.flip()

    def update(self):
        pass

    def run(self):
        while True:
            self.event_handler()
            self.update()
            self.render()