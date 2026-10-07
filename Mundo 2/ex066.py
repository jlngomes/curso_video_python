
#--- Exercício 066 ---#

"""
Vários números com flag
"""

soma = cont = n = 0
while True:
    n = int(input("Digite um valor (999 para parar): "))

    if n == 999:
        break

    cont += 1
    soma += n

print(f"Soma dos {cont} valores foi {soma}")
