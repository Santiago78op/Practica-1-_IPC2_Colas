
class Cola_Pizza():

    def __init__(self):
        self.cola = []

    def append(self, numPiza):
        self.cola.append(numPiza)

    def recorrer(self):
        for elemento in self.cola:
            print("Numero de Pizza: ", elemento.numOfPizza,"Tipos de Pizza: ",elemento.Type)

    def buscarPizza(self,numPizza):
        for elemento in self.cola:
            if elemento == numPizza:
                return elemento

    def retornarPizza(self):
        return self.cola