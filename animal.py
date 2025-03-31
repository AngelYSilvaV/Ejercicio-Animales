from abc import ABC, abstractmethod

class Comer(ABC):
    @abstractmethod
    def comer_alimento(self):
        pass

class Animal(Comer):
    def __init__(self, nombre_animal="Animal Desconocido", peso=0, altura=0, edad=0):
        self.nombre_animal = nombre_animal
        self.peso = peso
        self.altura = altura
        self.edad = edad
    
    def get_nombre_animal(self):
        return self.nombre_animal

    def set_nombre_animal(self, nombre_animal):
        self.nombre_animal = nombre_animal
    
    def get_peso(self):
        return self.peso

    def set_peso(self, peso):
        self.peso = peso
    
    def get_altura(self):
        return self.altura

    def set_altura(self, altura):
        self.altura = altura
    
    def get_edad(self):
        return self.edad

    def set_edad(self, edad):
        self.edad = edad
    
    def comer_alimento(self):
        print(f"El animal: {self.nombre_animal} está comiendo.")
