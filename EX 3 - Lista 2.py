nome = input("Nome do funcionário: ") 
tempo = int(input("Anos de trabalho: ")) 
salario_atual = float(input("Salário atual: ")) 
dependentes = int(input("Numero de dependentes: ")) 
 
if tempo >= 4 and salario_atual < 500 and dependentes > 3: 
    print(f"{nome}, você pode receber um aumento!") 
    porcentagem = salario_atual * 0.4 
    novo_salario = porcentagem + salario_atual 
    print(f"Salário atual: {salario_atual} \nAumento: {porcentagem:.2f} \nNovo salário: {novo_salario}") 
else: 
    print("Você não pode receber aumento...")