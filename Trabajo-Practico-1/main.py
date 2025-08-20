# =========================================
# Trabajo Práctico n°1 - Programación 2
# Sección B - Ejercicios 1 al 10
# =========================================

# -- Importación para el ejercicio 7/8 descomentarlo despues
# from impresiones import declarar_comida_favorita

# =========================================
# Ejercicio 1
# =========================================
def realizar_calculo():
    pass


# =========================================
# Ejercicio 2
# =========================================
def numero_en_orden_ascendente(numero):
    pass


# =========================================
# Ejercicio 3
# =========================================
def numeros_impares_juntos(entrada):
    pass


# =========================================
# Ejercicio 4
# =========================================
def lista_elementos_en_comun(lista1, lista2):
    pass


# =========================================
# Ejercicio 5
# =========================================
def clave_valida(clave):
    pass


# =========================================
# Ejercicio 6
# =========================================
def persona_mayor_de_edad(edad):
    pass


# =========================================
# Ejercicio 7
# =========================================
def declarar_comida_favorita(nombre_persona, nombre_comida):
    pass


# =========================================
# Ejercicio 8
# =========================================
def ejercicio_8():
    pass


# =========================================
# Ejercicio 9
# =========================================
def cuenta_regresiva(entero_positivo):
    pass


# =========================================
# Ejercicio 10
# =========================================
def simplificar_expresion(a, b):
    pass


# =========================================
# Menú principal
# =========================================
def menu():
    while True:
        print("\n=== Menú de Ejercicios TP-N1 ===")
        print("1. Ejercicio 1 - realizar_calculo()")
        print("2. Ejercicio 2 - numero_en_orden_ascendente()")
        print("3. Ejercicio 3 - numeros_impares_juntos()")
        print("4. Ejercicio 4 - lista_elementos_en_comun()")
        print("5. Ejercicio 5 - clave_valida()")
        print("6. Ejercicio 6 - persona_mayor_de_edad()")
        print("7. Ejercicio 7 - declarar_comida_favorita()")
        print("8. Ejercicio 8 - ejercicio_8()")
        print("9. Ejercicio 9 - cuenta_regresiva()")
        print("10. Ejercicio 10 - simplificar_expresion()")
        print("0. Salir")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            realizar_calculo()
        elif opcion == "2":
            numero_en_orden_ascendente(numero)
        elif opcion == "3":
            numeros_impares_juntos(entrada)
        elif opcion == "4":
            lista_elementos_en_comun(lista1, lista2)
        elif opcion == "5":
            clave_valida(clave)
        elif opcion == "6":
            persona_mayor_de_edad(edad)
        elif opcion == "7":
            declarar_comida_favorita(nombre_persona, nombre_comida)
        elif opcion == "8":
            ejercicio_8()
        elif opcion == "9":
            cuenta_regresiva(entero_positivo)
        elif opcion == "10":
            simplificar_expresion(a, b)
        elif opcion == "0":
            print("Saliendo del programa...")
            break
        else:
            print("\nOpción no válida. Intente de nuevo.")
            input("Presione Enter para continuar...")



if __name__ == "__main__":
    menu()
