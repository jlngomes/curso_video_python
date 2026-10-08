
#--- Exercício 071 ---#

"""
Simulador de Caixa Eletrônico
"""

print("="*20)
print("BANCO CEV")
print("="*20)

valor = float(input("Que valor você quer sacar? "))

total = valor
cont_50 = cont_20 = cont_10 = cont_5 = cont_1 = 0
while True:
    if (total - 50) > 0:
        total -= 50
        cont_50 += 1
    elif (total - 20) > 0:
        total -= 20
        cont_20 += 1
    elif (total - 10) > 0:
        total -= 10
        cont_10 += 1
    else:
        total -= 1
        cont_1 += 1

    if total == 0:
        if cont_50:
            print(f"Total de {cont_50} cédulas de 50$")
        if cont_20:
            print(f"Total de {cont_20} cédulas de 20$")
        if cont_10:
            print(f"Total de {cont_10} cédulas de 10$")
        if cont_1:
            print(f"Total de {cont_1} cédulas de 1$")
        break

print("="*20)
print("Volte sempre ao BANCO CEV! Tenha um bom dia!")