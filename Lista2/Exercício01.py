'''
1. A Ficha do Aventureiro (Alinhamento e Preenchimento com f-strings) 
Crie um programa que leia o nome de um personagem de RPG, sua classe e seu nível. O programa deve exibir uma ficha resumida onde os textos fiquem alinhados à esquerda (ocupando 20 espaços preenchidos com pontos) e o nível fique alinhado à direita (ocupando 5 espaços). 
Exemplo de Entrada: 
Nome: Thrall 
Classe: Xamã 
Nível: 85 

Exemplo de Saída:
Nome................Thrall 
Classe..............Xamã 
Nível...................85
'''

# Entrada
nome = input("Nome: ")
classe = input("Classe: ")
nivel = int(input("Nível: "))

# Saída
print("{:.<20}{}".format("Nome", nome))
print("{:.<20}{}".format("Classe", classe))
print("{:.<20}{:>5}".format("Nível", nivel))