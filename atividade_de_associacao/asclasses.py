class Motor:
    def __init__(self,potencia,marca):
        self.potencia = potencia
        self.marca = marca

    def getPotencia(self):
        return self.potencia
    def setPotencia(self,potencia):
        self.potencia = potencia

    def getMarca(self):
        return self.marca
    def setMarca(self,marca):
        self.marca = marca


class Roda:
    def __init__(self,tamanho,marca):
        self.tamanho = tamanho
        self.marca = marca

    def getTamanho(self):
        return self.tamanho
    def setTamanho(self,tamanho):
        self.tamanho = tamanho

    def getMarca(self):
        return self.marca
    def setMarca(self,marca):
        self.marca = marca


class Carro:
    def __init__(self):
        self.motor = None
        self.roda = None

    def getMotor(self):
        return self.motor
    def setMotor(self,motor):
        self.motor = motor

    def getRoda(self):
        return self.roda
    def setRoda(self,roda):
        self.roda = roda