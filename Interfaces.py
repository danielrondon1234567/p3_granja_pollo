from abc import ABC, abstractmethod

class CrudAnimal(ABC):
@abstractmethod
def crear_aniaml(self, animal):pass

@abstractmethod
def leer_animal(self,codigo):pass

@abstractmethod
def actualisar_animal(self,codigo, nuevo_animal):pass

@abstractmethod
def eliminar_animal(self, codigo):pass
