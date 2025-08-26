distâcia = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}km.'.format(distâcia))
preço = distâcia * 0.50 if distâcia <= 200 else distâcia * 0.45
print('E o preço da sua passagem será de {:.2f}R$'.format(preço))



""" Outra forma de resolução
distâcia = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}km.'.format(distâcia))
if distâcia <= 200:
    preço = distâcia * 0.50
else:
    preço = distâcia * 0.45
print('E o preço da sua passagem será de {:.2f}R$'.format(preço))"""