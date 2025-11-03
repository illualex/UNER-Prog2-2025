# Ejercicio 4 - clase Venta

class Venta:
    def __init__(self, numero_id: int, fecha: str, cliente_id: int, vehiculo_id: int, monto: int):
        self.__numero_id = numero_id
        self.__fecha = fecha
        self.__cliente_id = cliente_id
        self.__vehiculo_id = vehiculo_id
        self.__monto = monto

    # Comandos
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

    # Consultas
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


    # Ejercicio 5 - implementacion __str__ y __eq__
    def __eq__(self, other):
        if isinstance(other, Venta):
            return self.__numero_id == other.__numero_id
        return False

    def __str__(self):
        return (
            f"Venta #{self.__numero_id} | Fecha: {self.__fecha} | "
            f"Cliente ID: {self.__cliente_id} | Vehículo ID: {self.__vehiculo_id} | "
            f"Monto: ${self.__monto}"
        )