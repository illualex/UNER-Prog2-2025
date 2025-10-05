# =========================================
# Ejercicio 4 y 7
# =========================================

from producto import Producto
from empleado import Empleado


class Empresa:
    def __init__(self, razon_social: str):
        self.__razon_social = razon_social
        self.__productos = []
        self.__empleados = []

    def establecerRazonSocial(self, razon_social):
        self.__razon_social = razon_social

    def agregarProducto(self, producto: Producto):
        self.__productos.append(producto)

    def removerProducto(self, producto: Producto):
        self.__productos.remove(producto)

    def altaEmpleado(self, empleado: Empleado):
        self.__empleados.append(empleado)

    def bajaEmpleado(self, empleado: Empleado):
        empleado.establecerEstado(Empleado.ESTADO_BAJA)

    def obtenerRazonSocial(self) -> str:
        return self.__razon_social

    def obtenerProductos(self) -> list:
        return self.__productos

    # --- Ejercicio 7B ---
    def obtenerEmpleadosDeAlta(self) -> list:
        return [
            e for e in self.__empleados if e.obtenerEstado() == Empleado.ESTADO_ALTA
        ]

    # --- Ejercicio 7B ---
    def obtenerEmpleadosHistorico(self) -> list:
        return self.__empleados

    def __str__(self):
        productos = ", ".join(str(p) for p in self.__productos) or "Sin productos"
        empleados = (
            ", ".join(str(e) for e in self.obtenerEmpleadosDeAlta())
            or "Sin empleados de alta"
        )
        return f"Empresa: {self.__razon_social}\nProductos: {productos}\nEmpleados de alta: {empleados}"

    def __eq__(self, other):
        if isinstance(other, Empresa):
            return other.__razon_social == self.__razon_social
        return NotImplemented
