
#--- Exercício 069 ---#

"""
Análise de dados do grupo
"""

maior_18 = []
qtd_homem = []
qtd_mulher_menor_20 = []
while True:
    print("-"*20)
    print("CADASTRE UMA PESSOA")
    print("-"*20)

    idade = int(input("Idade: "))
    sexo = str(input("Sexo: [M/F] ")).upper().strip()

    if sexo == "M":
        qtd_homem.append(sexo)

    if idade > 18:
        maior_18.append(idade)

    if sexo == "F" and idade < 20:
        qtd_mulher_menor_20.append(sexo)

    print("-"*20)
    escolha = str(input("Deseja continuar? [S/N] ")).upper().strip()

    if escolha == "N":
        break

print("\n")
print(f"Total de pessoas maiores de 18: {len(maior_18)}")
print(f"Ao todo temos {len(qtd_homem)} homens cadastrados")
print(f"E temos {len(qtd_mulher_menor_20)} com menos de 20 anos")
