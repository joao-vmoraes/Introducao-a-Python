def analisador(*numeros , sit=False):
    aluno = dict()
    aluno["total"] = len(numeros)
    soma = 0
    contador = 0
    
    for i in numeros:
        if contador == 0:
            aluno["maior"] = i
            aluno["menor"] = i
        elif i > aluno["maior"]:
            aluno["maior"] = i
        elif i < aluno["menor"]:
            aluno["menor"] = i
        contador += 1
        soma += i

    aluno["media"] = soma / aluno["total"]

    if sit:
        if aluno["media"] >= 7:
            aluno["situacao"] = "Aprovado"
        elif aluno["media"] < 7:
            aluno["situacao"] = "Reprovado"

    return print(aluno)

aluno = analisador(5,7,3,9,9,10,5,7,8, sit=True)