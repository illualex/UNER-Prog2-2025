# =========================================
# Ejercicio 1 - Clase Sucursal
# =========================================

# Importaciones necesarias
from typing import List
from venta import Venta


class Sucursal:
    # << Constructores >>
    def __init__(self, numero_id: int, direccion: str):
        self.__numero_id = numero_id
        self.__direccion = direccion
        self.__ventas: List[Venta] = []

    # << Comandos >>
    def establecer_numero_id(self, numero_id: int):
        self.__numero_id = numero_id

    def establecer_direccion(self, direccion: str):
        self.__direccion = direccion

    def agregar_venta(self, venta: Venta):
        self.__ventas.append(venta)

    def remover_venta(self, venta: Venta):
        if venta in self.__ventas:
            self.__ventas.remove(venta)

    # << Consultas >>
    def obtener_numero_id(self) -> int:
        return self.__numero_id

    def obtener_direccion(self) -> str:
        return self.__direccion

    def obtener_ventas(self) -> List[Venta]:
        return self.__ventas

    # >> Ejercicio 5 - __eq__ <<
    def __eq__(self, other):
        if isinstance(other, Sucursal):
            return self.__numero_id == other.__numero_id
        return False

    # >> Ejercicio 5 - __str__ <<
    def __str__(self):
        texto_ventas = "\n    ".join(str(venta) for venta in self.__ventas)
        return (
            f"Sucursal #{self.__numero_id} | Dirección: {self.__direccion}\n"
            f"  Ventas:\n    {texto_ventas if texto_ventas else 'Sin ventas registradas'}"
        )
