# =========================================
# Ejercicio 4 - Clase Venta
# =========================================


class Venta:
    # << Constructores >>
    def __init__(
        self, numero_id: int, fecha: str, cliente_id: int, vehiculo_id: int, monto: int
    ):
        self.__numero_id = numero_id
        self.__fecha = fecha
        self.__cliente_id = cliente_id
        self.__vehiculo_id = vehiculo_id
        self.__monto = monto

    # << Comandos >>
    def establecer_numero_id(self, numero_id: int):
        self.__numero_id = numero_id

    def establecer_fecha(self, fecha: str):
        self.__fecha = fecha

    def establecer_cliente_id(self, cliente_id: int):
        self.__cliente_id = cliente_id

    def establecer_vehiculo_id(self, vehiculo_id: int):
        self.__vehiculo_id = vehiculo_id

    def establecer_monto(self, monto: int):
        self.__monto = monto

    # << Consultas >>
    def obtener_numero_id(self) -> int:
        return self.__numero_id

    def obtener_fecha(self) -> str:
        return self.__fecha

    def obtener_cliente_id(self) -> int:
        return self.__cliente_id

    def obtener_vehiculo_id(self) -> int:
        return self.__vehiculo_id

    def obtener_monto(self) -> int:
        return self.__monto

    # >> Ejercicio 5 - __eq__ <<
    def __eq__(self, other):
        # Comparación por numero_id
        if isinstance(other, Venta):
            return self.__numero_id == other.__numero_id
        return False

    # >> Ejercicio 5 - __str__ <<
    def __str__(self):
        # Representación completa de la venta
        return (
            f"Venta("
            f"numero_id={self.__numero_id}, fecha='{self.__fecha}', "
            f"cliente_id={self.__cliente_id}, vehiculo_id={self.__vehiculo_id}, "
            f"monto={self.__monto}"
            f")"
        )
