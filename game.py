from direct.showbase.ShowBase import ShowBase

from mapmanager import Mapmanager

class Game(ShowBase):
    def __init__(self):
        self.land = Mapmanager()
        self.land.LoadLand('land.txt')
        base.camLens.setfov(50)

game = Game()
game.run()