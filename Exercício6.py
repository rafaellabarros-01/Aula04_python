'''
Crie um programa que leia dois valores para as variáveis A e B, que efetue a troca dos valores de forma que a variável A passe a ter o valor da variável B e que a variável B passe a ter o valor da variável A. Apresente os valores trocados. 
Exemplo:
A=5
B=10
INVERTENDO
A=10
B=5
'''

# Entrada 
valor_a = int(input('Informe o valor de a: '))
valor_b = int(input('Informe o valor de b: '))
print("")
print("")
print("Exercício6.py")

# Saída
print("Valor de A:", valor_a)
print("Valor de B:", valor_b)

# Processamento 
temp = valor_a #Armazena temporariamente valor de a
valor_a = valor_b
valor_b = temp

# Saída 2
print("")
print("Inversão:")
print("")
print("Valor de A:", valor_a)
print("Valor de B:", valor_b)
