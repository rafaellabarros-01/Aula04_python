'''
3. Desenvolva um programa para calcular e escrever a área e o perímetro de um retângulo.
Exemplo: 
Base= 5
Altura = 4
Área = 20
Perímetro = 18
'''

#Entrada
Base = float(input("informe a base: "))
Altura = float(input("informe a altura: "))

#processo
Área = Base * Altura
Perímetro = (Base * 2) + (Altura * 2)

#Saída
print("Área do retângulo:", Área)
print("Perímetro do retângulo:", Perímetro)