import datetime
ano_atual = int(datetime.datetime.now().year)

pessoa = dict()

pessoa["nome"] = input("Qual o seu nome: ")
ano_nasc = int(input("Qual o ano que voce nasceu: "))
pessoa["idade"] = ano_atual - ano_nasc
pessoa["carteira"] = int(input("Carteira de Trabalho (0 se nao tiver): "))

if pessoa["carteira"] != 0:
    pessoa["contratacao"] = int(input("Ano de contratacao:  "))
    pessoa["aposentadoria"] = pessoa["contratacao"] + 35

print("=" * 20)
for k,v in pessoa.items():
    print(f"{k} tem valor {v}")