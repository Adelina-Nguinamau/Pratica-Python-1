larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
área = larg * alt
print('Sua parede tem a dimensão de {}x{} e a sua área é de {} metros quadrados'.format(larg, alt, área))
tinta = área / 2
print('Para pintar essa parede vo^ce precisará de {} de tinta'.format(tinta))
