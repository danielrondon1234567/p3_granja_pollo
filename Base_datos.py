from crud_animal import CrudAnimal
from produccion import Produccion

class BaseDatos(CrudAnimal):
    def __init__(self):
        self.animales = {}
        self.producciones = {}

    def crear_animal(self, animal):
        if animal.codigo in self.animales:
            print(f"Ya existe un animal con el código {animal.codigo}")
            return
        self.animales[animal.codigo] = animal
        self.producciones[animal.codigo] = Produccion(animal.codigo)

    def leer_animal(self, codigo):
        return self.animales.get(codigo)

    def actualizar_animal(self, codigo, nuevo_animal):
        if codigo in self.animales:
            self.animales[codigo] = nuevo_animal
        else:
            print(f"No se encontró el animal con código {codigo}")

    def eliminar_animal(self, codigo):
        if codigo in self.animales:
            del self.animales[codigo]
            if codigo in self.producciones:
                del self.producciones[codigo]
        else:
            print(f"No se encontró el animal con código {codigo}")

    def registrar_produccion(self, codigo, semana, cantidad):
        if codigo in self.producciones:
            self.producciones[codigo].registrar_produccion(semana, cantidad)
        else:
            print(f"No hay producción registrada para el código {codigo}")

    def mostrar_produccion(self, codigo):
        if codigo in self.producciones:
            print(self.producciones[codigo])
        else:
            print("No hay producción registrada para ese código")

    def reporte_general(self):
        print("Reporte general de producción:")
        for codigo, produccion in self.producciones.items():
            print(f"{codigo} - Total huevos: {produccion.produccion_total()}")

