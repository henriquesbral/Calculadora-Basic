# REALIZANDO AS OPERAÇÕES

"""
Desenvolvido por Carlos Henrique Da Silva Sobral
20/07/2022
"""

print("\n\n\n Bem vindo a calculadora !")
print("\n Lista de operações: \n"
      "Adição = +"
      "\nSubtração = -"
      "\nDivisão = /"
      "\nMultiplicação = *\n")


def soma():
    num1 = float(input("Escreva o primeiro número: "))
    num2 = float(input("Escreva o segundo número: "))
    soma = num1 + num2
    return soma

def sub():
    num1 = float(input("Escreva o primeiro número: "))
    num2 = float(input("Escreva o segundo número: "))
    sub = num1 - num2
    return sub

def div():
    num1 = float(input("Escreva o primeiro número: "))
    num2 = float(input("Escreva o segundo número: "))
    div = num1 / num2
    return div

def mult():
    num1 = float(input("Escreva o primeiro número: "))
    num2 = float(input("Escreva o segundo número: "))
    mult = num1 * num2
    return mult

while True:
    Pergunta = str(input("Digite o sinal da operação ou 0 para sair: "))

    if Pergunta == "+":
        print("O resultado é: ", soma())
    elif Pergunta == "-":
        print("O resultado é: ", sub())
    elif Pergunta == "/":
        print("O resultado é: ", div())
    elif Pergunta == "*":
        print("O resultado é: ", mult())
    else:
        print("Obrigado !")
        break