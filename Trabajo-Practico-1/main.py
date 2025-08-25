# =========================================
# Trabajo Práctico n°1 - Programación 2
# Sección B - Ejercicios 1 al 10
# Integrantes: 
# - Alejo Paniagua
# - Sabrina Bidal
# - 
# =========================================

# Importación para el ejercicio 8
from impresiones import declarar_comida_favorita



# =========================================
# Ejercicio 1
# =========================================
def realizar_calculo():
    pass


# =========================================
# Ejercicio 2
# =========================================
def numero_en_orden_ascendente(numero):
    digitos = [int(d) for d in str(numero)]
    return digitos == sorted(digitos)


# =========================================
# Ejercicio 3
# =========================================
def numeros_impares_juntos(entrada):
    impares = [str(n) for n in entrada if n % 2 != 0]
    if not impares:
        return "No hay números impares"
    return ",".join(impares)


# =========================================
# Ejercicio 4
# =========================================
def lista_elementos_en_comun(lista1, lista2):
    elementos_comunes = set(lista1) & set(lista2)
    for elemento in elementos_comunes:
        print(elemento)


# =========================================
# Ejercicio 5
# =========================================
def clave_valida(clave):
    pass


# =========================================
# Ejercicio 6
# =========================================
def persona_mayor_de_edad(edad):
    return edad >= 18


# =========================================
# Ejercicio 9
# =========================================
def cuenta_regresiva(entero_positivo):
    print(entero_positivo)
    if entero_positivo > 0:
        cuenta_regresiva(entero_positivo - 1)


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
        print("\n====== Menú de Ejercicios TP-N1 ======")
        print("1. Ejercicio 1 - realizar_calculo()")
        print("2. Ejercicio 2 - numero_en_orden_ascendente()")
        print("3. Ejercicio 3 - numeros_impares_juntos()")
        print("4. Ejercicio 4 - lista_elementos_en_comun()")
        print("5. Ejercicio 5 - clave_valida()")
        print("6. Ejercicio 6 - persona_mayor_de_edad()")
        print("7. Ejercicio 7 - declarar_comida_favorita()")
        print("9. Ejercicio 9 - cuenta_regresiva()")
        print("10. Ejercicio 10 - simplificar_expresion()")
        print("0. Salir")

        opcion = input("\n> Seleccione una opción: ")

        if opcion == "1":
            realizar_calculo()


        elif opcion == "2":
            print("\n<<<-- Ejercicio 2 -->>>")
            entrada = input("Ingrese varios números (ej: 12345 o 1 2 3 4 5): ")
            numero = int(entrada.replace(" ", "")) 
            if numero_en_orden_ascendente(numero):
                print("> Los dígitos están en orden ascendente")
            else:
                print("> Los dígitos NO están en orden ascendente")
            input("\nPresione Enter para continuar...")


        elif opcion == "3":
            print("\n<<<-- Ejercicio 3 -->>>")
            entrada = input("Ingrese números separados por comas (ej: 1,2,3 o 1, 2, 3): ")
            entrada = entrada.replace(" ", ",")
            lista_numeros = [int(x.strip()) for x in entrada.split(",") if x.strip() != '']
            resultado = numeros_impares_juntos(lista_numeros)
            print("> Números impares juntos:", resultado)
            input("\nPresione Enter para continuar...")


        elif opcion == "4":
            lista1 = [1, 2, 3, 4, 5]
            lista2 = [3, 4, 5, 6, 7]
            lista_elementos_en_comun(lista1, lista2)


        elif opcion == "5":
            clave_valida(clave)


        elif opcion == "6":
            print("\n<<<-- Ejercicio 6 -->>>")
            edad = int(input("Ingrese la edad: "))
            if persona_mayor_de_edad(edad):
                print("> Es mayor de edad")
            else:
                print("> No es mayor de edad")
            input("\nPresione Enter para continuar...")


        elif opcion == "7":
            declarar_comida_favorita("Pablo", "pollo frito")
            declarar_comida_favorita("Pedro", "canelones")
            declarar_comida_favorita("Juan", "pizza")


        elif opcion == "9":
            cuenta_regresiva(4)


        elif opcion == "10":
            simplificar_expresion(a, b)


        elif opcion == "0":
            print("Finalizando el programa...")
            break
        else:
            print("\nOpción no válida. Intente de nuevo.")
            input("Presione Enter para continuar...")


if __name__ == "__main__":
    menu()
