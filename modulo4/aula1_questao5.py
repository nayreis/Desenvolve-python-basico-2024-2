n=int(input("Digite o número da quantidade dos respondentes: "))
aux=0
soma=0
while aux<n:
    idade=int(input("Digite a idade: "))
    aux+=1
    soma+=idade
media=soma/n
print("A soma das idades é: ", media)
