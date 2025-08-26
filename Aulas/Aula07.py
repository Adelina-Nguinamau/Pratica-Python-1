n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, o produto é {}, e a divisão é {:.3f}'.format(s, m, d), end=' ') # {:.3f} Diz o numero de casas decimais ou flutuantes e o , end=' ' faz com que não haja quebra de linha e o \n serve para quebrar a linha
print('Divisão inteira {} e potência {}'.format(di, e))