'''
3. Ingresso VIP de Heavy Metal (Centralização de Strings) 
Desenvolva um programa que leia o nome de uma banda e a cidade do show. O programa deve gerar o layout de um ingresso na tela. O nome da banda deve ser transformado para letras maiúsculas (.upper()) e exibido centralizado em uma linha de 40 caracteres, preenchida com o símbolo de igual (=). 

Exemplo de Entrada: 
Banda: Iron Maiden 
Cidade: São Paulo 

Exemplo de Saída:
==============IRON MAIDEN=============== 
Local: São Paulo
Ticket: VIP - Acesso Liberado
========================================
'''
# Entrada
banda = input("Banda: ")
cidade = input("Cidade: ")

# Saída
print("{:=^40}".format(banda.upper()))
print("Local: {}".format(cidade))
print("Ticket: VIP - Acesso Liberado")
print("=" * 40)