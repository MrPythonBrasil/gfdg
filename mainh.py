pip install colorama

import os
from colorama import Fore, Back, Style, init

# Inicializa o colorama
init(autoreset=True)

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_titulo():
    print(Fore.YELLOW + Back.BLACK + Style.BRIGHT + "Calculadora Super Eficiente!")
    print(Fore.CYAN + "Escolha uma operação:")

def mostrar_opcoes():
    print(Fore.GREEN + "1. Adição (+)")
    print(Fore.GREEN + "2. Subtração (-)")
    print(Fore.GREEN + "3. Multiplicação (*)")
    print(Fore.GREEN + "4. Divisão (/)")
    print(Fore.RED + "5. Sair")

def realizar_calculo():
    while True:
        limpar_tela()
        mostrar_titulo()
        mostrar_opcoes()

        try:
            escolha = int(input(Fore.MAGENTA + "Digite o número da operação desejada: "))

            if escolha == 5:
                print(Fore.BLUE + "Saindo da calculadora. Até mais!")
                break

            if escolha < 1 or escolha > 5:
                print(Fore.RED + "Opção inválida! Tente novamente.")
                continue

            num1 = float(input(Fore.CYAN + "Digite o primeiro número: "))
            num2 = float(input(Fore.CYAN + "Digite o segundo número: "))

            if escolha == 1:
                resultado = num1 + num2
                print(Fore.GREEN + f"O resultado de {num1} + {num2} é: {resultado}")
            elif escolha == 2:
                resultado = num1 - num2
                print(Fore.GREEN + f"O resultado de {num1} - {num2} é: {resultado}")
            elif escolha == 3:
                resultado = num1 * num2
                print(Fore.GREEN + f"O resultado de {num1} * {num2} é: {resultado}")
            elif escolha == 4:
                if num2 == 0:
                    print(Fore.RED + "Erro! Divisão por zero.")
                else:
                    resultado = num1 / num2
                    print(Fore.GREEN + f"O resultado de {num1} / {num2} é: {resultado}")
        except ValueError:
            print(Fore.RED + "Entrada inválida! Por favor, digite números válidos.")
        
        input(Fore.YELLOW + "\nPressione Enter para continuar...")

if __name__ == "__main__":
    realizar_calculo()
