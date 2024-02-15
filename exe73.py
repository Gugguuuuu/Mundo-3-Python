times = ('Athletico-PR','Athletico Goainiense','Atlético-MG','Bahia',
         'Botafogo','Corinthians','Criciúma','Cruzeiro',
         'Cuiabá','Flamengo','Fluminense','Fortaleza',
         'Grêmio','Internacional','Juventude','Palmeiras','Red Bull Bragantino',
         'São Paulo','Vasco da Gama','Vitória'

)
print(f'\033[1;32mtimes em ordem alfabetica :\033[m \033[1;34m{sorted(times)}\033[m')
print(f'\n\033[1;31m5 primeiros times:\033[m \033[1;33m{times[:5]}\033[m')
print(f'\n\033[1;35m4 ultimos times\033[m \033[1;7;37;40m{times[16:]}\033[m')
print("\n\033[1mCOLOCAÇÃO DO BRASILEIRAO\033[m\n")

d = 0
time = str(input('Digite um time e você vera a sua colocação : ')).strip().title()
while time not in times:
    time = str(input('Este time não esta no BRASILEIRÃO SERIE A\nDigite um time e você vera a sua colocação : ')).strip().title()
for t, c in enumerate(times):
    print(f'\033[1;33m{t+1}ª\033[m \033[1m{c}\033[m')
for i in times:
    d += 1
    if i == time:
        print(f'O {time} está na posição {d}ª')
