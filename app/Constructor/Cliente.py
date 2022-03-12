from Lista.ColaPizza import Cola_Pizza

class Cliente():

    def __init__(self,name=None,nit=None,time=None,numOfOrder=None):
        self.name = name #Santiago
        self.nit = nit #196879-9
        self.time = time #11:00
        self.numOfOrder = numOfOrder #1
        self.listPizza = Cola_Pizza()


