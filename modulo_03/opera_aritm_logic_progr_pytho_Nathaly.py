'''
OPERADORES ARITMÉTICOS
Este programa demonstra as 5 operações básicas com 2 números.
Peça ao usuario para digitar 2 números inteiros e mostre:
- A soma
- A diferença (subtração)
- A multiplicação
- A divisão
- O módulo (resto da divisão)

'''

try:
    numero1 = int(input("Digite o primeiro número: "))
    numero2 = int(input("Digite o segundo número: "))
except ValueError:
    print("\nERRO: Por favor, digite apenas números inteiros.")
   
    exit() 

print("\n--- Resultados das Operações ---")


soma = numero1 + numero2
print(f"1. SOMA: {numero1} + {numero2} = {soma}")

diferenca = numero1 - numero2
print(f"2. SUBTRAÇÃO: {numero1} - {numero2} = {diferenca}")


multiplicacao = numero1 * numero2
print(f"3. MULTIPLICAÇÃO: {numero1} * {numero2} = {multiplicacao}")


divisao = numero1 / numero2
print(f"4. DIVISÃO: {numero1} / {numero2} = {divisao}")

resto_divisao = numero1 % numero2
print(f"5. MÓDULO (Resto): {numero1} % {numero2} = {resto_divisao}")

print("\n---------------------------------")