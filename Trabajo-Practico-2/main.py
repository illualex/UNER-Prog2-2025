# =========================================
# Trabajo Práctico n°2 - Programación 2
# Sección B - Ejercicios 1 al 10
# Integrantes:
# - Alejo Paniagua
# - Sabrina Bidal
# - Francisco Diaz
# =========================================

# Importación para el ejercicio 1
from cancion import Cancion

# Importación para el ejercicio 5
from circulo import Circulo

# =========================================
# Ejercicio 2
# =========================================
cancion1 = Cancion("Imagine", 183, "Pop")
cancion2 = Cancion("Bohemian Rhapsody", 354, "Rock")
cancion3 = Cancion("Billie Jean", 294, "Pop")


def ejercicio_2():
    print("Se crearon las siguientes canciones:")
    print("-", cancion1.obtenerNombre())
    print("-", cancion2.obtenerNombre())
    print("-", cancion3.obtenerNombre())
    input("\nPresione Enter para continuar...")


# =========================================
# Ejercicio 3
# =========================================
def ejercicio_3():
    print("Género de las canciones")
    print(f"- {cancion1.obtenerNombre()}: {cancion1.obtenerGenero()}")
    print(f"- {cancion2.obtenerNombre()}: {cancion2.obtenerGenero()}")
    print(f"- {cancion3.obtenerNombre()}: {cancion3.obtenerGenero()}")
    input("\nPresione Enter para continuar...")


# =========================================
# Ejercicio 4
# =========================================
def ejercicio_4():
    print("Antes de modificar:")
    print(f"- {cancion1.obtenerNombre()}: {cancion1.obtenerGenero()}")

    cancion1.establecerGenero("Rock")

    print("\nDespués de modificar:")
    print(f"- {cancion1.obtenerNombre()}: {cancion1.obtenerGenero()}")
    input("\nPresione Enter para continuar...")


# =========================================
# Ejercicio 6
# =========================================
circulo1 = Circulo(3)
circulo2 = Circulo(5.5)
circulo3 = Circulo(10)


def ejercicio_6():
    print("Se crearon 3 círculos con radios:")
    print("Círculo 1:", circulo1.obtenerRadio())
    print("Círculo 2:", circulo2.obtenerRadio())
    print("Círculo 3:", circulo3.obtenerRadio())
    input("\nPresione Enter para continuar...")


# =========================================
# Menú principal
# =========================================
def menu():
    while True:
        print("\n====== Menú de Ejercicios TP-N2 ======")
        print("2. Ejercicio 2 - Canciones")
        print("3. Ejercicio 3 - Género de las canciones")
        print("4. Ejercicio 4 - Modificar género de una canción")
        print("6. Ejercicio 6 - 3 Círculos")
        print("7. Ejercicio 7 - ")
        print("9. Ejercicio 9 - ")
        print("10. Ejercicio 10 - ")
        print("0. Salir")

        opcion = input("\n> Seleccione una opción: ")

        if opcion == "2":
            print("\n<<<-- Ejercicio 2 -->>>")
            ejercicio_2()

        elif opcion == "3":
            print("\n<<<-- Ejercicio 3 -->>>")
            ejercicio_3()

        elif opcion == "4":
            print("\n<<<-- Ejercicio 4 -->>>")
            ejercicio_4()

        elif opcion == "6":
            print("\n<<<-- Ejercicio 6 -->>>")
            ejercicio_6()

        elif opcion == "7":
            pass

        elif opcion == "8":
            pass

        elif opcion == "9":
            pass

        elif opcion == "10":
            pass

        elif opcion == "0":
            print("Finalizando el programa...")
            break
        else:
            print("\nOpción no válida. Intente de nuevo.")
            input("Presione Enter para continuar...")


if __name__ == "__main__":
    menu()
