nome = 'Guanabara'
cores = {'limpa': '\033[m', # lista de corres para usar no programa
          'azul':'\033[34m',
            'amarelo': '\033[33m',
              'pretobranco': '\033[7; 30m'}
print('Olá, muito prazer em te conhecer, {}{}{}!!'.format(cores['amarelo'], nome , cores['limpa']))



"""
Ex.3:
nome = 'Guanabara'
print('Olá, muito prazer em te conhecer, {}{}{}!!'.format('\033[4;34m', nome ,'\033[m'))


Ex.2:
a = 5
b = 8
print('Os valores são \033[32m{} e \033[35m{}'.format(a ,b))


Ex.1:
print('\033[7;34;47mOlá mundo!\033[m') #O \033[m no final serve para fazer com que obackground fique no limite da frase msotarada na tela"""