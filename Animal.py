class Animal:
    def _init_(self, codigo, raza, edad):
        self.codigo = codigo
        self.raza = raza
        self.edad = edad

    def _str_(self):
        return f"Animal[código={self.codigo}, raza={self.raza}, edad={self.edad}]"
