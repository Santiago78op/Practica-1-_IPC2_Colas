from Lista.ColaIngredientes import Cola_Ingredeintes

class Pizza():

    def __init__(self,numOfPizza=None,type=None):
        self.numOfPizza = numOfPizza
        self.type = type
        self.listaType = Cola_Ingredeintes()

