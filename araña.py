#Animal Araña
from abc import ABC, abstractmethod

class Comer(ABC):
    @abstractmethod
    def comer(self):
        pass

class Tejer(ABC):
    @abstractmethod
    def tejer(self):
        pass

class Picar(ABC):
    @abstractmethod
    def picar(self):
        pass
    
class Caminar(ABC):
    @abstractmethod
    def caminar(self):
        pass

#clase Araña
class Araña(Comer, Tejer, Picar, Caminar):
    def __init__(self, EstaComiendo= False, VelocidadTejedura= 15, DolorPicadura=20, velocidad_caminata=15) :
        
        self.EstaComiendo= EstaComiendo
        self.VelocidadTejedura= VelocidadTejedura
        self.DolorPicadura= DolorPicadura
        self.velocidad_caminata= velocidad_caminata
        
    #Metdodo get y set
    def get_EstaComiendo(self):
        return self.EstaComiendo

    def set_EstaComiendo(self, EstaComiendo):
        self.EstaComiendo= EstaComiendo

    def get_VelocidadTejedura(self):
        return self.VelocidadTejedura

    def set_VelocidadTejedura(self, VelocidadTejedura):
        self.VelocidadTejedura= VelocidadTejedura

    def get_DolorPicadura(self):
        return self.DolorPicadura

    def set_DolorPicadura(self, DolorPicadura):
        self.DolorPicadura= DolorPicadura

    def get_velocidad_caminata(self):
        return self.velocidad_caminata

    def set_velocidad_caminata(self, velocidad_caminata):
        self.velocidad_caminata= velocidad_caminata
    #Implementacion de todos de la clase
    def comer(self):
        print("La araña está comiendo", self.EstaComiendo)

    def caminar(self):
        print("La araña camina a una velocidad de: ", self.velocidad_caminata, "km/h")

    def tejer(self):
        print("La araña teje a una velocidad de: ", self.VelocidadTejedura, "km/h")

    def picar(self):
        print("La araña pica a una velocidad de: ", self.DolorPicadura, "km/h")

