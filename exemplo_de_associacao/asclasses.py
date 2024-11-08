class Programador:
    def __init__(self,nome):
        self.nome = nome
        self.equip = None

    def getNome(self):
        return self.nome
    def setNome(self,x):
        self.nome = x
    
    def getEquip(self):
        return self.equip
    def setEquip(self,x):
        self.equip = x


class Equipamento:
    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo

    def getMarca(self):
        return self.marca
    def setMarca(self,x):
        self.marca = x

    def getModelo(self):
        return self.modelo
    def setModelo(self,x):
        self.modelo = x