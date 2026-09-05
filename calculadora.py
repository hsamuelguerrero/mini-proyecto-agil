"""Calculadora básica para simulación ágil."""


def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b


if __name__ == "__main__":
    print("Suma 5 + 3:", sumar(5, 3))
    print("Resta 5 - 3:", restar(5, 3))
    print("Multiplicación 4 * 2:", multiplicar(4, 2))
    print("División 10 / 2:", dividir(10, 2))
