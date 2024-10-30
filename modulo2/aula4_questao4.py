#Você está desenvolvendo um programa para calcular o preço total de uma compra em uma loja online. O preço dos produtos é 
#calculado multiplicando a quantidade pelo preço unitário. Escreva um programa em Python que solicite do usuário o nome, o
#  preço unitário e a quantidade de 3 produtos comprados e imprima ao final o preço total da compra. Note no exemplo a seguir
#  que: Cada entrada de dados tem uma mensagem indicando o dado solicitado (mensagens em itálico, dado de entrada em negrito)
# A saída deve estar formatada exatamente como indicado (a string "Total: R$" e o preço com um separador de 
# milhar e duas casas decimais).

produto_1 = (input ("Digite o nome do produto 1: "))
preco_1 = float(input ("Digite o preço unitário do produto 1: "))
quantidade_1 = int(input ( "Digite a quantidade do produto 1: "))
valor_1 = preco_1*quantidade_1
produto_2 = (input ("Digite o nome do produto 2: "))
preco_2 = float(input ("Digite o preço unitário do produto 2: "))
quantidade_2 = int(input ( "Digite a quantidade do produto 2: "))
valor_2 = preco_2*quantidade_2
produto_3 = (input ("Digite o nome do produto 3: "))
preco_3 = float(input ("Digite o preço unitário do produto 3: "))
quantidade_3 = int(input ( "Digite a quantidade do produto 3: "))
valor_3 = preco_3*quantidade_3

valor_total = valor_1+valor_2+valor_3
print (f" O valor total é R$ {valor_total:,.2f}  ")

