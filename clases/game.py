#escribe aquí un código para la ventana principal del juego

from direct.showbase.ShowBase import ShowBase
from mapmanager import MapManager
from hero import Hero
class Game(ShowBase):
    def __init__(self):    
        super().__init__(self)
        self.land = MapManager()
        self.hero = Hero((10,20,2), self.land)
        base.camLens.setFov(90)

juego = Game()
juego.run()