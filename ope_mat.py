# Função para validar se uma entrada é um número inteiro
def input_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Por favor, digite um número válido.")

num1 = input_float("Digite o primeiro número: ")
num2 = input_float("Digite o segundo número: ")

resultado = num1 + num2

print(f"Resultado da adição: {num1} + {num2} = {resultado}")
