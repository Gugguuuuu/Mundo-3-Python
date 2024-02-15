# EXERCICIO 72
numeros = ('zero','um','dois','três','quatro',
           'cinco','seis','sete','oito',
           'nove','dez','onze','doze',
           'treze','catorze','quinze','dezesseis',
           'dezessete','dezoito','dezenove','vinte')
n = int(input('Digite um numero : '))
while n < 0 or n > 20:
    n = int(input('\033[1;31mDIGITE  UM NUMERO VALÍDO\033[m\nDigite um numero : '))
print(f'Você digitou o numero \033[1;34m{numeros[n]}\033[m')