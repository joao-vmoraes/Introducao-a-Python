class Numero:
    """ Essa classe e um exemplo de um numero 

    use com sabedoria!
    """

    def __init__(self, x: int|float):
        """
        Docstring para __init__
        
        :param self: Descrição
        :param x: Descrição
        :type x: int | float
        """
        self.x = x

    def soma(self, y: int | float) -> int|float:
        """
        Docstring para soma
        
        :param self: numero 1
        :param y: numero 2
        :type y: int | float
        :return: numero 3
        :rtype: int | float
        """

        return self.x + y
