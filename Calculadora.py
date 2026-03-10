class Calculadora:
    def __init__(self, marca="Básica"):
        self.marca = marca

    def sumar(self, a, b):
        return a + b

    def restar(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b == 0:
            return "Error: No se puede dividir por cero000000."
        return a / b

# --- Ejemplo de uso ---
mi_calculadora = Calculadora("Casio")

num1 = 10
num2 = 5

print(f"Calculadora {mi_calculadora.marca}")
print(f"Suma: {mi_calculadora.sumar(num1, num2)}")
print(f"Resta: {mi_calculadora.restar(num1, num2)}")
print(f"Multiplicación: {mi_calculadora.multiplicar(num1, num2)}")
print(f"División: {mi_calculadora.dividir(num1, num2)}")