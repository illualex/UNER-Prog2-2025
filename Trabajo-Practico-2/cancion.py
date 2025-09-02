# =========================================
# Ejercicio 1
# =========================================
class Cancion:
    def __init__(self, nombre: str, duracion: int, genero: str):
        self.nombre = nombre
        self.duracion = duracion 
        self.genero = genero

    def establecerNombre(self, nombre: str):
        self.nombre = nombre

    def establecerDuracion(self, duracion: int):
        self.duracion = duracion

    def establecerGenero(self, genero: str):
        self.genero = genero

    def obtenerNombre(self) -> str:
        return self.nombre

    def obtenerDuracion(self) -> int:
        return self.duracion

    def obtenerGenero(self) -> str:
        return self.genero