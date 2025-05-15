class Produccion:
    def _init_(self, codigo_animal, semanas=10):
        self.codigo_animal = codigo_animal
        self.huevos_por_semana = [0] * semanas

    def registrar_produccion(self, semana, cantidad):
        if 0 <= semana < len(self.huevos_por_semana):
            self.huevos_por_semana[semana] = cantidad
        else:
            print("Semana fuera de rango")

    def produccion_total(self):
        return sum(self.huevos_por_semana)

    def produccion_semana(self, semana):
        if 0 <= semana < len(self.huevos_por_semana):
            return self.huevos_por_semana[semana]
        else:
            return None

    def _str_(self):
        return f"Producción {self.codigo_animal}: {self.huevos_por_semana}"
