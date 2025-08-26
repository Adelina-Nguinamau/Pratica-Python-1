n = str(input('Digite o seu nome completo: ')).strip()
nome = n.split()
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1])) # O len aqui está a medir o tamanho da frase para depois o -1 fazer com que o último nome apareça na posição da nossa prespectiva e não na o computador.
