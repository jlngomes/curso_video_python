
#--- Exercício 061 ---#

"""
Progressão Aritmética v2.0
"""

print('=' * 20)
print('10 TERMOS DE UMA PA')
print('=' * 20)

p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
cont = 0

while cont < 10:
    print(f'{p} -> ', end='')
    p += r
    cont += 1

print('Fim')
