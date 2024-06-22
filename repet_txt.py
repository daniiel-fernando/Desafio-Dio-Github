# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.
def input_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Por favor, digite um número inteiro válido.")

input_string = input("Digite uma string: ")
repetitions = input_int("Digite um número inteiro para repetir a string: ")

result_string = input_string * repetitions

print("String repetida:", result_string)
