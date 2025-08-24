import datetime

def checar_voto(ano):
    atual = datetime.datetime.now().year
    idade = atual - ano
    if idade >= 18:
        return print(f"Com {idade} anos o voto é: OBRIGATÓRIO")
    elif idade >= 16:
        return print(f"Com {idade} anos o voto é: OPCIONAL")
    else:
        return print(f"Com {idade} anos o voto é: PROIBIDO")
    


ano = int(input("Digite o ano de seu nascimento: "))
checar_voto(ano)