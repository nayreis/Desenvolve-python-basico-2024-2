#Juliana e Cris querem entrar em um bar, mas só podem se ambos 
# forem maiores de idade (>17). Escreva um programa que solicite as 
# idades de Juliana e Cris e imprima True se ambas forem maiores de 17 anos, 
# indicando que podem entrar no bar, e False caso contrário.

idade_1 = int(input ("Juliana digite sua idade: "))
idade_2 = int(input ("Cris digite sua idade: "))
print((idade_1>17)and(idade_2>17))