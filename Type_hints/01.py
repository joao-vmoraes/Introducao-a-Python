# TIpos Primitivos

nome: str = 'lui'
x: int = 2026
y: float = 11.11
c: complex = 3 + 4j
is_valid: bool = True
data: bytes = b'a byte'

# Coleções
lista_numeros: list[int|str] = [1,2,3,'a']
tupla_dois_valores: tuple[str, int] = ("valor", 23)
tupla_varios:tuple[str,...] = ("a","b","c","...")
dicionario: dict[int | str,int | str] = {"Valor1": 'ola', "Valor 2" : 123}

#Outras coisas
nada: None = None
qualquer_coisa: object = 123
tipo: type = str