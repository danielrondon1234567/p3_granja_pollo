from crud_animal import CrudAnimal
from animal import Animal

class BaseDatosAnimal(CrudAnimal):
    def __init__(self):
       
        self._registro = {}

    def crear_animal(self, animal):
        if animal.codigo in self._registro:
            print(f"[!] Ya existe un animal con el código '{animal.codigo}'.")
        else:
            self._registro[animal.codigo] = animal
            print(f"[+] Animal registrado: {animal.codigo}")

    def leer_animal(self, codigo):
        animal = self._registro.get(codigo)
        if animal:
            return animal
        else:
            print(f"[!] No se encontró ningún animal con el código '{codigo}'.")
            return None

    def actualizar_animal(self, codigo, nuevo_animal):
        if codigo in self._registro:
            self._registro[codigo] = nuevo_animal
            print(f"[~] Animal actualizado: {codigo}")
        else:
            print(f"[!] No se puede actualizar. Código '{codigo}' no encontrado.")

    def eliminar_animal(self, codigo):
        if codigo in self._registro:
            del self._registro[codigo]
            print(f"[-] Animal eliminado: {codigo}")
        else:
            print(f"[!] No se puede eliminar. Código '{codigo}' no existe.")

    def listar_animales(self):
        if not self._registro:
            print("[i] No hay animales registrados.")
        else:
            print("[📋] Lista de animales:")
            for codigo, animal in self._registro.items():
                print(f" - {animal}")
