# =========================================
# Ejercicio 6 - obtener_total_ventas_por_cliente
# =========================================

# Importación: servicio concesionarias
from servicio_concesionarias import ServicioConcesionarias


class ServicioClientes:

    def obtener_total_ventas_por_cliente(
        self, concesionaria_id: int, cliente_id: int
    ) -> int:
        servicio_conc = ServicioConcesionarias()
        concesionaria = servicio_conc.obtener_por_id(concesionaria_id)

        if concesionaria is None:
            return 0

        # Verificar existencia del cliente
        clientes = concesionaria.obtener_clientes()
        cliente_existe = any(c.obtener_numero_id() == cliente_id for c in clientes)
        if not cliente_existe:
            return 0

        # Sumar montos de ventas al cliente en todas las sucursales
        total = sum(
            int(venta.obtener_monto())
            for sucursal in concesionaria.obtener_sucursales()
            for venta in sucursal.obtener_ventas()
            if venta.obtener_cliente_id() == cliente_id
        )

        return total
