dias = int(input('Digite quantos dias o carro foi alugado: '))
km= float(input('Digite quantos quilômetros foram rodados: '))
num_dias = dias*60
km_percorrido= km*0.15
preco_total = num_dias + km_percorrido
print('O total a pagar será {} R$'.format(preco_total))