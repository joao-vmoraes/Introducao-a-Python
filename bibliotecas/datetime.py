import datetime

#datetime.datetime.now().year  == retorna o valor do ano atual
#datetime.date(ano , mes , dia) == guarda esse tempo
#datetime.date.today() == guarda apenas o dia mes e ano do dia atual
#datetime.time(hora, minuto, segundo) == guarda esse tempo
#datetime.datetime(ano , mes , dia , hora , minuto , segundo, microsegundo)
#datetime.now() = pega todas as informações no momento em que ele foi chamado



#data = datetime.datetime(2025 , 8 , 27 )
#data.weekday() = segunda = 0 , terca = 1 ... domingo = 6
#nova_data = data.replace(month = 9) = muda apenas o mes mas em uma nova variavel


###
# 
# data = datetime(2025, 8 , 27)
# sete_dias = timedelta(days = 7)
# nova_data = data + sete_dias
# 
# ###

#agora = datetime.datetime.now()
#tempo = agora.timestamp()
#print(tempo) mostra a quantidade de segundos passados desde algum tempo predefinido pela propria library
#agora = datetime.datetime(2025, 08 , 27)
# mensagem = agora.strftime("Hoje é dia %d do mes %m do ano %Y")

# data_string = "27/08/2025"
# data = datetime.datetime.strptime(data_string , "%d/%m/%Y")
