from abc import ABC, abstractmethod
from animal import Animal

class Comer(ABC):
    @abstractmethod
    def comer_alimento(self):
        pass

class Caminar(ABC):
    @abstractmethod
    def caminar(self):
        pass

class Tigre(Animal, Caminar, Comer):
    def __init__(self, numero_de_rayas=200, velocidad=10, nivel_de_sonido=10):
        super().__init__("Tigre")
        self.numero_de_rayas = numero_de_rayas
        self.velocidad = velocidad
        self.nivel_de_sonido = nivel_de_sonido

    def get_numero_de_rayas(self):
        return self.numero_de_rayas

    def get_velocidad(self):
        return self.velocidad

    def get_nivel_de_sonido(self):
        return self.nivel_de_sonido

    def set_numero_de_rayas(self, numero_de_rayas):
        self.numero_de_rayas = numero_de_rayas

    def set_velocidad(self, velocidad):
        self.velocidad = velocidad

    def set_nivel_de_sonido(self, nivel_de_sonido):
        self.nivel_de_sonido = nivel_de_sonido

    def comer_alimento(self):
        print("Tigre: He comido carne")

    def caminar(self):
        print(f"Tigre: Estoy caminando a una velocidad de {self.velocidad} k/h")