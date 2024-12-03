#Escreva um programa em Python que utiliza a biblioteca random 
# para gerar um número aleatório entre 1 e 10 e peça ao usuário 
# para adivinhar o número. Forneça feedback se o palpite é muito 
# alto, muito baixo ou correto. Interrompa a execução 
# somente quando o usuário acertar o palpite.

import random
num_aleat= random.randint(1,10)

while True:
   n = int( input("Vamos testar sua sorte, digite um número de 1 a 10: "))

   if n==num_aleat: 
      print("Acertou")
      break
      
   if n>num_aleat: 
     print ("Muito alto, tente novamente!")

   if n<num_aleat: 
     print ("Muito baixo, tente novamente!")


