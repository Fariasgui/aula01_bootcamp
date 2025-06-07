# Primeira Aula

Nesta aula, aprendemos o básico da estrutura de python e utilizando do conhecimento fornecido para criar uma calculadora de bônus para os funcionário de uma empresa.

## Calculadora

Ela consiste em 5 passos:

1. Solicitamos o nome do funcionário através de:

`nome = str(input("Digite seu nome: "))`

2. Pedimos o salário:

`salario = float(input("Digite seu salário: "))`

3. Pedimos a porcentagem de bônus aplicada:

`porc_bonus = float(input("Qual a porcentagem do bônus: "))`

4. Calculamos o bônus:

`kpi_bonus = 1000 + salario * porc_bonus`

5. Mostamos o resultado ao funcionário:

`print(f"Olá {nome}, o seu bônus em 2024 foi de {kpi_bonus}")`