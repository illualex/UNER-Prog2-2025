# =========================================
# Ejercicio 2, 3, 6 y 8
# =========================================


class Empleado:
    ESTADO_ALTA = 1
    ESTADO_BAJA = 2

    def __init__(self, nombres: str, apellidos: str):
        self.__numeroLegajo = None
        self.__nombres = nombres
        self.__apellidos = apellidos

        # --- Ejercicio 3 ---
        self.__estado = Empleado.ESTADO_ALTA

    def establecerNumeroLegajo(self, numero: int):
        self.__numeroLegajo = numero

    def establecerNombres(self, nombres: str):
        self.__nombres = nombres

    def establecerApellidos(self, apellidos: str):
        self.__apellidos = apellidos

    def establecerEstado(self, estado: int):
        self.__estado = estado

    def obtenerNumeroLegajo(self) -> int:
        return self.__numeroLegajo

    def obtenerNombres(self) -> str:
        return self.__nombres

    def obtenerApellidos(self) -> str:
        return self.__apellidos

    def obtenerEstado(self) -> int:
        return self.__estado

    # --- Ejercicio 6 ---
    def bajaEmpleado(self):
        self.__estado = Empleado.ESTADO_BAJA

    # --- Ejercicio 8 ---
    def __str__(self):
        estado_str = "Alta" if self.__estado == Empleado.ESTADO_ALTA else "Baja"
        return f"Legajo: {self.__numeroLegajo}, Nombre: {self.__nombres} {self.__apellidos}, Estado: {estado_str}"

    # --- Ejercicio 8 ---
    def __eq__(self, other):
        if isinstance(other, Empleado):
            return self.__numeroLegajo == other.__numeroLegajo
        return False
