
def factorial(numero):
    """
    Calcula el factorial de un número entero no negativo.

    Args:
        numero (int): Número cuyo factorial se desea calcular.

    Returns:
        int: Resultado del factorial.

    Raises:
        TypeError: Si la entrada no es un entero.
        ValueError: Si el número es negativo.
    """
    if isinstance(numero, bool) or not isinstance(numero, int):
        raise TypeError("El número debe ser un entero.")

    if numero < 0:
        raise ValueError("El número no puede ser negativo.")

    resultado = 1

    for i in range(1, numero + 1):
        resultado *= i

    return resultado

