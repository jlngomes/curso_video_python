
#--- Exercício 059 ---#

"""
Criando um Menu de Opções
"""
import time

menu = """
=======================
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Qual é a sua opção: """

def show_maior(a: int, b: int) -> None:
    if a > b:
        print(f"O maior é o {a}")
    else:
        print(f"O maior é o {b}")

valor1 = int(input('Primeiro valor: '))
valor2 = int(input('Segundo valor: '))

while True:
    try:
        opcao = int(input(menu))
    except ValueError:
        opcao = 0
        print("Digite apenas números inteiros!!")

    match opcao:
        case 0:
            continue
        case 1:
            print(f"A soma entre {valor1} e {valor2} = {valor1 + valor2}")
        case 2:
            print(f"A Multiplicação entre {valor1} e {valor2} = {valor1 * valor2}")
        case 3:
            show_maior(a=valor1, b=valor2)
        case 4:
            valor1 = int(input('Primeiro valor: '))
            valor2 = int(input('Segundo valor: '))
        case 5:
            print("Obrigado por jogar, volte sempre!")
            break
        case _:
            print("Opção invalida!")

    time.sleep(1)
