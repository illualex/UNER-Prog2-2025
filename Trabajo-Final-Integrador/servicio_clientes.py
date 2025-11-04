# =========================================
# Ejercicio 6 - Clase ServicioClientes
# =========================================

# Importación de la clase ServicioConcesionarias
from servicio_concesionarias import ServicioConcesionarias

class ServicioClientes:
    # << Consultas >>
    def obtener_total_ventas_por_cliente(
        self, concesionaria_id: int, cliente_id: int
    ) -> int:
        cliente_id = int(cliente_id)
        servicio_conc = ServicioConcesionarias()
        concesionaria = servicio_conc.obtener_por_id(concesionaria_id)

        if concesionaria is None:
            return 0

        clientes = concesionaria.obtener_clientes()
        cliente_existe = any(c.obtener_numero_id() == cliente_id for c in clientes)
        if not cliente_existe:
            return 0

        total = sum(
            int(venta.obtener_monto())
            for sucursal in concesionaria.obtener_sucursales()
            for venta in sucursal.obtener_ventas()
            if venta.obtener_cliente_id() == cliente_id
        )

        return total
