import moeda

n = 80

print(f"O dobro de {n} é {moeda.dobrar(n)}")
print(f"A metade de {n} é {moeda.metade(n)}")
print(f"Um aumento de 17% em {n} é {moeda.aumento(n,17)}")
print(f"Um desconto de 17% em {n} é {moeda.desconto(n,17):.2f}")