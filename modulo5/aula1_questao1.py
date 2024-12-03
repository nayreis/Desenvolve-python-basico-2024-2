#desenvolva um programa em Python que peça ao usuário para inserir 
# dois números decimais e calcule a diferença absoluta entre esses 
# dois números. Utilize a função nativa abs para garantir que o resultado 
# seja sempre positivo e round para arredondar o resultado para 
# duas casas decimais.


num_1 = float (input("Digite o número: "))
num_2 = float ( input ("Digite o segundo número"))
   
diferença= abs(num_2-num_1)
arrend = round (diferença,2)
print (f"A diferença é: {arrend}")
