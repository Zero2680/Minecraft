# escribe aquí el código para crear y administrar el mapa
from clases.colores import Colors

class MapManager():
    def __init__(self):
        self.modelFile = './archivos/block.egg' #fichero con el modelo
        self.textureFile = './archivos/block.png' #fichero con la textura
        self.color = (0,1,1,1) #color
        self.colores = [Colors.ROJO.value, Colors.AMARILLO.value, Colors.VERDE.value, Colors.AZUL.value]
        self.startNew()
        self.loadLand()

    def startNew(self):
        '''Me crea el terreno sobre el que construir el mapa.
        Este terreno será un nodo de render
        '''
        self.land = render.attachNewNode('Land')

    def addBlock(self, posicion):
        '''
        Descripción: 
            Añadir un bloque al mapa en una posición en concreto
        ---
        Argumentos:
            posicion: la posición a la que será añadida el bloque
        '''
        self.block = loader.loadModel(self.modelFile)
        self.block.setTexture(loader.loadTexture(self.textureFile))
        altura = posicion[2]
        self.block.setColor(self.getColor(altura))
        self.block.setPos(posicion)
        self.block.reparentTo(self.land)

    def getColor(self, altura):
        '''recibe una altura y devuelve un color de la lista de colores'''
        if altura < len(self.colores):
            return self.colores[altura]
        else:
            return self.colores[-1]

    def loadLand(self):
        with open('./archivos/land.txt') as file:
            y = 0
            for linea in file:
                lista = linea.split(' ')
                lista = list(map(int, lista))
                x = 0
                for elemento in lista:
                    z = elemento + 1
                    for i in range(z):
                        self.getColor(x)
                        self.addBlock((x, y, i))
                    x += 1
                y +=1

    def clear(self):
        self.land.removeNode()  #eliminamos el mapa actual
        self.startNew()         #creamos un nuevo nodo