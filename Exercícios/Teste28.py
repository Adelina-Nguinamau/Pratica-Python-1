frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1)) # O +1 faz com que ao invés de aparecer a posição na prespectiva do computador que é 0 pareça na nossa que é 1
print('A última letra A apareceu na posição {}'.format(frase.rfind('A')+1)) # o rfind inicada a posição do último A ou seja o A a direita por isso o rfinda (r de right)
