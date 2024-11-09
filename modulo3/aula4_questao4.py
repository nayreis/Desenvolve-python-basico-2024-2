#Você está implementando um sistema de entrega expressa e precisa 
# calcular o valor do frete com base na distância e no peso do pacote. 
# Escreva um código que solicita a distância da entrega em quilômetros 
# e o peso do pacote em quilogramas. O programa deve calcular e imprimir 
# o valor do frete de acordo com as seguintes regras:

#Distância até 100 km: R$1 por kg.
#Distância entre 101 e 300 km: R$1.50 por kg.
#Distância acima de 300 km: R$2 por kg.
#Acrescente uma taxa de R$10 para pacotes com peso superior a 10 kg

distancia = int ( input("Digite a distância em Km: "))
peso = int ( input("Digite o peso da mercadoria em Kg: "))


if distancia <= 100:
    entrega = distancia*peso*1

if distancia >100 and distancia<=300:
    entrega = distancia*peso*1.5
    
if distancia >300:
    entrega = distancia*peso*2

if peso>10:
    entrega+=10

print ( "o Valor da entrega sera: ", entrega)



