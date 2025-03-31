from abc import ABC, abstractmethod
from animal import Animal, Nadar, Comer

class Delfin(Animal, Nadar, Comer):
    def __init__(self, color="Gris", velocidad_nado=10):
        super().__init__("Delfín")
        self.color = color
        self.velocidad_nado = velocidad_nado

    def get_color(self):
        return self.color

    def get_velocidad_nado(self):
        return self.velocidad_nado

    def set_color(self, color):
        self.color = color

    def set_velocidad_nado(self, velocidad_nado):
        self.velocidad_nado = velocidad_nado

    def comer_alimento(self):
        print("Delfín: Estoy comiendo un delicioso pescado")

    def nadar(self):
        print(f"Delfín: Estoy nadando a una velocidad de {self.velocidad_nado} nudos por hora")