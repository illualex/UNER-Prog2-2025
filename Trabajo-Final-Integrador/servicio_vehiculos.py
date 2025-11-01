# =========================================
# Ejercicio 7 - obtener_vehiculos_por_sucursal_y_estado
# =========================================

from servicio_concesionarias import ServicioConcesionarias
from typing import List


class ServicioVehiculos:

    def obtener_vehiculos_por_sucursal_y_estado(
        self, concesionaria_id: int, sucursal_id: int, estado_id: int
    ) -> List:
        servicio_conc = ServicioConcesionarias()
        concesionaria = servicio_conc.obtener_por_id(concesionaria_id)

        if concesionaria is None:
            return []

        # Buscar sucursal
        sucursal = None
        for s in concesionaria.obtener_sucursales():
            if s.obtener_numero_id() == sucursal_id:
                sucursal = s
                break

        if sucursal is None:
            return []

        # Filtrar vehículos por sucursal y estado
        vehiculos = concesionaria.obtener_vehiculos()
        return [
            v
            for v in vehiculos
            if v.obtener_sucursal_id() == sucursal_id
            and v.obtener_estado_id() == estado_id
        ]
