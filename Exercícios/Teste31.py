velocidade = float(input('Qual a velociidade actual do carro? '))
# Condição simples apenas com if
if  velocidade > 80:
    print('Multado! Você excedeu o limite permitido que é 80km/h')
    multa = (velocidade-80)*7
    print('Você deve pagar uma multa de {:.2f}'.format(multa))
print('Tenha um bom dia e dirija com segurança!') # por este print estar colocado ao canto esquerdo ele sempre será executado, é uma regra do Python.

