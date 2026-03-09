'''
2. A Padaria (Casas Decimais e Operadores Aritméticos) 
Elabore um programa para ajudar no caixa de uma padaria. O programa deve solicitar o nome do cliente, o nome do doce comprado, a quantidade e o preço unitário. Calcule o valor total a pagar e exiba um mini-recibo. Os valores monetários devem obrigatoriamente aparecer com duas casas decimais e o nome do cliente deve ser exibido com a primeira letra maiúscula (usando o método .title() ou .capitalize()). 

Exemplo de Entrada: 
Cliente: jonin 
Doce: Croissant 
Quantidade: 3 
Preço Unitário: 5.5 

Exemplo de Saída:
--------- RECIBO --------- 
Cliente: Jonin 
Item: Croissant x3 
Total a pagar: R$ 16.50 
--------------------------
'''
# Entrada
cliente = input("Cliente: ")
doce = input("Doce: ")
quantidade = int(input("Quantidade: "))
preco = float(input("Preço Unitário: "))

# Processo
total = quantidade * preco

# Saída
print("--------- RECIBO ---------")
print("Cliente: {}".format(cliente.title()))
print("Item: {} x{}".format(doce, quantidade))
print("Total a pagar: R$ {:.2f}".format(total))
print("--------------------------")