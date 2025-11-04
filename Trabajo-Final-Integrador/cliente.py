# =========================================
# Ejercicio 2 - generar la clase cliente.py
# =========================================


class Cliente:
    # Constructor
    def __init__(self, numeroId: int, nombres: str, apellidos: str, mail: str):
        self.__numeroId = numeroId
        self.__nombres = nombres
        self.__apellidos = apellidos
        self.__email = mail

    # --- Comandos (modificadores) ---
    def establecerNumeroId(self, numeroId: int):
        self.__numeroId = numeroId

    def establecerNombres(self, nombres: str):
        self.__nombres = nombres

    def establecerApellidos(self, apellidos: str):
        self.__apellidos = apellidos

    def establecerEmail(self, email: str):
        self.__email = email

    # --- Consultas (getters) ---
    def obtenerNumeroId(self) -> int:
        return self.__numeroId

    def obtenerNombres(self) -> str:
        return self.__nombres

    def obtenerApellidos(self) -> str:
        return self.__apellidos

    def obtenerEmail(self) -> str:
        return self.__email


    # Ejercicio 5 - implementacion __str__ y __eq__
    def __eq__(self, other):
        if isinstance(other, Cliente):
            return self.__numeroId == other.__numeroId
        return False

    def __str__(self):
        return (
            f"Cliente #{self.__numeroId} | "
            f"Nombre: {self.__nombres} {self.__apellidos} | "
            f"Email: {self.__email}"
        )