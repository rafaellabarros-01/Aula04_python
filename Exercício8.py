'''
Fazer um programa que dado um valor inteiro m calcule o menor número de notas de Real em que este número pode ser decomposto. 
Lembre-se que as notas existentes são 1, 2, 5, 10, 20, 50 e 100.
A Saída do programa deve ser o valor da entrada seguido de uma lista de notas correspondentes. 
Exemplo:
Valor R$ 1.488,00
R$ 100,00 -- 14 -- R$ 1.400,00
R$ 50,00 -- 1 -- R$ 50,00
R$ 20,00 -- 1 -- R$ 20,00
R$ 10,00 -- 1 -- R$ 10,00
R$ 5,00 -- 1 -- R$ 5,00
R$ 2,00 -- 1 -- R$ 2,00
R$ 1,00 -- 1 -- R$ 1,00
Total: R$ 1.451,00
Qtd Notas: 20

'''

# Entrada 
valor = int(input("Valor de saque: "))

# Quantidade de notas
notas_100 = valor // 100
notas_50 = (valor % 100) // 50
notas_20 = ((valor % 100) % 50) // 20
notas_10 = (((valor % 100) % 50)%20) // 10
notas_05 = ((((valor % 100) % 50)%20)%10) // 5
notas_02 = (((((valor % 100) % 50)%20)%10)%5) // 2
notas_01 = ((((((valor % 100) % 50)%20)%10)%5)%2) // 1


# Saída
print ("Valor: R$", valor)
print ("R$ 100.00 --", "{:02}".format(notas_100), "-- R${:8.2f}".format(notas_100 * 100))
print ("R$ 50.00 --", "{:02}".format(notas_50), "-- R${:8.2f}".format(notas_50 * 50))
print ("R$ 20.00 --", "{:02}".format(notas_20), "-- R${:8.2f}".format(notas_20 * 20))
print ("R$ 10.00 --", "{:02}".format(notas_10), "-- R${:8.2f}".format(notas_10 * 10))
print ("R$ 5.00 --", "{:02}".format(notas_05), "-- R${:8.2f}".format(notas_05 * 5))
print ("R$ 2.00 --", "{:02}".format(notas_02), "-- R${:8.2f}".format(notas_02 * 2))
print ("R$ 1.00 --", "{:02}".format(notas_01), "-- R${:8.2f}".format(notas_01 * 1))