# =========================================
# Ejercicio 1 y 8
# =========================================


class Producto:
    def __init__(self, nombre: str):
        self.__nombre = nombre

    def obtenerNombre(self) -> str:
        return self.__nombre

    # --- Ejercicio 8 ---
    def __str__(self):
        return self.__nombre

    # --- Ejercicio 8 ---
    def __eq__(self, other):
        if isinstance(other, Producto):
            return self.__nombre == other.__nombre
        return False
