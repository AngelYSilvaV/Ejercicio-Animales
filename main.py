from abc import ABC, abstractmethod
from tigre import Tigre
from delfin import Delfin
from pinguino import Pinguino
from buho import Buho
from araña import Araña
from mono import Mono

#Este menú nos ayuda a que el usuario seleccione un animal
def menu_seleccion_animal():
    print("Seleccione un animal:")
    print("1. Tigre")
    print("2. Delfín")
    print("3. Pingüino")
    print("4. Búho")
    print("5. Araña")
    print("6. Mono")
    return int(input("Ingrese su opción: "))

#Este menú nos va a ayudar a que el usuario seleccione alguna acción a realizar
def menu_detalles_animal(animal):
    print("Opciones:")
    print("1. Ingresar detalles")
    print("2. Mostrar detalles")
    print("3. Acción específica")
    print("4. Comer")
    return int(input("Ingrese su opción: "))

#Esta es la parte principal del código
def main():
    #Esta variable booleana nos servirá para controlar el bucle del menú de elección de animales
    continuar_bucle_externo = True

    #Definimos los objetos de los animales con su configuración por defecto
    objeto_tigre = Tigre()
    objeto_delfin = Delfin()
    objeto_pinguino = Pinguino()
    objeto_buho = Buho()
    objeto_araña = Araña()
    objeto_mono = Mono()

    #Este es un bucle para el menú de elección de animales
    while continuar_bucle_externo:
        opcion = menu_seleccion_animal()
        match opcion:
            case 1:
                animal = objeto_tigre
            case 2:
                animal = objeto_delfin
            case 3:
                animal = objeto_pinguino
            case 4:
                animal = objeto_buho
            case 5:
                animal = objeto_araña
            case 6:
                animal = objeto_mono
            case _:
                print("Opción inválida.")
                continue

        #Variable booleana para controlar el bucle de elección de acción
        continuar_bucle_interno = True
        #Bucle para el menú de elección de acción
        while continuar_bucle_interno:
            print(f"El animal seleccionado es: {animal.get_nombre()}")
            opcion_menu = menu_detalles_animal(animal)
            if opcion_menu == 1:
                animal.set_edad(int(input("Ingrese la edad: ")))
                animal.set_altura(int(input("Ingrese la altura: ")))
                animal.set_peso(int(input("Ingrese el peso: ")))
                if isinstance(animal, Tigre):
                    animal.set_numero_de_rayas(int(input("Ingrese el número de rayas: ")))
                    animal.set_nivel_de_sonido(int(input("Ingrese el nivel de sonido del rugido: ")))
                    animal.set_velocidad(int(input("Ingrese la velocidad: ")))
                elif isinstance(animal, Delfin):
                    animal.set_velocidad_nado(int(input("Ingrese la velocidad de nado: ")))
                    animal.set_color(input("Ingrese el color del delfín: "))
                elif isinstance(animal, Pinguino):
                    nadando = input("¿El pingüino está nadando? (s/n): ").lower() == "s"
                    animal.set_esta_nadando(nadando)
                    if nadando:
                        animal.set_velocidad_nado(int(input("Ingrese la velocidad de nado: ")))
                    else:
                        animal.set_velocidad_caminata(int(input("Ingrese la velocidad de caminata: ")))
            elif opcion_menu == 2:
                print(f"Edad: {animal.get_edad()}")
                print(f"Altura: {animal.get_altura()}")
                print(f"Peso: {animal.get_peso()}")
                if isinstance(animal, Tigre):
                    print(f"Número de rayas: {animal.get_numero_de_rayas()}")
                    print(f"Nivel de sonido del rugido: {animal.get_nivel_de_sonido()}")
                elif isinstance(animal, Delfin):
                    print(f"Color del delfín: {animal.get_color()}")
                elif isinstance(animal, Pinguino):
                    print(f"Está nadando: {'Sí' if animal.get_esta_nadando() else 'No'}")
            elif opcion_menu == 3:
                if isinstance(animal, Delfin):
                    animal.nadar()
                elif isinstance(animal, Pinguino):
                    if animal.get_esta_nadando():
                        animal.nadar()
                    else:
                        animal.caminar()
                elif isinstance(animal, Tigre):
                    animal.caminar()
            elif opcion_menu == 4:
                animal.comer_alimento()
            else:
                print("Opción inválida")
            
            continuar_bucle_interno = input("¿Continuar con este animal? (s/n): ").lower() == "s"
        
        continuar_bucle_externo = input("¿Continuar con el menú principal del zoológico? (s/n): ").lower() == "s"

if __name__ == "__main__":
    main()
