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
    
class Trepar(ABC):
    @abstractmethod
    def trepar(self):
        pass
    

class mono(Animal, Caminar, Comer,Trepar):
    def __init__(self, peso=0, velocidad=10):
        super().__init__("mono")
        self.numero_de_rayas = peso
        self.velocidad = velocidad
        
    def peso(self):
        return self.peso
     

    def comiendo(self):
        print("Mono: esta comiendo")

    def caminar(self):
        print(f"El mono: esta caminando")
        
    def trepar(self):
        print(f"EL mono esta trepando un arbol ")    
        
