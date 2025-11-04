# =========================================
# Ejercicio 2 - Clase Cliente
# =========================================


class Cliente:
    # << Constructores >>
    def __init__(self, numero_id: int, nombres: str, apellidos: str, email: str):
        self.__numero_id = numero_id
        self.__nombres = nombres
        self.__apellidos = apellidos
        self.__email = email

    # << Comandos >>
    def establecer_numero_id(self, numero_id: int):
        self.__numero_id = numero_id

    def establecer_nombres(self, nombres: str):
        self.__nombres = nombres

    def establecer_apellidos(self, apellidos: str):
        self.__apellidos = apellidos

    def establecer_email(self, email: str):
        self.__email = email

    # << Consultas >>
    def obtener_numero_id(self) -> int:
        return self.__numero_id

    def obtener_nombres(self) -> str:
        return self.__nombres

    def obtener_apellidos(self) -> str:
        return self.__apellidos

    def obtener_email(self) -> str:
        return self.__email

    # >> Ejercicio 5 - __eq__ <<
    def __eq__(self, other):
        if isinstance(other, Cliente):
            return self.__numero_id == other.__numero_id
        return False

    # >> Ejercicio 5 - __str__ <<
    def __str__(self):
        return (
            f"Cliente #{self.__numero_id} | "
            f"Nombre: {self.__nombres} {self.__apellidos} | "
            f"Email: {self.__email}"
        )
