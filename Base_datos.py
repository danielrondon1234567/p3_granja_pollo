class base_datos(CrudAnimal):
  def_init_(self):
  self.lista_datos=[]
  self.producciones=[]

def crear_animal(self, animal):
  self.aniamles[animal.codigo]=animal
  self.producciones[animal.codigo]=Produccion(animal.codigo)

def leer_aniaml(self, codigo):
  return self.animales.get(codigo)

def actualizar_animal(self, codigo, nuevo_animal):
  if codigo in self.animales:
      self.animales[codigo]=nuevo_animal

def eliminar_animal(self,codigo):
  if codigo in self.animales:
    del self.animales[codigo]
    del self.produciones[codigo]

def regitrar_produccion(self,codigo,semana,cantidad)
if codigo in self.producciones:
  self.producciones[codigo].registrar_producion(semana, cantidad)

def mostrar_producion(self,codigo):
  if codigo in self.produciones:
    print(self.producines[codigo])
  else:
    print("no hay produccion registrada para ese codigo")

def reporte_general(self):
  for codigo, produccion in self.producciones.items():
    print(f"{codigo}-total huevos: {produccion.produccion_total()}")
