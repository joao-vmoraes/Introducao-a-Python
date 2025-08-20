import random
from operator import itemgetter
import time

jogadores = {
    "jogador1" : random.randint(1,6) , 
    "jogador2" : random.randint(1,6) , 
    "jogador3" : random.randint(1,6) , 
    "jogador4" : random.randint(1,6) 
    }

for k,v in jogadores.items():
    print(f"{k} tirou : {v} no dado")

ranking = ()
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse = True) #operator.itemgatter(1) vai receber o segundo valor dos itens que no caso é o valor(resultado do dado). E o sorted vai ordenar de forma crescente usando o valor(valor do dado) como parametro de ordem crescente.


for i in range(len(ranking)):
    print(f"{i + 1}° foi o {ranking[i][0]} tirando {ranking[i][1]} no dado !")