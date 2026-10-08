
#--- Exercício 068 ---#

"""
Jogo do Par ou Ímpar
"""

from random import randint

print("VAMOS JOGAR PAR NO ÍMPAR")
while True:
    n = int(input("Digite um valor: "))
    escolha_humana = str(input("Par ou Ímpar [P/I]:")).upper().strip()
    escolha_computador = randint(1, 10)

    soma = escolha_computador + n
    if soma % 2 == 0 and escolha_humana == "P":
        print(f"Você jogou {n} e o computador {escolha_computador}. total deu {soma} DEU PAR")
        print("\nVocê venceu!")
        continue
    if soma % 2 == 1 and escolha_humana == "I":
        print(f"Você jogou {n} e o computador {escolha_computador}. total deu {soma} DEU ÍMPAR")
        print("\nVocê venceu!")
        continue

    tentativa = "IMPAR" if not soma % 2 == 0 else "PAR"
    print(f"Você jogou {n} e o computador {escolha_computador}. total deu {soma} DEU {tentativa}")
    print("Você perdeu")
    break
