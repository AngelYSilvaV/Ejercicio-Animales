from abc import ABC, abstractmethod

#Estamos generando clases base para las acciones que pueden realizar los animales
# y las cuales serán heredadas por las clases hijas que representan a los animales específicos.

class Comer(ABC):
    @abstractmethod
    def comer_alimento(self):
        pass

class Caminar(ABC):
    @abstractmethod
    def caminar(self):
        pass

class Nadar(ABC):
    @abstractmethod
    def nadar(self):
        pass

class Tejer(ABC):
    @abstractmethod
    def tejer(self):
        pass

class Picar(ABC):
    @abstractmethod
    def picar(self):
        pass

class Hibernar(ABC):
    @abstractmethod
    def mimir(self):
        pass

class Trepar(ABC):
    @abstractmethod
    def trepar(self):
        pass

class Volar(ABC):
    @abstractmethod
    def volar(self):
        pass

#Clase base para los animales, que contiene atributos y métodos comunes a todos los animales.
# Esta clase hereda de la clase Comer, lo que significa que todos los animales son capaces de comer.
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
