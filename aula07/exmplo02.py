previsoes = ['Ensolarado', 'Nublado', 'Chuvoso', 'Tempestade', 'Ensolarado']
print(previsoes)

PREVISAO_FELIZ = 'Ensolarado'
PREVISAO_TRISTE = 'Tempestade'

for p in previsoes:
    print(p)

    if p == PREVISAO_FELIZ:
        print('Aproveite e passeie!')
    elif p == PREVISAO_TRISTE:
        print('Não saia de casa!')
    else:
        print('Não esqueça o guarda chuva')