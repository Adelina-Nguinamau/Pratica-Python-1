print('-=-'*20)
print('Analisador de Triângulos')
print('-=-'*20)
r1 = float(input('Primeiro segimento: '))
r2 = float(input('Segundo segimento: '))
r3 = float(input('Terceiro segimento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos acima podem formar triângulos!')
else:
    print('Os seguimentos acima não podem formar triângulos!')