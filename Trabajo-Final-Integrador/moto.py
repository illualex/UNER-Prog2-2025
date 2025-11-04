import vehiculo


class Moto(vehiculo.Vehiculo):
    def __init__(
        self, numero_id, marca, modelo, anio, sucursal_id, estado_id, cilindrada
    ):
        super().__init__(numero_id, marca, modelo, anio, sucursal_id, estado_id)
        self.__cilindrada = cilindrada

    def establecer_cilindrada(self, cilindrada):
        self.__cilindrada = cilindrada

    def obtener_cilindrada(self):
        return self.__cilindrada

    # >> Ejercicio 5 - __str__ <<
    def __str__(self) -> str:
        return (
            f"Moto("
            f"numero_id={self.obtener_numero_id()}, "
            f"marca='{self.obtener_marca()}', "
            f"modelo='{self.obtener_modelo()}', "
            f"anio='{self.obtener_anio()}', "
            f"sucursal_id={self.obtener_sucursal_id()}, "
            f"estado_id={self.obtener_estado_id()}, "
            f"cilindrada={self.__cilindrada}"
            f")"
        )
