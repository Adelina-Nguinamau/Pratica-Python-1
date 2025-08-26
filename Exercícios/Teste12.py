valor_reais = float(input('Digite quanto tem na carteira: '))
valor_dolar = valor_reais / 3.27
print('Com esse valor em R$ {:.2f} você pode comparar US$ {:.2f}.'.format(valor_reais, valor_dolar))