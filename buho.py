from abc import ABC, abstractmethod
from animal import Animal

class Comer(ABC):
    @abstractmethod
    def comer_alimento(self):
        pass
    
class Volar(ABC):
    @abstractmethod
    def volar(self):
        pass

class Hibernar(ABC):
    @abstractmethod
    def mimir(self):
        pass
    
class Buho(Animal, Comer, Volar, Hibernar):
    def __init__(self, color = "Blanco", hibernando = False, vel_vuelo = 0):
        super().__init__("Buho")
        self.color = color
        self.hibernando = hibernando
        self.vel_vuelo = vel_vuelo
        
    def get_color(self):
        return self.color
    
    def get_hibernando(self):
        return self.hibernando
    
    def get_vel_vuelo(self):
        return self.vel_vuelo
    
    def set_color(self,color):
        self.color=color
        
    def set_hibernando(self,hibernando):
        self.hibernando=hibernando
        
    def set_vel_vuelo(self,vel_vuelo):
        self.vel_vuelo=vel_vuelo
        
    def comer_alimento(self):
        print("Buho: Estoy comiendo un raton")
        
    def volar(self):
        print(f"Buho: Estoy volando a una velocidad de {self.vel_vuelo} km/hr")
        
    def mimir(self):
        if self.hibernando == True:
            print(f"Buho: Estoy hibernando")