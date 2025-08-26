salário = float(input('Qual é o salário do funcionário? '))
if salário <= 1250:
    novo = salário + (salário * 15 / 100)
else:
    novo = salário + (salário * 10 / 100)
print('O novo salário será {:.2f}R$'.format(novo))