
class Cola_Ingredeintes():

    def __init__(self):
        self.cola = []


    def append(self,Pizza):
        self.cola.append(Pizza)

    def recorrer(self):
        for elemento in self.cola:
            print("Nombre: ", elemento.type, "Timepo: ", elemento.time)

    def retornar(self):
            return self.cola

    def desencolar(self):
        if self.cola:
            self.cola.pop(0)

    def buscarIng(self,nT):
        for elemento in self.cola:
            if elemento.result == nT:
                elemento.time = elemento.result
                return self.cola

    def switchElment(self,second,resultado):
        for elemento in self.cola:
            if elemento.end == second:
                elemento.time = resultado


    def devolver_tamano(self):
        return len(self.cola)