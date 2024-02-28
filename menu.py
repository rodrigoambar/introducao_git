def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b != 0:
        return a / b
    else:
        print("Não se pode dividir por 0")



    

def menu():
        print("Selecione a operação:")
        print("1. Adição")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("0. Sair")
        while True:
            escolha = int(input("Escolha a operação desejada: "))
            if escolha != 0:
                num1 = float(input(" Digite o primeiro numero"))
                num2 = float(input(" Digite o primeiro numero"))
            if escolha == 1:
                print(f'Foi escolhido a soma de {num1} e {num2}, assim ficando {somar(num1, num2)}')
            elif escolha == 2:
                print(f'Foi escolhido a subtração de {num1} e {num2}, assim ficando {subtrair(num1, num2)}')
            elif escolha == 3:
                 print(f'Foi escolhido a multiplicação de {num1} e {num2}, assim ficando {multiplicar(num1, num2)}')
            elif escolha == 4:
                print(f'Foi escolhido a divisão de {num1} e {num2}, assim ficando {dividir(num1, num2)}')
            else:
                print("Saindo do menu")
                break

menu()


