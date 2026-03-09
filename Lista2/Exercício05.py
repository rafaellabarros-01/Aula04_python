'''
5. Calculadora de Dano Crítico (Matemática e Formatação Mista) 
Crie um programa que simule o cálculo de dano de um ataque em um jogo. Leia o nome do ataque, o valor do dano base e o multiplicador de acerto crítico (um número decimal). Calcule o dano total (dano base * multiplicador). Exiba na tela uma mensagem de combate emocionante, formatando o dano total com zero casas decimais (arredondamento visual no f-string) e destacando o nome do ataque em maiúsculas. 

Exemplo de Entrada: 
Ataque: corte ninja 
Dano base: 150 
Multiplicador: 1.5 

Exemplo de Saída:
O ataque CORTE NINJA foi um sucesso! 
Dano causado: 225 pontos!

'''

# Entrada
ataque = input("Ataque: ")
dano_base = float(input("Dano base: "))
multiplicador = float(input("Multiplicador: "))

# Processo
dano_total = dano_base * multiplicador

# Saída
print("O ataque {} foi um sucesso!".format(ataque.upper()))
print("Dano causado: {:.0f} pontos!".format(dano_total))