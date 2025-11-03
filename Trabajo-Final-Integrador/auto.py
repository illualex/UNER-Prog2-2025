# auto.py

from vehiculo import Vehiculo 

class Auto(Vehiculo):
    # Constructor
    def __init__(self, numeroId: int, marca: str, modelo: str, anio: str,
                 sucursalId: int, estadoId: int,
                 airbags: int, frenosAbs: bool, caballosFuerza: int):
        # Llamada al constructor de la clase base Vehiculo
        super().__init__(numeroId, marca, modelo, anio, sucursalId, estadoId)
        # Atributos propios de Auto
        self.__airbags = airbags
        self.__frenosAbs = frenosAbs
        self.__caballosFuerza = caballosFuerza

    # --- Comandos ---
    def establecerAirbags(self, airbags: int):
        self.__airbags = airbags

    def establecerFrenosAbs(self, frenosAbs: bool):
        self.__frenosAbs = frenosAbs

    def establecerCaballosFuerza(self, caballosFuerza: int):
        self.__caballosFuerza = caballosFuerza

    # --- Consultas---
    def obtenerAirbags(self) -> int:
        return self.__airbags

    def obtenerFrenosAbs(self) -> bool:
        return self.__frenosAbs

    def obtenerCaballosFuerza(self) -> int:
        return self.__caballosFuerza
