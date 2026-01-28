class MeuError(Exception):
    ...

class OutroError(Exception):
    ...

def levantar():
    exception_ = MeuError("a", "b")
    exception_.add_note("Voce errou na passagem dos parametros")
    raise exception_

try:
    levantar()
except MeuError as error:
    print(error)
    exception_ = OutroError("cobra", "calango")
    exception_.add_note("Voce errou a tipagem")
    print(exception_.__notes__)
    print(error.__notes__)
    raise exception_ from error