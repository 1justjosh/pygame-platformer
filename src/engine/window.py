from src.engine.settings import *
from src.engine.screen import Screen

class Window:
    def __init__(self):
        self.win = pg.display.set_mode(RES)
        pg.display.set_caption(TITLE)

        self.screen = Screen()

        self.clock = pg.time.Clock()

    def event_handler(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

    def render(self):
        self.win.fill((20,40,80))

        self.screen.render()

        pg.display.flip()

    def update(self):
        dt = self.clock.tick(120) / 1000

        self.screen.update(dt)

    def run(self):
        while True:
            self.event_handler()
            self.update()
            self.render()