
#--- Exercício 064 ---#

"""
Tratando vários valores v1.0
"""

n = 0
cont = 0
soma = 0

while n != 999:
    n = int(input("Digite um número [999 para encerrar]: "))

    if n != 999:
        soma += n
        cont += 1

print(f"Você digitou {cont} e a soma entre ele é {soma}")
