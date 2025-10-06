# =========================================
# Ejercicio 4, 5, 6, 7 y 8
# =========================================

from producto import Producto
from empleado import Empleado


class Empresa:
    def __init__(self, razon_social: str):
        self.__razon_social = razon_social
        self.__productos = []
        self.__empleados = []

    # --- Ejercicio 5 ---
    def __obtenerMaximoLegajo(self) -> int:
        if not self.__empleados:
            return 0
        legajos_validos = [
            e.obtenerNumeroLegajo()
            for e in self.__empleados
            if e.obtenerNumeroLegajo() is not None
        ]
        return max(legajos_validos) if legajos_validos else 0

    def establecerRazonSocial(self, razon_social):
        self.__razon_social = razon_social

    def agregarProducto(self, producto: Producto):
        self.__productos.append(producto)

    def removerProducto(self, producto: Producto):
        self.__productos.remove(producto)

    # --- Ejercicio 5 ---
    def altaEmpleado(self, empleado: Empleado):
        maximo_legajo_actual = self.__obtenerMaximoLegajo()
        nuevo_legajo = maximo_legajo_actual + 1
        empleado.establecerNumeroLegajo(nuevo_legajo)
        self.__empleados.append(empleado)

    # --- Ejercicio 6 ---
    def bajaEmpleado(self, empleado: Empleado):
        empleado.establecerEstado(Empleado.ESTADO_BAJA)

    def obtenerRazonSocial(self) -> str:
        return self.__razon_social

    def obtenerProductos(self) -> list:
        return self.__productos

    # --- Ejercicio 7 ---
    def obtenerEmpleadosDeAlta(self) -> list:
        return [
            e for e in self.__empleados if e.obtenerEstado() == Empleado.ESTADO_ALTA
        ]

    # --- Ejercicio 7 ---
    def obtenerEmpleadoHistorico(self) -> list:
        """Retorna todos los empleados sin importar su estado actual."""
        return self.__empleados

    # --- Ejercicio 8 ---
    def __str__(self):
        productos = ", ".join(str(p) for p in self.__productos) or "Sin productos"
        empleados = (
            ", ".join(str(e) for e in self.obtenerEmpleadosDeAlta())
            or "Sin empleados de alta"
        )
        return (
            f"Empresa: {self.__razon_social}\n"
            f"Productos: {productos}\n"
            f"Empleados de alta: {empleados}"
        )

    # --- Ejercicio 8 ---
    def __eq__(self, other):
        if isinstance(other, Empresa):
            return self.__razon_social == other.__razon_social
        return False
