#5 - Solicite de um usuário seu gênero ("M" ou "F"), sua idade e seu 
# tempo de serviço (em anos) e escreva uma expressão que imprima True 
# se a pessoa já pode se aposentar, ou False caso contrário, de acordo 
# com as seguintes regras:
# A: Para mulheres, ter mais de 60 anos. Para homens, 65.
#B: Ou ter trabalhado pelo menos 30 anos
#C: Ou ter 60 anos  e trabalhado pelo menos 25.

genero = input("Digite o gênero (M ou F):")
idade = int(input("Digite a idade: "))
tempo_serv = int(input("Digite o tempo de serviço: "))

print((genero == "M" and idade >= 65) or (genero == "F" and idade >= 60) 
      or (tempo_serv >= 30)
      or (genero == "M" and idade >= 60 and tempo_serv>=25)   or 
      (genero == "F" and idade >= 60 and tempo_serv>=25) )