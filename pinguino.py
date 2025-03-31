from abc import ABC, abstractmethod
from animal import Animal

class Comer(ABC):
    @abstractmethod
    def comer_alimento(self):
        pass

class Nadar(ABC):
    @abstractmethod
    def nadar(self):
        pass

class Caminar(ABC):
    @abstractmethod
    def caminar(self):
        pass

class Pinguino(Animal, Nadar, Caminar):
    def __init__(self, esta_nadando=False, velocidad_caminata=2, velocidad_nado=10):
        super().__init__("Pingüino")
        self.esta_nadando = esta_nadando
        self.velocidad_caminata = velocidad_caminata
        self.velocidad_nado = velocidad_nado

    def set_esta_nadando(self, esta_nadando):
        self.esta_nadando = esta_nadando

    def set_velocidad_caminata(self, velocidad_caminata):
        self.velocidad_caminata = velocidad_caminata

    def set_velocidad_nado(self, velocidad_nado):
        self.velocidad_nado = velocidad_nado

    def get_esta_nadando(self):
        return self.esta_nadando

    def get_velocidad_caminata(self):
        return self.velocidad_caminata

    def get_velocidad_nado(self):
        return self.velocidad_nado

    def comer_alimento(self):
        print("Pingüino: Estoy comiendo pescado delicioso")

    def nadar(self):
        print(f"Pingüino: Estoy nadando a una velocidad de {self.velocidad_nado} millas náuticas por hora")

    def caminar(self):
        print(f"Pingüino: Estoy caminando a una velocidad de {self.velocidad_caminata} mph")

