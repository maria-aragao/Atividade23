# Crie um programa que receba um número do usuário e exiba a tabuada desse número 

número = int(input("Digite um número para ver sua tabuada: "))

print(f"Tabuada de {número}:")
for i in range(1, 11):
    resultado = número * i
    print(f"{número} * {i} = {resultado}")