#Escreva um programa em Python que utiliza a biblioteca 
# datetime para exibir a data e hora atuais com a formatação 
# apresentada a seguir:

from datetime import datetime

data=datetime.now()

data_form = data.strftime("%d/%m/%Y %H:%M:%S")

print ("Data e hora atual:",data_form)