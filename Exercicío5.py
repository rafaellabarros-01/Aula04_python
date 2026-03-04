'''
5. Codifique um programa que leia um número inteiro qualquer e imprima o seu sucessor e seu antecessor. A seguir, uma ilustração da entrada e da saída de uma execução do programa.
Exemplo:
valor = 7
antecessor = 6
sucessor = 8
'''

# Entrada 
numero = int(input('Informe um número: '))

# Processamento 
print ( "Número selecionado:", numero )
print("Antecessor =", numero - 1)
print("Sucessor =", numero + 1)