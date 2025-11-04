# =========================================
# Ejercicio 3 - Clase Auto
# =========================================

# Importación de la clase Vehículo
from vehiculo import Vehiculo


class Auto(Vehiculo):
    # << Atributos de Instancia >>
    def __init__(
        self,
        numero_id: int,
        marca: str,
        modelo: str,
        anio: str,
        sucursal_id: int,
        estado_id: int,
        airbags: int,
        frenos_abs: bool,
        caballos_fuerza: int,
    ):
        # << Constructores >>
        super().__init__(numero_id, marca, modelo, anio, sucursal_id, estado_id)
        self.__airbags = airbags
        self.__frenos_abs = frenos_abs
        self.__caballos_fuerza = caballos_fuerza

    # << Comandos >>
    def establecer_airbags(self, airbags: int):
        self.__airbags = airbags

    def establecer_frenos_abs(self, frenos_abs: bool):
        self.__frenos_abs = frenos_abs

    def establecer_caballos_fuerza(self, caballos_fuerza: int):
        self.__caballos_fuerza = caballos_fuerza

    # << Consultas >>
    def obtener_airbags(self) -> int:
        return self.__airbags

    def obtener_frenos_abs(self) -> bool:
        return self.__frenos_abs

    def obtener_caballos_fuerza(self) -> int:
        return self.__caballos_fuerza

    # >> Ejercicio 5 - __str__ <<
    def __str__(self) -> str:
        return (
            f"Auto("
            f"numero_id={self.obtener_numero_id()}, "
            f"marca='{self.obtener_marca()}', "
            f"modelo='{self.obtener_modelo()}', "
            f"anio='{self.obtener_anio()}', "
            f"sucursal_id={self.obtener_sucursal_id()}, "
            f"estado_id={self.obtener_estado_id()}, "
            f"airbags={self.__airbags}, "
            f"frenos_abs={self.__frenos_abs}, "
            f"caballos_fuerza={self.__caballos_fuerza}"
            f")"
        )
