# ----- Proyecto Concesionarias - Grupo CJ -----
## Integrantes del Grupo
- **Alejo Paniagua**
- **Sabrina Bidal**
- **Francisco Diaz**

## Instalación y ejecución
1. Instalar dependencias:
    pip install flask

2. Ejecutar el servidor Flask:
    python -m flask run

## Links de prueba
- Devuelve toda la información de la concesionaria:
    http://localhost:5000/concesionarias/1/
>Respuesta: 
    Concesionaria(ID: 1, Nombre: Vehiculos de primera, Clientes: [1, 2], Sucursales: [1, 2], Vehiculos: [1, 2, 3, 4, 5, 6, 7])

- Cliente 1:
    http://localhost:5000/concesionarias/1/clientes/1/total-ventas/
> Respuesta:
    15000000

- Cliente 2:
    http://localhost:5000/concesionarias/1/clientes/2/total-ventas/
> Respuesta:
    3000000

- Cliente inexistente:
    http://localhost:5000/concesionarias/1/clientes/3/total-ventas/
> Respuesta:
    0

- Sucursal 1, estado 1:
    http://localhost:5000/concesionarias/1/sucursales/1/vehiculos?estado_id=1
> Respuesta (Corolla y Golf):
    Vehículos:
        Auto(numero_id=1, marca='Toyota', modelo='Corolla', anio='2020', sucursal_id=1, estado_id=1, airbags=7, frenos_abs=True, caballos_fuerza=169)
        Auto(numero_id=2, marca='Volkswagen', modelo='Golf', anio='2019', sucursal_id=1, estado_id=1, airbags=7, frenos_abs=True, caballos_fuerza=148)

- Sucursal 1, estado 2:
    http://localhost:5000/concesionarias/1/sucursales/1/vehiculos?estado_id=2
> Respuesta (Focus):
    Vehículos:
        Auto(numero_id=3, marca='Ford', modelo='Focus', anio='2018', sucursal_id=1, estado_id=2, airbags=6, frenos_abs=True, caballos_fuerza=168)

- Vehículos Sucursal 2, estado 2:
    http://localhost:5000/concesionarias/1/sucursales/2/vehiculos/?estado_id=2
> Respuesta (FZ25):
    Vehículos:
        Moto(numero_id=7, marca='Yamaha', modelo='FZ25', anio='2020', sucursal_id=2, estado_id=2, cilindrada=249)

- Sucursal inexistente:
    http://localhost:5000/concesionarias/1/sucursales/3/vehiculos?estado_id=1
> Respuesta (vació):
    Vehículos: