#2 - Dando continuidade à questão anterior, um outro bar permite a 
# entrada de grupos onde pelo menos uma pessoa é maior de idade 
# (ficando responsável pelas outras). Ajuste sua resposta da questão 
# anterior, ainda solicitando as idades de Juliana e Cris, mas ajustando 
# a expressão para esse novo cenário, 
# imprimindo True se puderem entrar no bar, e False caso contrário.

idade_1 = int(input ("Juliana digite sua idade: "))
idade_2 = int(input ("Cris digite sua idade: "))
print((idade_1>17)or(idade_2>17))