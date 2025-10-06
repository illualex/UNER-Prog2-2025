# =========================================
# Trabajo Práctico n°3 - Programación 2
# Sección B - Ejercicios 1 al 10
# Integrantes:
# - Alejo Paniagua
# - Sabrina Bidal
# - Francisco Diaz
# =========================================

# Importaciones
from empresa import Empresa
from producto import Producto
from empleado import Empleado


# =========================================
# Ejercicio 7
# =========================================
def ejercicio_7():
    empresa = Empresa("Demo S.A.")

    # -- Crear empleados --
    emp1 = Empleado("Juan", "Pérez")
    emp2 = Empleado("Ana", "García")
    emp3 = Empleado("Lucas", "Díaz")

    # -- Dar de alta los empleados --
    empresa.altaEmpleado(emp1)
    empresa.altaEmpleado(emp2)
    empresa.altaEmpleado(emp3)

    # -- Dar de baja a uno --
    empresa.bajaEmpleado(emp2)

    # -- Mostrar empleados de alta --
    print("\nEmpleados de alta:")
    for e in empresa.obtenerEmpleadosDeAlta():
        print(e)

    # -- Mostrar empleados históricos --
    print("\nEmpleados históricos:")
    for e in empresa.obtenerEmpleadoHistorico():
        print(e)

    input("\nPresione Enter para continuar...")


# =========================================
# Ejercicio 10
# =========================================
def ejercicio_10():
    # -- Crear dos empresas --
    empresa1 = Empresa("Tech Solutions S.A.")
    empresa2 = Empresa("EcoMarket SRL")

    # -- Crear productos --
    prod1 = Producto("Laptop")
    prod2 = Producto("Mouse")
    prod3 = Producto("Verduras orgánicas")
    prod4 = Producto("Frutas frescas")

    # -- Agregar productos a cada empresa --
    empresa1.agregarProducto(prod1)
    empresa1.agregarProducto(prod2)
    empresa2.agregarProducto(prod3)
    empresa2.agregarProducto(prod4)

    # -- Crear empleados --
    emp1 = Empleado("Juan", "Pérez")
    emp2 = Empleado("Ana", "García")
    emp3 = Empleado("Lucas", "Díaz")
    emp4 = Empleado("Sofía", "Martínez")
    emp5 = Empleado("Marcos", "López")
    emp6 = Empleado("Lucía", "Fernández")

    # -- Dar de alta los empleados en las empresas --
    empresa1.altaEmpleado(emp1)
    empresa1.altaEmpleado(emp2)
    empresa1.altaEmpleado(emp3)

    empresa2.altaEmpleado(emp4)
    empresa2.altaEmpleado(emp5)
    empresa2.altaEmpleado(emp6)

    # -- Dar de baja a dos empleados de empresa1 --
    empresa1.bajaEmpleado(emp2)
    empresa1.bajaEmpleado(emp3)

    # -- Mostrar información de ambas empresas --
    print("\n--- Información de las empresas ---\n")
    print(empresa1)
    print("\n-----------------------------\n")
    print(empresa2)

    input("\nPresione Enter para continuar...")


# =========================================
# Menú principal
# =========================================
def menu():
    while True:
        print("\n====== Menú de Ejercicios TP-N3 ======")
        print("7. Ejercicio 7 - Empleados de alta e histórico")
        print("10. Ejercicio 10 - Crear empresas y mostrar datos")
        print("0. Salir")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "7":
            print("\n<<<-- Ejercicio 7 -->>>")
            ejercicio_7()
        elif opcion == "10":
            print("\n<<<-- Ejercicio 10 -->>>")
            ejercicio_10()
        elif opcion == "0":
            print("\nSaliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    menu()
