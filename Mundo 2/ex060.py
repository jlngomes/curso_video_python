
#--- Exercício 060 ---#
"""
Cálculo do Fatorial
"""

def fatorial(n: int) -> int:
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)

valor = int(input("Digite um valor: "))
print(f"\nO fatorial de {valor} é {fatorial(valor)}")
