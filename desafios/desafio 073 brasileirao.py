times_brasileirao_2021 = (
    "Atlético-MG", "Flamengo", "Palmeiras", "Fortaleza", "Corinthians",
    "Bragantino", "Fluminense", "América-MG", "Atlético-GO", "Santos",
    "Ceará", "Internacional", "São Paulo", "Athletico-PR", "Cuiabá",
    "Juventude", "Grêmio", "Bahia", "Sport", "Chapecoense"
)

print(f'os primeiros 5 colocados foram : ', end='')
for primeiros_colocados in times_brasileirao_2021[0:5]:
    print(primeiros_colocados , end=', ')

print(f'\nOs 4 ultimos foram: ')
for ultimos in times_brasileirao_2021[-4:]:
    print(ultimos , end=', ')

print('=-' *10)
print(f'A lista em ordem alfabética fica: {sorted(times_brasileirao_2021)}')
print('=-' *10)

print(f'O sport ficou na posição: {times_brasileirao_2021.index('Sport')}')