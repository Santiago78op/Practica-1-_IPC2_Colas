
class Cola_Cliente():

    def __init__(self):
        self.cola = []


    def append(self,Cliente):
        self.cola.append(Cliente)

    def recorrer(self):
        for elemento in self.cola:
            print("Nombre: ", elemento.name,"Nit: ",elemento.nit,"Tiempo Inicio Orden: ",elemento.time, "Numero de Orden: ", elemento.numOfOrder)

    def buscar(self,orden):
        for elemento in self.cola:
            if elemento.numOfOrder == orden:
                return elemento

    def desencolar(self):
        if self.cola:
            self.cola.pop(0)

    def devolver_tamano(self):
        return len(self.cola)

    def devolver_lista(self):
        return self.cola

