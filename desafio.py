#Calculadora de Bônus
print("Olá, bem vindo ao cálculo de bônus 2024")
nome = str(input("Digite seu nome: "))
salario = float(input("Digite seu salário: "))
porc_bonus = float(input("Qual a porcentagem do bônus: "))
kpi_bonus = 1000 + salario * porc_bonus
print(f"Olá {nome}, o seu bônus em 2024 foi de {kpi_bonus}")