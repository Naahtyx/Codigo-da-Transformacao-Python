'''
Comparando números com IF-ELIF-ELSE
Pedir dois números para o usuário 
O usuário irá escolher dois números
O programa irá comparar e falar qual é o maior e qual é o menor

''' 
print("\n--- Comparador de Números ---")

try:
    numero_a = int(input("Digite o primeiro número inteiro: "))
    numero_b = int(input("Digite o segundo número inteiro: "))

except ValueError:
    print("\nERRO: Por favor, digite apenas números inteiros válidos.")
    exit()

print("\n--- Resultado da Comparação ---")

if numero_a > numero_b:

    print(f"O número ({numero_a}) é o MAIOR.")

elif numero_b > numero_a:
    print(f"O número ({numero_b}) é o MAIOR.")

else:
    print("Os dois números são IGUAIS.")

print("\n-----------------------------------")