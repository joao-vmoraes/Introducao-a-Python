#perguntando o ano da pessoa
ano_pessoa = int(input('Bom dia! Aqui é do sistema militar, qual o seu ano de nascimento? '))
ano = 2025
idade = 2025 - ano_pessoa
if (idade == 18):
    alistamento = int(input('voce ja se alistou? digite 1 para sim, e 2 para nao: '))
    if alistamento == 1:
        print('Parabens amigao! voce é o novo almirante do exercito brasileiro')
    else:
        print('Você estava com 1 ano de atraso. Seu alistamento foi agentado!')
elif (idade == 17):
    alistamento = ('voce esta na idade de se alistar! você deseja se alistar? digite 1 para sim, e 2 para nao')
    if alistamento == 1:
        print('Seu alistamento foi agendado! tenha um otimo dia.')
    else:
        print('Você esta na idade para se alistar! tenha cuidado para nao passar desse prazo, até logo!')
elif (idade < 17):
    print('Calma jovem apenas com 17 anos que você estará na idade para se alistar! Te vejo daqui a {} anos.'.format(17 - idade))
else:
    alistamento = int(input('Você ja se alistou? digite 1 para sim, e 2 para nao: '))
    if alistamento == 1:
        print('Agora é so aguardar! tenha um otimo dia.')
    else:
        print('Que isso amigão, ta atrasado em {} anos, se cuida'.format(idade - 17))
print('se precisar falar comigo, estarei aqui!')

