
#--- Exercício 070 ---#

"""
Estatísticas em produtos
"""

soma = 0
maior_1000 = []
cont = 0
menor = 0
produto_menor_valor = ''
while True:
    print("-"*20)
    print("Loja do Jean")
    print("-" * 20)

    produto = str(input("Nome do produto: "))
    valor = float(input("Preço: R$"))
    cont += 1

    soma += valor

    if valor > 1000:
        maior_1000.append(valor)

    if cont == 1:
        produto_menor_valor = produto
        menor = valor
    else:
        if valor < menor:
            produto_menor_valor = produto
            menor = valor

    print("-" * 20)
    escolha = str(input("Deseja continuar? [S/N] ")).upper().strip()

    if escolha == "N":
        break

print(f"O total da compra for de {soma:.2f}")
print(f"Temos {len(maior_1000)} produtos custando mais de R$1000.00")
print(f"O produto mais barato foi {produto_menor_valor} que custa R${menor:.2f}")
