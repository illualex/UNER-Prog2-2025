class Concesionaria:

    def __init__(self, numero_id, nombre):
        self.__numero_id = numero_id
        self.__nombre = nombre
        self.__clientes = []
        self.__sucursales = []
        self.__vehiculos = []

    def establecer_numero_id(self, numero_id):
        self.__numero_id = numero_id

    def establecer_nombre(self, nombre):
        self.__nombre = nombre

    def agregar_cliente(self, cliente):
        self.__clientes.append(cliente)

    def remover_cliente(self, cliente):
        self.__clientes.remove(cliente)

    def agregar_sucursal(self, sucursal):
        self.__sucursales.append(sucursal)

    def remover_sucursal(self, sucursal):
        self.__sucursales.remove(sucursal)

    def agregar_vehiculo(self, vehiculo):
        self.__vehiculos.append(vehiculo)

    def remover_vehiculo(self, vehiculo):
        self.__vehiculos.remove(vehiculo)

    def obtener_numero_id(self):
        return self.__numero_id

    def obtener_nombre(self):
        return self.__nombre

    def obtener_clientes(self):
        return self.__clientes

    def obtener_sucursales(self):
        return self.__sucursales

    def obtener_vehiculos(self):
        return self.__vehiculos

    # >> Ejercicio 5 - __eq__ <<
    def __eq__(self, other):
        if isinstance(other, Concesionaria):
            return self.__numero_id == other.__numero_id
        return False

    # >> Ejercicio 5 - __str__ <<
    def __str__(self):
        clientes = ", ".join(str(c.obtener_numero_id()) for c in self.__clientes)
        sucursales = ", ".join(str(s.obtener_numero_id()) for s in self.__sucursales)
        vehiculos = ", ".join(str(v.obtener_numero_id()) for v in self.__vehiculos)

        return (
            f"Concesionaria(ID: {self.__numero_id}, Nombre: {self.__nombre}, "
            f"Clientes: [{clientes}], Sucursales: [{sucursales}], Vehiculos: [{vehiculos}])"
        )
