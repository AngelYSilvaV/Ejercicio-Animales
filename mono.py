from abc import ABC, abstractmethod
from animal import Animal


   
class Trepar(ABC):
    @abstractmethod
    def trepar(self):
        pass
    

class mono(Animal, Trepar):
    def __init__(self, peso=0, velocidad=10):
        super().__init__("mono")
        self.peso = peso
        self.velocidad= velocidad
        
    def peso(self):
        return self.peso
     

    def comiendo(self):
        print("Mono: esta comiendo")

    def caminar(self):
        print(f"El mono: esta caminando")
        
    def trepar(self):
        print(f"EL mono esta trepando un arbol ")    

mi_mono= mono(7.5, 20)
print(mi_mono.get_peso())
print(mi_mono.velocidad)
mi_mono.comer_alimento()
mi_mono.caminar()
mi_mono.trepar()
print(mi_mono.get_nombre_animal())
mi_mono.peso = 37.5
print(mi_mono.get_peso())
mi_mono.set_peso(47.5)
print(mi_mono.get_peso())
mi_mono.set_altura(1.5)
mi_mono.set_edad(5)
print(mi_mono.get_altura())
print(mi_mono.get_edad())
mi_mono.set_nombre_animal("Mono Araña")
print(mi_mono.get_nombre_animal())


