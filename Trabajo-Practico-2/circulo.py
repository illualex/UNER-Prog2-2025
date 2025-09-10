# =========================================
# Ejercicio 5
# =========================================
class Circulo:
    PI = 3.14159

    def __init__(self, radio: float):
        self.radio = radio

    def establecerRadio(self, radio: float):
        self.radio = radio

    def obtenerRadio(self) -> float:
        return self.radio

    def obtenerDiametro(self) -> float:
        return self.radio * 2

    def obtenerArea(self) -> float:
        return Circulo.PI * (self.radio**2)

    def obtenerPerimetro(self) -> float:
        return 2 * Circulo.PI * self.radio
