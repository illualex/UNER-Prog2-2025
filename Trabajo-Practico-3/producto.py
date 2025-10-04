# =========================================
# Ejercicio 1
# =========================================

class Producto:
    def __init__(self, nombre: str):
        self.__nombre = nombre

    def obtenerNombre(self) -> str:
        return self.__nombre