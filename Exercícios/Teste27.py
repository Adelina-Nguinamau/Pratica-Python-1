nome = str(input('Qual é o seu nome?  ')).strip()
print('Seu nome tem Silva? {}'.format('silva' in nome.lower())) # usamos o operador in para verificar se dentro do nome há o silva