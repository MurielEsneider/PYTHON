from animal import Animal

class Gato(Animal):
    def __init__(self, nombre, peso, maullar):
        super().__init__(nombre, peso)
        self.__maullar = maullar

    def Maullar(self):
        return f"el gato está maullando"