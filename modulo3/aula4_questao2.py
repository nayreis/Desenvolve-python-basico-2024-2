#Você está criando um sistema de classificação de filmes com base nas 
# avaliações dos usuários. Escreva um programa em Python que solicita ao 
# usuário para inserir a avaliação de um filme em uma escala de 1 a 5. 
# O programa deve imprimir uma mensagem correspondente à classificação 
# do filme:

#Se a avaliação for 5, imprima "Excelente!" Se a avaliação for 4, imprima "Muito Bom!"
#Se a avaliação for 3, imprima "Bom!"vSe a avaliação for 2, imprima "Regular."
#Se a avaliação for 1, imprima "Ruim."

avaliaçao = int (input( "Digite a avaliação do filme em uma escala de 1 a 5, onde 1 é ruim e 5 excelente: "))

if avaliaçao == 5:
    print ( " Excelente" )

if avaliaçao == 4:
    print ( " Muito Bom" )

if avaliaçao == 3:
    print ( " Bom" )

if avaliaçao == 2:
    print ( " Regular" )

if avaliaçao == 1:
    print ( " Ruim" )