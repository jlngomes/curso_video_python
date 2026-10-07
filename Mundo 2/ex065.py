
#--- Exercício 065 ---#

"""
Maior e Menor valores
"""

escolha = "S"
cont = soma = 0

while escolha in "Ss":
    n = int(input("Digite um número: "))
    if cont == 0:
        maior = menor = n

    if n > maior:
        maior = n
    if n < menor:
        menor = n

    soma += n
    cont += 1

    escolha = str(input("Deseja continuar [S/N]: ")).upper().strip()

print(f"Você digitou {cont} números e a média foi {soma / cont}")
print(f"O maior valor foi {maior} e o menor foi {menor}")
