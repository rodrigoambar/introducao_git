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


def calculadora():
    while True:
        menu()
        escolha = int(input("Escolha a operação desejada: "))
        if escolha != 0:
            num1 = float(input(" Digite o primeiro numero"))
            num2 = float(input(" Digite o primeiro numero"))
            if escolha == 1:
                print(f'Foi escolhido a soma de {num1} e {num2}, assim ficando {somar(num1, num2)}')