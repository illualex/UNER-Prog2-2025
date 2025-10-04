# empleado.py

class Empleado:
    # Atributos de clase
    ESTADO_ALTA = 1
    ESTADO_BAJA = 2

    # Constructor
    def __init__(self, nombres: str, apellidos: str):
        self.numeroLegajo = None
        self.nombres = nombres
        self.apellidos = apellidos
        self.estado = Empleado.ESTADO_ALTA

    # Comandos (setters)
    def establecerNumeroLegajo(self, numero: int):
        self.numeroLegajo = numero

    def establecerNombres(self, nombres: str):
        self.nombres = nombres

    def establecerApellidos(self, apellidos: str):
        self.apellidos = apellidos

    def establecerEstado(self, estado: int):
        self.estado = estado

    # Consultas (getters)
    def obtenerNumeroLegajo(self) -> int:
        return self.numeroLegajo

    def obtenerNombres(self) -> str:
        return self.nombres

    def obtenerApellidos(self) -> str:
        return self.apellidos

    def obtenerEstado(self) -> int:
        return self.estado
    def bajaEmpleado(self):
        """Cambia el estado del empleado a BAJA."""
        self.estado = Empleado.ESTADO_BAJA
    def __str__(self):
        estado_str = "Alta" if self.estado == Empleado.ESTADO_ALTA else "Baja"
        return f"Legajo: {self.numeroLegajo}, Nombre: {self.nombres} {self.apellidos}, Estado: {estado_str}"

    def __eq__(self, other):
        if isinstance(other, Empleado):
          return self.numeroLegajo == other.numeroLegajo
        return False
