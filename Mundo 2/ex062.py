
#--- Exercício 062 ---#

"""
Super Progressão Aritmética v3.0
"""
print('=' * 20)
print('Gerador de PA')
print('=' * 20)

p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
cont = 0
total = 0
mais = 10

while mais != 0:
    total += mais
    while cont < total:
        print(f'{p} -> ', end='')
        p += r
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos deseja mostrar: '))

print(f'Progressão finalizada com {total} termos')

