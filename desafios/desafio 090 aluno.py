aluno = {}

aluno["nome"] = input("Nome do aluno(a): ")
aluno["media"] = float(input(f"Media de {aluno["nome"]}: "))

if aluno["media"] >= 7:
    aluno["situacao"] = "Aprovado"
else:
    aluno["situacao"] = "Reprovado"

for k,v in aluno.items():
    print(f"{k} é {v}")