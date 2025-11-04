# =========================================
# Ejercicio 1 - generar la clase sucursal.py
# =========================================


class Sucursal:
    # Constructor
    def __init__(self, numeroId: int, direccion: str):
        self.__numeroId = numeroId
        self.__direccion = direccion
        self.__ventas: List[Venta] = []

    # --- Comandos (modificadores) ---
    def establecerNumeroId(self, numeroId: int):
        self.__numeroId = numeroId

    def establecerDireccion(self, direccion: str):
        self.__direccion = direccion

    def agregarVenta(self, venta: Venta):
        self.__ventas.append(venta)

    def removerVenta(self, venta: Venta):
        if venta in self.__ventas:
            self.__ventas.remove(venta)

    # --- Consultas ( ---
    def obtenerNumeroId(self) -> int:
        return self.__numeroId

    def obtenerDireccion(self) -> str:
        return self.__direccion

    def obtenerVentas(self) -> List[Venta]:
        return self.__ventas
