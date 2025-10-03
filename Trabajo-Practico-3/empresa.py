# =========================================
# Ejercicio 4
# =========================================

from producto import Producto
from empleado import Empleado


class Empresa:
    def __init__(self, razon_social: str):
        self.__razon_social = razon_social
        self.__productos = []
        self.__empleados = []

    def establecer_razon_social(self, razon_social):
        self.__razon_social = razon_social

    def agregar_producto(self, producto: Producto):
        self.__productos.append(producto)

    def remover_producto(self, producto: Producto):
        self.__productos.remove(producto)

    def alta_empleado(self, empleado: Empleado):
        self.__empleados.append(empleado)

    def baja_empleado(self, empleado: Empleado):
        empleado.establecer_estado(Empleado.ESTADO_BAJA)

    def obtener_razon_social(self) -> str:
        return self.__razon_social

    def obtener_productos(self) -> list:
        return self.__productos

    def obtener_empleados_de_alta(self) -> list:
        return [
            e for e in self.__empleados if e.obtener_estado() == Empleado.ESTADO_ALTA
        ]

    def obtener_empleados_historico(self) -> list:
        return self.__empleados

    def __str__(self):
        productos = ", ".join(str(p) for p in self.__productos) or "Sin productos"
        empleados = (
            ", ".join(str(e) for e in self.obtener_empleados_de_alta())
            or "Sin empleados de alta"
        )
        return f"Empresa: {self.__razon_social}\nProductos: {productos}\nEmpleados de alta: {empleados}"

    def __eq__(self, other):
        if isinstance(other, Empresa):
            return other.__razon_social == self.__razon_social
        return NotImplemented
