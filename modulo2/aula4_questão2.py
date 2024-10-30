# - Faça um programa para ler as dimensões de um terreno em inteiros
# (comprimento e largura), bem como o preço do metro quadrado da região 
#em ponto flutuante. Calcule o valor do terreno e imprima o resultado 
#como mostra o exemplo a seguir:O terreno possui 250m2 e custa R$512,490.50

comprimento = int(input ("Digite o comprimento do terreno: "))
largura = int(input ("Informe a largura do terreno: "))
preco_m2 = float(input ( "Informe o preço por m2: "))

area_m2 = comprimento * largura

preco_total = preco_m2 * area_m2

print (f"O terreno possui {area_m2} m2 e custa R$ {preco_total:,.2f}")