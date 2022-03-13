
#1. Construa um programa que apresente na tela os 10 primeiros números naturais, em Ordem:

for n in range(0,11):
    print(n)

#2. Construa um programa que leia as notas de um aluno em cada questão, de uma prova de 10 questões.
# Se for digitada a nota zero para uma questão, o sistema deverá parar imediatamente, informando a mensagem "Não aprovado".

nota = int(input("Digite a nota da sua questão: "))
while nota > 0:
        print(f"Sua nota para essa questão é {nota}: ")
        nota = int(input("Digite a nota da sua questão: "))
else:
        print("Não Aprovado")

#3  Construa um programa que leia um valor do usuário e apresente em seguida a soma de todos os números inteiros de 1 até o valor informado.

valor = int (input("Digite um número: "))
soma = 0

for i in range (1, valor+1):
    soma = soma + i
print(f"O valor da soma é {soma}: ")



# 4 Construa um programa que apresente a tabuada de determinado valor informado.

valor = int(input("Digite um número: "))
print(f"Os valores para a tabuada de {valor} são: ")
for multiplicador in range(0,11):
    print(valor, "X", multiplicador, "=", (valor * multiplicador))

#5 Construa um programa que leia valores digitados pelo usuário e informe se o valor é par ou é impar. O programa deverá continuar solicitando valores ao usuário até que este digite o valor "0", que irá encerrar o programa.

valor = int(input("Digite um número: "))
resto = valor % 2

while valor == 0:
    print(f"O número {valor} é inválido, por favor digite outro.")
    int(input("Digite o número novamente:"))
    break
if resto == 0:
    print(f"O número {valor} é: Par")
else:
    print(f"O número {valor} é: Impar")

#______________________________________________

valor = 1

while (valor != 0):
    valor = int(input("Digite um número: "))
    resto = valor % 2

    if (resto == 0):
        print(f"O número {valor} é PAR")
    else:
        print(f"O número {valor} é IMPAR")

print("Fim do Código!")

#6 Um sistema de uma fábrica registra o peso de determinados produtos inseridos, sendo
#considerados inválidos pesos registrados abaixo de 100 ou acima de 900 (gramas).
#Construa um programa que solicite os pesos a serem digitados pelo usuário e conte
#quantos valores inválidos foram informados. O programa deverá encerrar ao ser digitado o
#valor "0". Ao encerrar, o programa deverá exibir quantos valores inválidos foram digitados

peso = int(input("Digite o peso dos produtos: "))
contador_invalido = 0

while peso != 0:
    peso = int(input("Digite o peso dos produtos: "))
    if peso > 900 or peso < 100:
        contador_invalido=contador_invalido+1
print(f"A quantidade de vezes que um valor invalido foi digitado foi de: {contador_invalido} vezes!")

#7. Escreva um programa para apresentar na tela os 7 primeiros números múltiplos de 7.
#Sugestão: Utilize a operação "resto", que captura o resto da divisão inteira

n = 7
multiplos = [ ]
for i in range(1, n+1):
    multiplos.append(7 * i)
print(f"Os sete primeiros multiplos de 7, são: {multiplos}")

#8 Construa um programa que registre diferentes notas de alunos de uma mesma turma. Ao
#ser digitado o valor 0, o programa deverá ser interrompido e apresentar na tela a média das
#notas informadas até então.

notas = [ ]
nota = 1
while nota != 0:
     nota =(float(input(f"Digite o valor da nota:")))
     notas.append(nota)
soma = 0
for nota in notas:
    soma = soma + nota
notas=notas[:-1]
media = soma / len(notas)
print(f"O valor da média é {round(media,2)}")

