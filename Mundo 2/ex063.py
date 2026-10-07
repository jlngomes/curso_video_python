
#--- Exercício 063 ---#

"""
Sequência de Fibonacci v1.0
"""

termos = int(input("Quantos termos você quer mostrar: "))
cont = 3
f1 = 0
f2 = 1
print(f"{f1} -> {f2}", end="")
while cont <= termos:
    f3 = f1 + f2
    print(f" -> {f3}", end="")
    f1 = f2
    f2 = f3

    cont += 1

print("-> FIM")