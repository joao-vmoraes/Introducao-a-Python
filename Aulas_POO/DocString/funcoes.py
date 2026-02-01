"""Este é um modulo de exemplo

sobre docstrings de funcoes"""

variavel_1 = 1

def soma(x: int | float, y: int | float ) -> int |float:
    """
    Docstring para soma
    
    :param x: Numero 1
    :type x: int | float
    :param y: Numero 2
    :type y: int | float
    :return: A soma entre numero 1 e numero 2
    :rtype: int | float
    """
    return x + y

variavel_2 = 2